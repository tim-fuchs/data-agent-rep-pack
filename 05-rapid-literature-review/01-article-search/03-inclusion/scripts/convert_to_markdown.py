import re
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify
from pypdf import PdfReader
from pypdf.errors import PdfReadError


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
INPUT_DIR = DATA_DIR / "html_pdf"
OUTPUT_DIR = DATA_DIR / "markdown"

SUPPORTED_SUFFIXES = {".html", ".pdf"}
HTML_TAGS_TO_REMOVE = {
    "script",
    "style",
    "noscript",
    "svg",
    "canvas",
    "nav",
    "header",
    "footer",
    "aside",
    "form",
}


def ensure_paths(input_dir: Path, output_dir: Path) -> None:
    """Validate the input directory and create the output directory."""
    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"Required input folder not found: {input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)


def discover_files(folder: Path) -> list[Path]:
    """Return sorted, direct child files from the provided folder."""
    return sorted(file_path for file_path in folder.iterdir() if file_path.is_file())


def normalize_markdown(text: str) -> str:
    """Normalize whitespace and blank lines in Markdown output."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = "\n".join(line.rstrip() for line in normalized.split("\n"))
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def normalize_pdf_text(text: str) -> str:
    """Collapse noisy PDF text while keeping paragraph breaks readable."""
    lines = [line.strip() for line in text.splitlines()]
    cleaned: list[str] = []
    previous_blank = False

    for line in lines:
        if line:
            cleaned.append(line)
            previous_blank = False
            continue

        if not previous_blank:
            cleaned.append("")
            previous_blank = True

    return "\n".join(cleaned).strip()


def convert_html_to_markdown(html_path: Path) -> str:
    """Convert one HTML file to Markdown with lightweight cleanup."""
    html_text = html_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html_text, "html.parser")

    for tag_name in HTML_TAGS_TO_REMOVE:
        for tag in soup.find_all(tag_name):
            tag.decompose()

    content = soup.find("main") or soup.find("article") or soup.body or soup
    markdown = markdownify(
        str(content),
        heading_style="ATX",
        bullets="-",
        strip=list(HTML_TAGS_TO_REMOVE),
    )
    markdown = normalize_markdown(markdown)

    if not markdown:
        raise ValueError("No markdown content extracted from HTML file")

    return markdown


def convert_pdf_to_markdown(pdf_path: Path) -> str:
    """Convert one PDF file to Markdown by extracting per-page text."""
    reader = PdfReader(str(pdf_path))
    page_blocks: list[str] = []

    for page_index, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        cleaned_text = normalize_pdf_text(page_text)
        if not cleaned_text:
            continue

        page_blocks.append(f"## Page {page_index}\n\n{cleaned_text}")

    if not page_blocks:
        raise ValueError("No extractable text found in PDF file")

    return normalize_markdown("\n\n---\n\n".join(page_blocks))


def convert_file_to_markdown(file_path: Path) -> str:
    """Dispatch conversion based on file suffix and return Markdown output."""
    suffix = file_path.suffix.lower()
    if suffix == ".html":
        return convert_html_to_markdown(file_path)
    if suffix == ".pdf":
        return convert_pdf_to_markdown(file_path)

    raise ValueError(f"Unsupported file type: {file_path.suffix or '<none>'}")


def write_markdown(output_path: Path, markdown_text: str) -> None:
    """Write one Markdown file with trailing newline for consistency."""
    output_path.write_text(f"{markdown_text}\n", encoding="utf-8", errors="ignore")


def main() -> int:
    """Convert manual HTML/PDF downloads into Markdown files."""
    try:
        ensure_paths(INPUT_DIR, OUTPUT_DIR)
        files = discover_files(INPUT_DIR)
    except (FileNotFoundError, OSError) as error:
        print(f"Initialization failed: {error}")
        return 1

    processed_count = 0
    success_count = 0
    failed_count = 0
    skipped_count = 0

    for file_path in files:
        processed_count += 1
        if file_path.suffix.lower() not in SUPPORTED_SUFFIXES:
            skipped_count += 1
            continue

        try:
            markdown_text = convert_file_to_markdown(file_path)
            output_path = OUTPUT_DIR / f"{file_path.stem}.md"
            write_markdown(output_path, markdown_text)
            success_count += 1
        except (OSError, ValueError, PdfReadError) as error:
            failed_count += 1
            print(f"Failed: {file_path.name}; Reason: {error}")

    print(
        f"Processed: {processed_count}; "
        f"Success: {success_count}; "
        f"Failed: {failed_count}; "
        f"Skipped: {skipped_count}; "
        f"Output directory: {OUTPUT_DIR}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
