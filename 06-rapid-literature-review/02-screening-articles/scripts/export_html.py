import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, TextIO
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
INPUT_CSV = DATA_DIR / "sources.csv"
OUTPUT_DIR = DATA_DIR / "html_pdf"
LOG_CSV = DATA_DIR / "log.csv"

REQUEST_TIMEOUT_SECONDS = 20
LOG_HEADER = ["ID", "Timestamp", "Status"]
BOT_DETECTED_STATUS = "bot-detected"

REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

BOT_TEXT_MARKERS = (
    "captcha",
    "verify you are human",
    "are you a robot",
    "unusual traffic",
    "access denied",
    "attention required",
    "bot detection",
)


def row_value(row: dict[str, str], target_key: str) -> str:
    """Fetch a CSV row value by key with BOM-safe case-insensitive matching."""
    normalized_target = target_key.lower()
    for key, value in row.items():
        normalized_key = str(key).lstrip("\ufeff").strip().lower()
        if normalized_key == normalized_target:
            return (value or "").strip()
    return ""


def timestamp_utc() -> str:
    """Return the current timestamp in ISO-8601 UTC format."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def ensure_output_and_log_paths(output_dir: Path, log_csv: Path) -> None:
    """Create output directory and ensure the log file has a valid header."""
    output_dir.mkdir(parents=True, exist_ok=True)

    if not log_csv.exists() or log_csv.stat().st_size == 0:
        with log_csv.open("w", newline="", encoding="utf-8") as log_handle:
            writer = csv.writer(log_handle)
            writer.writerow(LOG_HEADER)
        return

    with log_csv.open(newline="", encoding="utf-8", errors="ignore") as log_handle:
        rows = list(csv.reader(log_handle))

    first_row = rows[0] if rows else []
    normalized_first_row = [
        str(column).lstrip("\ufeff").strip().lower() for column in first_row
    ]
    normalized_header = [column.lower() for column in LOG_HEADER]
    if normalized_first_row == normalized_header:
        raw_log_text = log_csv.read_text(encoding="utf-8", errors="ignore")
        if raw_log_text and not raw_log_text.endswith("\n"):
            log_csv.write_text(f"{raw_log_text}\n", encoding="utf-8")
        return

    with log_csv.open("w", newline="", encoding="utf-8") as log_handle:
        writer = csv.writer(log_handle)
        writer.writerow(LOG_HEADER)
        for index, row in enumerate(rows):
            normalized_row = [
                str(column).lstrip("\ufeff").strip().lower() for column in row
            ]
            if index == 0 and normalized_row[:3] == normalized_header:
                continue

            trimmed_row = list(row[:3])
            while len(trimmed_row) < 3:
                trimmed_row.append("")
            writer.writerow(trimmed_row)


def is_bot_detector_page(response: requests.Response) -> bool:
    """Detect likely anti-bot responses so the current entry can fail fast."""
    if response.status_code in {403, 429}:
        return True

    text_snippet = response.text[:20000].lower()
    if any(marker in text_snippet for marker in BOT_TEXT_MARKERS):
        return True

    if response.status_code >= 400:
        server_header = response.headers.get("Server", "").lower()
        if "cloudflare" in server_header or "cf-ray" in response.headers:
            return True

    return False


def looks_like_html(response: requests.Response, html_text: str) -> bool:
    """Run a lightweight HTML sanity check before persisting output."""
    content_type = response.headers.get("Content-Type", "").lower()
    if "pdf" in content_type:
        return False

    soup = BeautifulSoup(html_text, "html.parser")
    if soup.find("html") is not None:
        return True

    if "text/html" in content_type or "application/xhtml+xml" in content_type:
        return True

    return bool(soup.find())


def request_page(url: str) -> tuple[str, requests.Response | None]:
    """Perform one HTTP GET and return a normalized status plus response."""
    try:
        response = requests.get(
            url,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT_SECONDS,
            allow_redirects=True,
        )
    except requests.RequestException:
        return "failed", None

    if is_bot_detector_page(response):
        return BOT_DETECTED_STATUS, None

    if not response.ok:
        return "failed", None

    return "success", response


def discover_arxiv_html_experimental_url(html_text: str, base_url: str) -> str:
    """Find and resolve the arXiv HTML (experimental) link from a page."""
    soup = BeautifulSoup(html_text, "html.parser")

    for anchor in soup.find_all("a", href=True):
        anchor_text = " ".join(anchor.get_text(" ", strip=True).split()).lower()
        if "html (experimental)" not in anchor_text:
            continue

        href = str(anchor.get("href") or "").strip()
        if not href:
            continue

        candidate_url = urljoin(base_url, href)
        parsed = urlparse(candidate_url)
        if parsed.scheme.lower() in {"http", "https"}:
            return candidate_url

    return ""


def resolve_arxiv_source_url(url: str) -> tuple[str, str, str]:
    """Resolve final arXiv fetch URL via HTML (experimental), if available."""
    status, response = request_page(url)
    if status != "success" or response is None:
        return status, url, ""

    html_text = response.text
    if not html_text.strip():
        return "failed", url, ""

    if not looks_like_html(response, html_text):
        return "failed", url, ""

    html_experimental_url = discover_arxiv_html_experimental_url(
        html_text, response.url
    )
    if html_experimental_url:
        return "success", html_experimental_url, ""

    return "success", response.url, html_text


def is_arxiv_related_url(url: str) -> bool:
    """Return True when the source URL is arXiv-related."""
    return "arxiv" in url.lower()


def fetch_html(url: str) -> tuple[str, str]:
    """Fetch a URL and return a status plus HTML text if successful."""
    status, response = request_page(url)
    if status != "success" or response is None:
        return status, ""

    html_text = response.text
    if not html_text.strip():
        return "failed", ""

    if not looks_like_html(response, html_text):
        return "failed", ""

    return "success", html_text


def validate_article_id(article_id: str) -> bool:
    """Validate article IDs used as output filenames."""
    if not article_id:
        return False
    if "/" in article_id or "\\" in article_id:
        return False
    return True


def append_log_row(
    writer: Any,
    log_handle: TextIO,
    article_id: str,
    status: str,
) -> None:
    """Append one attempt row to the log and flush immediately."""
    writer.writerow([article_id, timestamp_utc(), status])
    log_handle.flush()


def main() -> int:
    """Export HTML files from source URLs and log all attempt statuses."""
    if not INPUT_CSV.exists() or not INPUT_CSV.is_file():
        print(f"Required input file not found: {INPUT_CSV}")
        return 1

    try:
        ensure_output_and_log_paths(OUTPUT_DIR, LOG_CSV)
    except OSError as error:
        print(f"Unable to initialize output/log paths: {error}")
        return 1

    processed_count = 0
    success_count = 0
    failed_count = 0
    bot_detected_count = 0
    invalid_count = 0

    try:
        with INPUT_CSV.open(
            newline="", encoding="utf-8", errors="ignore"
        ) as source_handle, LOG_CSV.open(
            "a", newline="", encoding="utf-8"
        ) as log_handle:
            reader = csv.DictReader(source_handle)
            log_writer = csv.writer(log_handle)

            for row_index, row in enumerate(reader, start=2):
                processed_count += 1

                article_id = row_value(row, "ID")
                link = row_value(row, "Link")
                if not validate_article_id(article_id) or not link:
                    invalid_count += 1
                    fallback_id = article_id or f"row-{row_index}"
                    append_log_row(log_writer, log_handle, fallback_id, "invalid")
                    continue

                prefetched_html = ""
                if is_arxiv_related_url(link):
                    resolver_status, request_url, prefetched_html = (
                        resolve_arxiv_source_url(link)
                    )
                    if resolver_status == BOT_DETECTED_STATUS:
                        bot_detected_count += 1
                        append_log_row(
                            log_writer,
                            log_handle,
                            article_id,
                            BOT_DETECTED_STATUS,
                        )
                        continue
                    if resolver_status != "success":
                        failed_count += 1
                        append_log_row(log_writer, log_handle, article_id, "failed")
                        continue
                else:
                    request_url = link

                if prefetched_html:
                    status = "success"
                    html_text = prefetched_html
                else:
                    status, html_text = fetch_html(request_url)

                if status == "success":
                    output_path = OUTPUT_DIR / f"{article_id}.html"
                    output_path.write_text(html_text, encoding="utf-8", errors="ignore")
                    success_count += 1
                elif status == BOT_DETECTED_STATUS:
                    bot_detected_count += 1
                else:
                    failed_count += 1

                append_log_row(log_writer, log_handle, article_id, status)
    except OSError as error:
        print(f"File processing failed: {error}")
        return 1

    print(
        f"Processed: {processed_count}; "
        f"Success: {success_count}; "
        f"Failed: {failed_count}; "
        f"Bot-detected: {bot_detected_count}; "
        f"Invalid: {invalid_count}; "
        f"Output directory: {OUTPUT_DIR}; "
        f"Log file: {LOG_CSV}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
