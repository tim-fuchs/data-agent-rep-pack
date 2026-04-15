import csv
from pathlib import Path
from statistics import mean


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT_CSV = DATA_DIR / "character_count.csv"
SOURCE_DIRS = {
    "markdown": DATA_DIR / "markdown",
    "markdown_cleaned": DATA_DIR / "markdown_cleaned",
}


def get_counts(folder: Path) -> dict[str, int]:
    """Return character counts keyed by file stem for all Markdown files in a folder."""
    return {
        file_path.stem: len(file_path.read_text(encoding="utf-8", errors="ignore"))
        for file_path in sorted(folder.glob("*.md"))
        if file_path.is_file()
    }


def main() -> int:
    """Create character_count.csv comparing markdown and markdown_cleaned file sizes."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    active_sources = [
        (name, path) for name, path in SOURCE_DIRS.items() if path.is_dir()
    ]

    if not active_sources:
        OUTPUT_CSV.write_text("", encoding="utf-8")
        return 0

    counts_by_column = {name: get_counts(path) for name, path in active_sources}
    ids = sorted(
        {file_id for counts in counts_by_column.values() for file_id in counts}
    )
    columns = [name for name, _ in active_sources]

    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["ID", *columns])

        for file_id in ids:
            writer.writerow(
                [file_id, *[counts_by_column[col].get(file_id, "") for col in columns]]
            )

        means = [
            mean(values.values()) if values else ""
            for values in (counts_by_column[col] for col in columns)
        ]
        writer.writerow(["MEAN", *means])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
