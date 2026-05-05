import csv
from pathlib import Path
from typing import Sequence

from reusables import OUTPUT_DIR, append_results_csv, reset_results_csv


INPUT_PREFIX = "requirements_"
INPUT_SUFFIX = ".csv"
OUTPUT_FILE_NAME = "requirements_combined.csv"
REQUIRED_COLUMNS = ("requirement_type", "requirement", "exact_text_quote")
OUTPUT_HEADERS = ["article_ID", *REQUIRED_COLUMNS]
ARTICLE_ID_COLUMNS = ("article_ID", "ID")


def discover_requirement_files(results_dir: Path) -> list[Path]:
    """Discover requirement files from the results folder."""
    requirement_files: list[Path] = []

    for path in sorted(results_dir.glob(f"{INPUT_PREFIX}*{INPUT_SUFFIX}")):
        if path.name == OUTPUT_FILE_NAME:
            continue
        requirement_files.append(path)

    return requirement_files


def select_article_id_column(fieldnames: Sequence[str] | None) -> str:
    """Select a supported article ID column from a CSV header."""
    if not fieldnames:
        raise ValueError("CSV is missing header columns")

    for column in ARTICLE_ID_COLUMNS:
        if column in fieldnames:
            return column

    raise ValueError(
        "CSV must include one of the article ID columns: "
        f"{', '.join(ARTICLE_ID_COLUMNS)}"
    )


def validate_required_columns(fieldnames: Sequence[str] | None, csv_name: str) -> None:
    """Validate that all required requirement columns are present in the CSV."""
    missing_columns = [
        column for column in REQUIRED_COLUMNS if column not in (fieldnames or [])
    ]

    if missing_columns:
        raise ValueError(
            f"{csv_name} is missing required column(s): {', '.join(missing_columns)}"
        )


def load_requirement_rows(
    csv_file: Path,
    combined_rows: list[dict[str, str]],
    counters: dict[str, int],
) -> None:
    """Load requirement rows into the combined row collection."""
    with csv_file.open("r", encoding="utf-8", newline="") as file_handle:
        reader = csv.DictReader(file_handle)
        validate_required_columns(reader.fieldnames, csv_file.name)
        article_id_column = select_article_id_column(reader.fieldnames)

        for row in reader:
            counters["rows_read"] += 1

            article_id = str(row.get(article_id_column, "")).strip()
            requirement_type = str(row.get("requirement_type", "")).strip()
            requirement = str(row.get("requirement", "")).strip()
            exact_text_quote = str(row.get("exact_text_quote", "")).strip()

            if not article_id:
                counters["rows_skipped_missing_article_id"] += 1
                continue

            if not requirement_type or not requirement:
                counters["rows_skipped_missing_required_fields"] += 1
                continue

            combined_rows.append(
                {
                    "article_ID": article_id,
                    "requirement_type": requirement_type,
                    "requirement": requirement,
                    "exact_text_quote": exact_text_quote,
                }
            )


def sort_requirement_rows(rows: list[dict[str, str]]) -> None:
    """Sort rows by article ID, requirement type, and requirement text."""
    rows.sort(
        key=lambda row: (
            row["article_ID"].casefold(),
            row["requirement_type"].casefold(),
            row["requirement"].casefold(),
        )
    )


def main() -> int:
    """Combine requirement rows from all providers into one sorted CSV file."""
    if not OUTPUT_DIR.exists() or not OUTPUT_DIR.is_dir():
        print(f"Initialization failed: Required results folder not found: {OUTPUT_DIR}")
        return 1

    requirement_files = discover_requirement_files(OUTPUT_DIR)
    if not requirement_files:
        print(
            "Initialization failed: No requirements files found in "
            f"{OUTPUT_DIR} matching '{INPUT_PREFIX}*{INPUT_SUFFIX}'"
        )
        return 1

    combined_rows: list[dict[str, str]] = []
    counters = {
        "rows_read": 0,
        "rows_skipped_missing_article_id": 0,
        "rows_skipped_missing_required_fields": 0,
    }

    try:
        for csv_file in requirement_files:
            load_requirement_rows(csv_file, combined_rows, counters)
    except (OSError, ValueError) as error:
        print(f"Processing failed: {error}")
        return 1

    sort_requirement_rows(combined_rows)
    output_file = OUTPUT_DIR / OUTPUT_FILE_NAME

    try:
        reset_results_csv(output_file, OUTPUT_HEADERS)
        append_results_csv(output_file, OUTPUT_HEADERS, combined_rows)
    except OSError as error:
        print(f"Output write failed: {error}")
        return 1

    print(f"Requirement files discovered: {len(requirement_files)}")
    print(f"Rows read: {counters['rows_read']}")
    print(f"Rows combined: {len(combined_rows)}")
    print(
        "Rows skipped (missing article ID): "
        f"{counters['rows_skipped_missing_article_id']}"
    )
    print(
        "Rows skipped (missing requirement_type or requirement): "
        f"{counters['rows_skipped_missing_required_fields']}"
    )
    print("Sorted by: article_ID, requirement_type, requirement")
    print(f"Output file: {output_file}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
