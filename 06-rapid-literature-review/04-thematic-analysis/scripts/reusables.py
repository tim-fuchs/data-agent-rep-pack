import csv
from dataclasses import dataclass
from dotenv import load_dotenv
import json
from pathlib import Path
import os
import re
from openai import OpenAI
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent / "data"
INPUT_DIR = BASE_DIR / "articles"
OUTPUT_DIR = BASE_DIR / "results"
ANALYZERS_ENV_VAR = "ANALYZERS"

OPENAI_ANALYZER = "openai"
NEBIUS_ANALYZER = "nebius"
TEMPERATURE = 0.1  # Low model temperature for more consistent results, while allowing flexibility in reasoning

SUPPORTED_ANALYZERS = (OPENAI_ANALYZER, NEBIUS_ANALYZER)
DEFAULT_ANALYZERS = f"{OPENAI_ANALYZER},{NEBIUS_ANALYZER}"

SYNTHESIS_API_KEY_ENV = "SYNTHESIS_API_KEY"
SYNTHESIS_MODEL_ENV = "SYNTHESIS_MODEL"
SYNTHESIS_TIMEOUT_ENV = "SYNTHESIS_TIMEOUT_SECONDS"
SYNTHESIS_BASE_URL_ENV = "SYNTHESIS_BASE_URL"

PROVIDER_ENV_VARS = {
    OPENAI_ANALYZER: {
        "api_key": "OPENAI_API_KEY",
        "timeout_seconds": "OPENAI_TIMEOUT_SECONDS",
        "model": "OPENAI_MODEL",
        "base_url": "OPENAI_BASE_URL",
    },
    NEBIUS_ANALYZER: {
        "api_key": "NEBIUS_API_KEY",
        "timeout_seconds": "NEBIUS_TIMEOUT_SECONDS",
        "model": "NEBIUS_MODEL",
        "base_url": "NEBIUS_BASE_URL",
    },
}


@dataclass(frozen=True)
class ProviderConfig:
    """Provider-specific settings for an OpenAI-compatible chat endpoint."""

    name: str
    api_key: str
    model: str
    base_url: str
    timeout_seconds: float


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from required environment variables."""

    analyzers: tuple[str, ...]
    providers: dict[str, ProviderConfig]


def read_required_env(name: str) -> str:
    """Read a required non-empty environment variable."""
    value = os.getenv(name)
    if value is None or not value.strip():
        raise ValueError(f"Missing required environment variable: {name}")
    return value.strip()


def parse_positive_timeout(value: str, env_var_name: str) -> float:
    """Parse and validate a positive timeout value from an environment variable."""
    try:
        timeout_seconds = float(value)
    except ValueError as error:
        raise ValueError(f"{env_var_name} must be a number (seconds)") from error

    if timeout_seconds <= 0:
        raise ValueError(f"{env_var_name} must be greater than 0")

    return timeout_seconds


def load_synthesis_provider() -> ProviderConfig:
    """Load model-agnostic synthesis provider settings from environment variables."""
    load_dotenv()

    api_key = read_required_env(SYNTHESIS_API_KEY_ENV)
    model = read_required_env(SYNTHESIS_MODEL_ENV)
    timeout_seconds = parse_positive_timeout(
        read_required_env(SYNTHESIS_TIMEOUT_ENV),
        SYNTHESIS_TIMEOUT_ENV,
    )
    base_url = read_required_env(SYNTHESIS_BASE_URL_ENV)

    return ProviderConfig(
        name="synthesis",
        api_key=api_key,
        model=model,
        base_url=base_url,
        timeout_seconds=timeout_seconds,
    )


def parse_analyzers(raw_value: str) -> tuple[str, ...]:
    """Parse analyzer selection from ANALYZERS env var."""
    names = tuple(
        analyzer.strip().lower()
        for analyzer in raw_value.split(",")
        if analyzer.strip()
    )

    if not names:
        raise ValueError(
            f"{ANALYZERS_ENV_VAR} must include at least one analyzer "
            f"({', '.join(SUPPORTED_ANALYZERS)})"
        )

    unknown = sorted({name for name in names if name not in SUPPORTED_ANALYZERS})
    if unknown:
        raise ValueError(
            f"Unsupported analyzer(s) in {ANALYZERS_ENV_VAR}: {', '.join(unknown)}. "
            f"Supported values: {', '.join(SUPPORTED_ANALYZERS)}"
        )

    # Preserve order while removing duplicates.
    deduplicated: list[str] = []
    for name in names:
        if name not in deduplicated:
            deduplicated.append(name)

    return tuple(deduplicated)


def load_provider_config(provider_name: str) -> ProviderConfig:
    """Load and validate provider configuration for one analyzer."""
    env_keys = PROVIDER_ENV_VARS[provider_name]
    api_key = read_required_env(env_keys["api_key"])
    model = read_required_env(env_keys["model"])
    timeout_seconds = parse_positive_timeout(
        read_required_env(env_keys["timeout_seconds"]),
        env_keys["timeout_seconds"],
    )
    base_url = read_required_env(env_keys["base_url"])

    return ProviderConfig(
        name=provider_name,
        api_key=api_key,
        timeout_seconds=timeout_seconds,
        model=model,
        base_url=base_url,
    )


def load_settings() -> Settings:
    """Load required environment variables and return validated settings."""
    load_dotenv()
    raw_analyzers = os.getenv(ANALYZERS_ENV_VAR, DEFAULT_ANALYZERS)
    analyzers = parse_analyzers(raw_analyzers)

    providers = {analyzer: load_provider_config(analyzer) for analyzer in analyzers}

    return Settings(analyzers=analyzers, providers=providers)


def get_provider_config(settings: Settings, analyzer: str) -> ProviderConfig:
    """Return provider settings for one analyzer name."""
    normalized_analyzer = analyzer.strip().lower()

    try:
        return settings.providers[normalized_analyzer]
    except KeyError as error:
        raise ValueError(
            f"Analyzer '{analyzer}' is not enabled. Enabled analyzers: "
            f"{', '.join(settings.analyzers)}"
        ) from error


def ensure_paths(input_dir: Path, output_file: Path) -> None:
    """Validate input directory and create output parent folder."""
    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"Required input folder not found: {input_dir}")

    output_file.parent.mkdir(parents=True, exist_ok=True)


def discover_markdown_files(folder: Path) -> list[Path]:
    """Return sorted Markdown files from the input folder."""
    return sorted(
        file_path
        for file_path in folder.iterdir()
        if file_path.is_file() and file_path.suffix.lower() == ".md"
    )


def read_article_text(file_path: Path) -> str:
    """Read one article as UTF-8 and reject empty content."""
    content = file_path.read_text(encoding="utf-8", errors="ignore").strip()
    if not content:
        raise ValueError("Article is empty after decoding")
    return content


def build_user_prompt(prompt: str, article_id: str, article_text: str) -> str:
    """Build the LLM prompt for requirement extraction."""
    return f"{prompt}\n Article ID: {article_id}\n Article text:\n{article_text}"


def reduce_whitespace(value: str) -> str:
    """Reduce whitespace to keep CSV cells compact."""
    return re.sub(r"\s+", " ", value).strip()


def output_file_for_analyzer(output_prefix: str, analyzer: str) -> Path:
    """Return provider-specific output path for a given analysis prefix."""
    return OUTPUT_DIR / f"{output_prefix}_{analyzer}.csv"


def call_chat_completions(
    provider: ProviderConfig,
    system_prompt: str,
    user_prompt: str,
) -> str:
    """Call one OpenAI-compatible Chat Completions endpoint and return response text."""
    client = OpenAI(
        api_key=provider.api_key,
        base_url=provider.base_url,
        timeout=provider.timeout_seconds,
    )

    try:
        response = client.chat.completions.create(
            model=provider.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=TEMPERATURE,
        )
    except Exception as error:
        error_name = type(error).__name__.lower()
        if "timeout" in error_name:
            raise RuntimeError(f"{provider.name} request timed out: {error}") from error
        if "connection" in error_name:
            raise RuntimeError(f"{provider.name} connection failed: {error}") from error
        raise RuntimeError(f"{provider.name} request failed: {error}") from error

    try:
        model_response = response.choices[0].message.content
    except (AttributeError, IndexError, TypeError) as error:
        raise ValueError(
            f"{provider.name} response is missing message content"
        ) from error

    if not isinstance(model_response, str) or not model_response.strip():
        raise ValueError(f"{provider.name} response missing non-empty message content")

    return model_response.strip()


def call_analyzer(
    settings: Settings,
    analyzer: str,
    system_prompt: str,
    user_prompt: str,
) -> str:
    """Call one configured analyzer by name and return model response text."""
    provider = get_provider_config(settings, analyzer)
    return call_chat_completions(provider, system_prompt, user_prompt)


def parse_model_json(raw_text: str) -> dict[str, Any]:
    """Parse model text into a JSON object with fallback extraction."""
    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", raw_text, flags=re.DOTALL)
        if not match:
            raise ValueError("Model output does not contain a JSON object")
        parsed = json.loads(match.group(0))

    if not isinstance(parsed, dict):
        raise ValueError("Model output JSON must be an object")

    return parsed


def write_results_csv(
    output_file: Path,
    headers: list[str],
    rows: list[dict[str, str]],
) -> None:
    """Write all relevance rows to CSV output."""
    with output_file.open("w", encoding="utf-8", newline="") as file_handle:
        writer = csv.DictWriter(file_handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def reset_results_csv(output_file: Path, headers: list[str]) -> None:
    """Truncate an output CSV and write only the header row."""
    with output_file.open("w", encoding="utf-8", newline="") as file_handle:
        writer = csv.DictWriter(file_handle, fieldnames=headers)
        writer.writeheader()


def append_results_csv(
    output_file: Path,
    headers: list[str],
    rows: list[dict[str, str]],
) -> None:
    """Append one or more rows to an existing CSV output file."""
    if not rows:
        return

    with output_file.open("a", encoding="utf-8", newline="") as file_handle:
        writer = csv.DictWriter(file_handle, fieldnames=headers)
        writer.writerows(rows)
