import csv
import re
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlparse
from bs4 import BeautifulSoup


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
SCHOLAR_RAW_DIR = DATA_DIR / "scholar"
GOOGLE_RAW_DIR = DATA_DIR / "google"
CONSENSUS_RAW_DIR = DATA_DIR / "consensus"
ADDITIONAL_PAPERS_RAW_DIR = DATA_DIR / "additional-papers"
OUTPUT_CSV = DATA_DIR / "sources.csv"

TITLE_PREFIX_RE = re.compile(
    r"^(?:(?:\[(?:PDF|HTML)\]|\((?:PDF|HTML)\)|\[\d{4}\.\d{4,5}(?:v\d+)?\])\s*)+",
    flags=re.IGNORECASE,
)
DOI_PREFIX_RE = re.compile(r"^https?://(?:dx\.)?doi\.org/", flags=re.IGNORECASE)

MOJIBAKE_REPLACEMENTS = {
    "\u201a\u00c4\u00fa": '"',
    "\u201a\u00c4\u00f9": '"',
    "\u201a\u00c4\u00f4": "'",
    "\u201a\u00c4\u00f2": "'",
    "\u00e2\u20ac\u0153": '"',
    "\u00e2\u20ac\u009d": '"',
    "\u00e2\u20ac\u02dc": "'",
    "\u00e2\u20ac\u2122": "'",
}


def discover_files(folder: Path, suffix: str) -> list[Path]:
    """Return sorted files in a folder that match the requested suffix."""
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Required folder not found: {folder}")

    files = [
        file_path
        for file_path in folder.iterdir()
        if file_path.is_file() and file_path.suffix.lower() == suffix
    ]
    return sorted(files)


def clean_title(title: str) -> str:
    """Normalize whitespace and strip repeated leading media badges."""
    normalized = " ".join(title.split())
    for malformed, replacement in MOJIBAKE_REPLACEMENTS.items():
        normalized = normalized.replace(malformed, replacement)

    cleaned = TITLE_PREFIX_RE.sub("", normalized)
    return " ".join(cleaned.split()).strip()


def href_to_string(raw_href: object) -> str:
    """Convert BeautifulSoup href values into a clean string."""
    if isinstance(raw_href, list):
        return " ".join(str(value) for value in raw_href).strip()
    if isinstance(raw_href, str):
        return raw_href.strip()
    return ""


def normalize_http_link(base_url: str, href: str) -> str:
    """Resolve href against a base URL and keep only HTTP(S) links."""
    if not href:
        return ""

    link = urljoin(base_url, href)
    parsed = urlparse(link)
    if parsed.scheme.lower() not in {"http", "https"}:
        return ""
    return link


def unwrap_google_link(link: str) -> str:
    """Unwrap Google redirect links and return the final destination URL."""
    parsed = urlparse(link)
    if parsed.path != "/url":
        return link

    params = parse_qs(parsed.query)
    for key in ("url", "q"):
        values = params.get(key)
        if not values:
            continue

        candidate = values[0].strip()
        candidate_parsed = urlparse(candidate)
        if candidate_parsed.scheme.lower() in {"http", "https"}:
            return candidate

    return link


def extract_entries_from_html(
    html_path: Path, base_url: str, use_parent_anchor: bool
) -> list[tuple[str, str]]:
    """Extract normalized title/link pairs from h3-based HTML result entries."""
    html_text = html_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html_text, "html.parser")

    entries: list[tuple[str, str]] = []
    for h3 in soup.find_all("h3"):
        title = clean_title(h3.get_text(" ", strip=True))
        if not title:
            continue

        anchor = h3.find("a", href=True)
        if anchor is None and use_parent_anchor:
            parent = h3.parent
            while parent is not None and getattr(parent, "name", None) not in {
                None,
                "[document]",
            }:
                if getattr(parent, "name", None) == "a" and parent.get("href"):
                    anchor = parent
                    break
                parent = parent.parent

        if anchor is None:
            continue

        href = href_to_string(anchor.get("href"))
        link = normalize_http_link(base_url, href)
        if not link:
            continue

        if use_parent_anchor:
            link = unwrap_google_link(link)
            link = normalize_http_link(base_url, link)
            if not link:
                continue

        entries.append((title, link))

    return entries


def normalize_doi(value: str) -> str:
    """Normalize DOI values by removing common URL and doi: prefixes."""
    doi = value.strip()
    doi = DOI_PREFIX_RE.sub("", doi)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    return doi.strip()


def row_value(row: dict[str, str], target_key: str) -> str:
    """Fetch a CSV row value by key with BOM-safe case-insensitive matching."""
    target = target_key.lower()
    for key, value in row.items():
        normalized_key = str(key).lstrip("\ufeff").strip().lower()
        if normalized_key == target:
            return (value or "").strip()
    return ""


def extract_entries_from_consensus(csv_path: Path) -> list[tuple[str, str]]:
    """Extract title/link pairs from consensus CSV rows using DOI links."""
    entries: list[tuple[str, str]] = []

    with csv_path.open(newline="", encoding="utf-8", errors="ignore") as file_handle:
        reader = csv.DictReader(file_handle)
        for row in reader:
            title = clean_title(row_value(row, "Title"))
            doi = normalize_doi(row_value(row, "DOI"))
            if not title or not doi:
                continue

            link = f"https://doi.org/{doi}"
            entries.append((title, link))

    return entries


def extract_entries_from_additional_papers(csv_path: Path) -> list[tuple[str, str]]:
    """Extract title/link pairs from additional papers CSV rows."""
    entries: list[tuple[str, str]] = []

    with csv_path.open(newline="", encoding="utf-8", errors="ignore") as file_handle:
        reader = csv.DictReader(file_handle)
        for row in reader:
            title = clean_title(row_value(row, "Title"))
            link = normalize_http_link("", row_value(row, "Link"))
            if not title or not link:
                continue

            entries.append((title, link))

    return entries


def build_rows(
    file_path: Path, entries: list[tuple[str, str]]
) -> list[tuple[str, str, str]]:
    """Build output rows with deterministic IDs for a file's entries."""
    rows: list[tuple[str, str, str]] = []
    for index, (title, link) in enumerate(entries, start=1):
        row_id = f"{file_path.stem}-{index:02d}"
        rows.append((row_id, title, link))
    return rows


def write_output(rows: list[tuple[str, str, str]], output_path: Path) -> None:
    """Write all aggregated rows to the output CSV with a fixed header."""
    with output_path.open("w", newline="", encoding="utf-8") as file_handle:
        writer = csv.writer(file_handle)
        writer.writerow(["ID", "Title", "Link"])
        writer.writerows(rows)


def main() -> int:
    """Run the full scrape workflow and return a process exit code."""
    try:
        scholar_files = discover_files(SCHOLAR_RAW_DIR, ".html")
        google_files = discover_files(GOOGLE_RAW_DIR, ".html")
        consensus_files = discover_files(CONSENSUS_RAW_DIR, ".csv")
        additional_paper_files = discover_files(ADDITIONAL_PAPERS_RAW_DIR, ".csv")
    except FileNotFoundError as error:
        print(error)
        return 1

    all_rows: list[tuple[str, str, str]] = []

    scholar_rows = 0
    for file_path in scholar_files:
        entries = extract_entries_from_html(
            file_path, "https://scholar.google.com", use_parent_anchor=False
        )
        rows = build_rows(file_path, entries)
        scholar_rows += len(rows)
        all_rows.extend(rows)

    google_rows = 0
    for file_path in google_files:
        entries = extract_entries_from_html(
            file_path, "https://www.google.com", use_parent_anchor=True
        )
        rows = build_rows(file_path, entries)
        google_rows += len(rows)
        all_rows.extend(rows)

    consensus_rows = 0
    for file_path in consensus_files:
        entries = extract_entries_from_consensus(file_path)
        rows = build_rows(file_path, entries)
        consensus_rows += len(rows)
        all_rows.extend(rows)

    additional_paper_rows = 0
    for file_path in additional_paper_files:
        entries = extract_entries_from_additional_papers(file_path)
        rows = build_rows(file_path, entries)
        additional_paper_rows += len(rows)
        all_rows.extend(rows)

    write_output(all_rows, OUTPUT_CSV)

    print(
        f"Scholar files: {len(scholar_files)}, rows: {scholar_rows}; "
        f"Google files: {len(google_files)}, rows: {google_rows}; "
        f"Consensus files: {len(consensus_files)}, rows: {consensus_rows}; "
        f"Additional papers files: {len(additional_paper_files)}, rows: {additional_paper_rows}; "
        f"Total rows written: {len(all_rows)} to {OUTPUT_CSV}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
