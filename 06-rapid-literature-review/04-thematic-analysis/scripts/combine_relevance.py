import csv
import math
from pathlib import Path
from statistics import fmean
from typing import Sequence

from reusables import OUTPUT_DIR, append_results_csv, reset_results_csv


INPUT_PREFIX = "relevance_"
INPUT_SUFFIX = ".csv"
OUTPUT_FILE_NAME = "relevance_combined.csv"
INPUT_SCORE_COLUMN = "relevance_score"
ARTICLE_ID_COLUMNS = ("article_ID", "ID")


def discover_relevance_files(results_dir: Path) -> list[tuple[str, Path]]:
    """Discover relevance files from the results folder."""
    relevance_files: list[tuple[str, Path]] = []

    for path in sorted(results_dir.glob(f"{INPUT_PREFIX}*{INPUT_SUFFIX}")):
        if path.name == OUTPUT_FILE_NAME:
            continue

        provider = path.stem[len(INPUT_PREFIX) :].strip().lower()
        if provider:
            relevance_files.append((provider, path))

    return relevance_files


def parse_relevance_score(raw_value: str) -> float | None:
    """Parse one relevance score value and validate allowed range."""
    cleaned = raw_value.strip()
    if not cleaned:
        return None

    try:
        score = float(cleaned)
    except ValueError:
        return None

    if score < 0.0 or score > 1.0:
        return None

    return score


def population_std(values: list[float], mean_value: float) -> float:
    """Compute population standard deviation (divide by N)."""
    if not values:
        return 0.0

    variance = sum((value - mean_value) ** 2 for value in values) / len(values)
    return math.sqrt(variance)


def select_article_id_column(fieldnames: Sequence[str] | None) -> str:
    """Select a supported article ID column from a CSV header."""
    if not fieldnames:
        raise ValueError("CSV is missing header columns")

    for column in ARTICLE_ID_COLUMNS:
        if column in fieldnames:
            return column

    raise ValueError(
        f"CSV must include one of the article ID columns: {', '.join(ARTICLE_ID_COLUMNS)}"
    )


def load_relevance_scores(
    provider: str,
    csv_file: Path,
    article_scores: dict[str, dict[str, float | None]],
    counters: dict[str, int],
) -> None:
    """Load relevance scores of a model provider into a nested dictionary keyed by article ID."""
    with csv_file.open("r", encoding="utf-8", newline="") as file_handle:
        reader = csv.DictReader(file_handle)

        if INPUT_SCORE_COLUMN not in (reader.fieldnames or []):
            raise ValueError(
                f"{csv_file.name} is missing required column '{INPUT_SCORE_COLUMN}'"
            )

        article_id_column = select_article_id_column(reader.fieldnames)

        for row in reader:
            counters["rows_read"] += 1

            article_id = str(row.get(article_id_column, "")).strip()
            if not article_id:
                counters["rows_skipped_missing_article_id"] += 1
                continue

            score = parse_relevance_score(str(row.get(INPUT_SCORE_COLUMN, "")))
            if score is None:
                counters["scores_ignored_invalid_or_missing"] += 1

            relevance_scores = article_scores.setdefault(article_id, {})
            if provider in relevance_scores:
                counters["duplicate_rows_overwritten"] += 1

            relevance_scores[provider] = score


def build_output_rows(
    article_scores: dict[str, dict[str, float | None]],
    providers: list[str],
    counters: dict[str, int],
) -> tuple[list[str], list[dict[str, str]]]:
    """Build CSV headers and rows for combined relevance output."""
    provider_columns = [f"relevance_score_{provider}" for provider in providers]
    headers = ["article_ID", *provider_columns, "mean", "std"]

    rows: list[dict[str, str]] = []

    for article_id in sorted(article_scores):
        provider_values = article_scores[article_id]
        numeric_scores = [
            score
            for score in (provider_values.get(provider) for provider in providers)
            if score is not None
        ]

        if numeric_scores:
            mean_value = fmean(numeric_scores)
            std_value = population_std(numeric_scores, mean_value)
            mean_text = f"{mean_value:.2f}"
            std_text = f"{std_value:.2f}"
        else:
            counters["articles_with_no_numeric_scores"] += 1
            mean_text = ""
            std_text = ""

        row = {
            "article_ID": article_id,
            "mean": mean_text,
            "std": std_text,
        }

        for provider in providers:
            score = provider_values.get(provider)
            row[f"relevance_score_{provider}"] = "" if score is None else f"{score:.2f}"

        rows.append(row)

    return headers, rows


def main() -> int:
    """Combine relevance scores from all providers and compute mean/std."""
    if not OUTPUT_DIR.exists() or not OUTPUT_DIR.is_dir():
        print(f"Initialization failed: Required results folder not found: {OUTPUT_DIR}")
        return 1

    relevance_files = discover_relevance_files(OUTPUT_DIR)
    if not relevance_files:
        print(
            "Initialization failed: No relevance files found in "
            f"{OUTPUT_DIR} matching '{INPUT_PREFIX}*{INPUT_SUFFIX}'"
        )
        return 1

    providers = [provider for provider, _ in relevance_files]
    article_scores: dict[str, dict[str, float | None]] = {}
    counters = {
        "rows_read": 0,
        "rows_skipped_missing_article_id": 0,
        "scores_ignored_invalid_or_missing": 0,
        "duplicate_rows_overwritten": 0,
        "articles_with_no_numeric_scores": 0,
    }

    try:
        for provider, csv_file in relevance_files:
            load_relevance_scores(provider, csv_file, article_scores, counters)
    except (OSError, ValueError) as error:
        print(f"Processing failed: {error}")
        return 1

    headers, rows = build_output_rows(article_scores, providers, counters)
    output_file = OUTPUT_DIR / OUTPUT_FILE_NAME

    try:
        reset_results_csv(output_file, headers)
        append_results_csv(output_file, headers, rows)
    except OSError as error:
        print(f"Output write failed: {error}")
        return 1

    print(f"Providers discovered: {', '.join(providers)}")
    print(f"Articles combined: {len(rows)}")
    print(
        "Scores ignored (missing/invalid/non-numeric/out-of-range): "
        f"{counters['scores_ignored_invalid_or_missing']}"
    )
    print(
        "Rows skipped (missing article ID): "
        f"{counters['rows_skipped_missing_article_id']}"
    )
    print(f"Duplicate rows overwritten: {counters['duplicate_rows_overwritten']}")
    print(
        "Articles without any numeric score: "
        f"{counters['articles_with_no_numeric_scores']}"
    )
    print(f"Output file: {output_file}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
