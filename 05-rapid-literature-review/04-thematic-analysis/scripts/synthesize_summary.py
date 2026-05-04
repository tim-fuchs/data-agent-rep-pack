import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import pandas as pd

from reusables import (
    OUTPUT_DIR,
    ProviderConfig,
    call_chat_completions,
    load_synthesis_provider,
    parse_model_json,
    reduce_whitespace,
)


THEMATIC_INPUT_FILE = OUTPUT_DIR / "synthesis_thematically_final.csv"
RELEVANCE_INPUT_FILE = OUTPUT_DIR / "relevance_combined.csv"
OUTPUT_FILE = OUTPUT_DIR / "synthesis_summary.md"

THEMATIC_REQUIRED_COLUMNS = [
    "article_ID",
    "requirement_type",
    "final_theme",
    "requirement",
    "exact_text_quote",
]
RELEVANCE_REQUIRED_COLUMNS = ["article_ID", "mean"]

THEME_SUMMARY_SYSTEM_PROMPT = "Return only a valid JSON object with key 'summary'."
THEME_SUMMARY_USER_PROMPT = (
    "You are assisting with thematic synthesis for a systematic literature review.\n"
    "Write one concise but detailed prose summary for one final theme.\n\n"
    "Requirement type: {requirement_type}\n"
    "Final theme: {final_theme}\n\n"
    "Evidence rows are ordered by relevance score (high to low).\n"
    "Prioritization rules:\n"
    "- Prioritize and foreground evidence from higher-score articles.\n"
    "- Deprioritize lower-score articles unless they add unique or contrasting evidence.\n"
    "- Keep the summary grounded only in the provided requirements and quotes.\n"
    "- If scores disagree with each other, briefly note the contrast.\n\n"
    "Style rules:\n"
    "- Use one paragraph with 2-5 sentences.\n"
    "- Be concise but specific.\n"
    "- Use an objective academic tone.\n"
    "- Do not use bullet points.\n\n"
    "Output rules:\n"
    "- Return ONLY one JSON object in this format:\n"
    "{{\n"
    '  "summary": "theme summary"\n'
    "}}\n\n"
    "Evidence JSON:\n{rows_json}"
)


@dataclass(frozen=True)
class ThemeSummary:
    """Structured summary payload for one requirement type + final theme."""

    requirement_type: str
    final_theme: str
    summary: str
    rows: pd.DataFrame


def parse_relevance_score(raw_value: str) -> float | None:
    """Parse one relevance score value and validate the allowed range [0, 1]."""
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


def load_relevance_scores(
    input_file: Path,
) -> tuple[dict[str, float | None], dict[str, int]]:
    """Load article relevance scores from the combined relevance CSV."""
    if not input_file.exists() or not input_file.is_file():
        raise FileNotFoundError(f"Required input file not found: {input_file}")

    try:
        dataframe = pd.read_csv(input_file, dtype=str, keep_default_na=False)
    except (OSError, pd.errors.ParserError) as error:
        raise ValueError(f"Failed reading relevance input CSV: {error}") from error

    missing_columns = [
        column for column in RELEVANCE_REQUIRED_COLUMNS if column not in dataframe
    ]
    if missing_columns:
        raise ValueError(
            "Relevance CSV is missing required column(s): "
            f"{', '.join(missing_columns)}"
        )

    counters = {
        "rows_read": len(dataframe),
        "rows_skipped_missing_article_id": 0,
        "scores_ignored_invalid_or_missing": 0,
        "duplicate_rows_overwritten": 0,
    }

    relevance_lookup: dict[str, float | None] = {}
    records = cast(list[dict[str, Any]], dataframe.to_dict(orient="records"))
    for record in records:
        article_id = str(record.get("article_ID", "")).strip()
        if not article_id:
            counters["rows_skipped_missing_article_id"] += 1
            continue

        score = parse_relevance_score(str(record.get("mean", "")))
        if score is None:
            counters["scores_ignored_invalid_or_missing"] += 1

        if article_id in relevance_lookup:
            counters["duplicate_rows_overwritten"] += 1

        relevance_lookup[article_id] = score

    return relevance_lookup, counters


def load_thematic_dataframe(input_file: Path) -> tuple[pd.DataFrame, dict[str, int]]:
    """Load and validate thematic synthesis rows for summary generation."""
    if not input_file.exists() or not input_file.is_file():
        raise FileNotFoundError(f"Required input file not found: {input_file}")

    try:
        dataframe = pd.read_csv(input_file, dtype=str, keep_default_na=False)
    except (OSError, pd.errors.ParserError) as error:
        raise ValueError(f"Failed reading thematic input CSV: {error}") from error

    missing_columns = [
        column for column in THEMATIC_REQUIRED_COLUMNS if column not in dataframe
    ]
    if missing_columns:
        raise ValueError(
            "Thematic CSV is missing required column(s): "
            f"{', '.join(missing_columns)}"
        )

    row_count_before_filter = len(dataframe)
    dataframe = dataframe[THEMATIC_REQUIRED_COLUMNS].copy()
    for column in THEMATIC_REQUIRED_COLUMNS:
        dataframe[column] = dataframe[column].map(lambda value: str(value).strip())

    valid_rows_mask = (
        dataframe["article_ID"].astype(bool)
        & dataframe["requirement_type"].astype(bool)
        & dataframe["final_theme"].astype(bool)
        & dataframe["requirement"].astype(bool)
    )
    skipped_rows = int((~valid_rows_mask).sum())

    dataframe = dataframe.loc[valid_rows_mask].copy()
    if dataframe.empty:
        raise ValueError(
            "Thematic CSV does not contain any usable rows with "
            "article_ID, requirement_type, final_theme, and requirement"
        )

    counters = {
        "rows_read": row_count_before_filter,
        "rows_skipped_missing_required_fields": skipped_rows,
    }
    return dataframe, counters


def attach_relevance_scores(
    thematic_dataframe: pd.DataFrame,
    relevance_lookup: dict[str, float | None],
) -> pd.DataFrame:
    """Attach mean relevance score to each thematic row via article_ID."""
    dataframe = thematic_dataframe.copy()
    dataframe["score_numeric"] = pd.to_numeric(
        dataframe["article_ID"].map(relevance_lookup),
        errors="coerce",
    )
    return dataframe


def sort_output_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Sort rows by requirement type, final theme, then score descending."""
    sorted_dataframe = dataframe.assign(
        _sort_requirement_type=dataframe["requirement_type"].str.casefold(),
        _sort_final_theme=dataframe["final_theme"].str.casefold(),
        _sort_score_missing=dataframe["score_numeric"].isna(),
        _sort_article_id=dataframe["article_ID"].str.casefold(),
        _sort_requirement=dataframe["requirement"].str.casefold(),
    ).sort_values(
        by=[
            "_sort_requirement_type",
            "_sort_final_theme",
            "_sort_score_missing",
            "score_numeric",
            "_sort_article_id",
            "_sort_requirement",
        ],
        ascending=[True, True, True, False, True, True],
        kind="mergesort",
    )

    return sorted_dataframe.drop(
        columns=[
            "_sort_requirement_type",
            "_sort_final_theme",
            "_sort_score_missing",
            "_sort_article_id",
            "_sort_requirement",
        ]
    )


def build_theme_summary_user_prompt(
    requirement_type: str,
    final_theme: str,
    rows: pd.DataFrame,
) -> str:
    """Build one summary-generation prompt for a specific final theme."""
    payload: list[dict[str, str]] = []
    records = cast(list[dict[str, Any]], rows.to_dict(orient="records"))

    for record in records:
        score_value = record.get("score_numeric")
        score_text = ""
        if not pd.isna(score_value):
            score_text = f"{float(score_value):.2f}"

        payload.append(
            {
                "score": score_text,
                "article_ID": str(record.get("article_ID", "")).strip(),
                "requirement": reduce_whitespace(str(record.get("requirement", ""))),
                "exact_text_quote": reduce_whitespace(
                    str(record.get("exact_text_quote", ""))
                ),
            }
        )

    return THEME_SUMMARY_USER_PROMPT.format(
        requirement_type=requirement_type,
        final_theme=final_theme,
        rows_json=json.dumps(payload, ensure_ascii=True),
    )


def parse_theme_summary(
    raw_text: str,
    requirement_type: str,
    final_theme: str,
) -> str:
    """Parse and validate summary text from model JSON output."""
    parsed = parse_model_json(raw_text)
    summary_text = reduce_whitespace(str(parsed.get("summary", "")))

    if not summary_text:
        raise ValueError(
            "Model output is missing a non-empty 'summary' for "
            f"requirement_type='{requirement_type}', final_theme='{final_theme}'"
        )

    return summary_text


def summarize_themes(
    provider: ProviderConfig,
    dataframe: pd.DataFrame,
) -> list[ThemeSummary]:
    """Generate one weighted prose summary for each requirement_type + final_theme group."""
    summaries: list[ThemeSummary] = []

    grouped = dataframe.groupby(["requirement_type", "final_theme"], sort=False)
    for (requirement_type, final_theme), group in grouped:
        requirement_type_text = str(requirement_type).strip()
        final_theme_text = str(final_theme).strip()
        group_frame = (
            group.to_frame().T if isinstance(group, pd.Series) else pd.DataFrame(group)
        )

        user_prompt = build_theme_summary_user_prompt(
            requirement_type_text,
            final_theme_text,
            group_frame,
        )
        raw_response = call_chat_completions(
            provider,
            THEME_SUMMARY_SYSTEM_PROMPT,
            user_prompt,
        )
        summary_text = parse_theme_summary(
            raw_response,
            requirement_type_text,
            final_theme_text,
        )

        summaries.append(
            ThemeSummary(
                requirement_type=requirement_type_text,
                final_theme=final_theme_text,
                summary=summary_text,
                rows=group_frame.copy(),
            )
        )

    return summaries


def escape_markdown_cell(value: str) -> str:
    """Escape markdown table cell content so long quotes stay in one row."""
    normalized = str(value).replace("\r\n", "\n").replace("\r", "\n").strip()
    normalized = normalized.replace("|", "\\|")
    normalized = normalized.replace("\n", "<br>")
    return normalized


def format_score(value: Any) -> str:
    """Format score values for markdown output."""
    if pd.isna(value):
        return "N/A"

    try:
        return f"{float(value):.2f}"
    except (TypeError, ValueError):
        return "N/A"


def build_markdown_report(theme_summaries: list[ThemeSummary]) -> str:
    """Render all summaries and evidence rows as markdown."""
    lines = ["# Summary of the Literature Review", ""]

    current_requirement_type = ""
    for theme_summary in theme_summaries:
        if theme_summary.requirement_type != current_requirement_type:
            if current_requirement_type:
                lines.append("")
            current_requirement_type = theme_summary.requirement_type
            lines.append(f"## {current_requirement_type}")
            lines.append("")

        lines.append(f"### {theme_summary.final_theme}")
        lines.append("")
        lines.append(theme_summary.summary)
        lines.append("")
        lines.append("<details><summary>Requirements</summary>")
        lines.append("")
        lines.append("| Score | Art ID | Requirement | Text Quote |")
        lines.append("| --- | --- | --- | --- |")

        records = cast(
            list[dict[str, Any]], theme_summary.rows.to_dict(orient="records")
        )
        for record in records:
            lines.append(
                "| "
                f"{format_score(record.get('score_numeric'))} | "
                f"{escape_markdown_cell(str(record.get('article_ID', '')))} | "
                f"{escape_markdown_cell(str(record.get('requirement', '')))} | "
                f"{escape_markdown_cell(str(record.get('exact_text_quote', '')))} "
                "|"
            )

        lines.append("</details>")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main() -> int:
    """Create a weighted narrative summary report grouped by requirement type and theme."""
    try:
        provider = load_synthesis_provider()
        thematic_dataframe, thematic_counters = load_thematic_dataframe(
            THEMATIC_INPUT_FILE
        )
        relevance_lookup, relevance_counters = load_relevance_scores(
            RELEVANCE_INPUT_FILE
        )
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Initialization failed: {error}")
        return 1

    enriched_dataframe = attach_relevance_scores(thematic_dataframe, relevance_lookup)
    rows_without_numeric_scores = int(enriched_dataframe["score_numeric"].isna().sum())
    sorted_dataframe = sort_output_dataframe(enriched_dataframe)

    try:
        theme_summaries = summarize_themes(provider, sorted_dataframe)
    except (RuntimeError, ValueError) as error:
        print(f"Processing failed: {error}")
        return 1

    markdown_output = build_markdown_report(theme_summaries)

    try:
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text(markdown_output, encoding="utf-8")
    except OSError as error:
        print(f"Output write failed: {error}")
        return 1

    print(f"Rows read (thematic): {thematic_counters['rows_read']}")
    print(
        "Rows skipped (missing article_ID, requirement_type, final_theme, or requirement): "
        f"{thematic_counters['rows_skipped_missing_required_fields']}"
    )
    print(f"Rows read (relevance): {relevance_counters['rows_read']}")
    print(
        "Rows skipped in relevance (missing article_ID): "
        f"{relevance_counters['rows_skipped_missing_article_id']}"
    )
    print(
        "Relevance scores ignored (missing/invalid/non-numeric/out-of-range): "
        f"{relevance_counters['scores_ignored_invalid_or_missing']}"
    )
    print(
        "Duplicate relevance rows overwritten: "
        f"{relevance_counters['duplicate_rows_overwritten']}"
    )
    print(f"Rows without numeric relevance score: {rows_without_numeric_scores}")
    print(f"Themes summarized: {len(theme_summaries)}")
    print(f"Rows written: {len(sorted_dataframe)}")
    print(f"Output file: {OUTPUT_FILE}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
