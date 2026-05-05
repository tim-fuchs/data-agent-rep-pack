from concurrent.futures import ThreadPoolExecutor, as_completed

from reusables import (
    INPUT_DIR,
    OUTPUT_DIR,
    output_file_for_analyzer,
    ensure_paths,
    discover_markdown_files,
    read_article_text,
    build_user_prompt,
    call_analyzer,
    load_settings,
    parse_model_json,
    reset_results_csv,
    append_results_csv,
    reduce_whitespace,
)


CSV_HEADERS = ["article_ID", "requirement_type", "requirement", "exact_text_quote"]
ALLOWED_REQUIREMENT_TYPES = {"functional", "non-functional"}
SYSTEM_PROMPT = (
    "Return only a valid JSON object with key 'requirements'. "
    "Each item must include requirement_type, requirement, and exact_text_quote."
)
USER_PROMPT = (
    "You are assisting with a systematic literature review.\n"
    "Extract requirements that are grounded in the provided article text and that clearly support the target system.\n\n"
    "Target system:\n"
    "Agentic AI system that support data scientists and natural scientists in writing source code for data analysis.\n\n"
    "Classification rules for requirement types:\n"
    "- functional requirement: describes a capability or behavior that a system must satisfy\n"
    "- non-functional requirement: describes quality attributes or constraints that a system must satisfy\n\n"
    "Transferability rules:\n"
    "- Only extract requirements applicable to the target system.\n"
    "- If a requirement is domain-specific, generalize it while preserving its original meaning.\n"
    "- Do not introduce new assumptions. If transferability is unclear, exclude the requirement.\n\n"
    "Extraction rules:\n"
    "- Use only information grounded in the text.\n"
    "- Each requirement must be supported by one exact, verbatim, contiguous quote.\n"
    "- Do not paraphrase or merge multiple quotes.\n"
    "- Avoid duplicates, overlaps, or redundant requirements.\n"
    "- Prefer the most specific formulation.\n\n"
    "Requirement formulation:\n"
    "- Write one clear, self-contained sentence per requirement.\n"
    "- Use neutral phrasing (e.g., 'The system shall...').\n"
    "- Avoid vague terms unless explicitly supported by the quote.\n\n"
    "Output format:\n"
    "Return ONLY a valid JSON object using this schema:\n"
    "{\n"
    '  "requirements": [\n'
    "    {\n"
    '      "requirement_type": "functional | non-functional",\n'
    '      "requirement": "single clear sentence",\n'
    '      "exact_text_quote": "verbatim quote from the article text"\n'
    "    }\n"
    "  ]\n"
    "}\n\n"
    "Validation:\n"
    "- Every requirement is supported by its quote\n"
    "- Quotes are verbatim and contiguous\n"
    "- No duplicates or overlaps\n"
    "- All requirements fit the target context\n"
    "- JSON is valid\n\n"
    'If no requirements are found, return: {"requirements": []}.\n'
)

OUTPUT_PREFIX = "requirements"


def normalize_requirement_type(raw_type: str) -> str:
    """Normalize requirement type values to supported labels."""
    normalized = raw_type.strip().lower()
    alias_map = {
        "functional": "functional",
        "functionality": "functional",
        "non-functional": "non-functional",
        "non functional": "non-functional",
        "nonfunctional": "non-functional",
    }
    normalized = alias_map.get(normalized, normalized)
    if normalized not in ALLOWED_REQUIREMENT_TYPES:
        raise ValueError(f"Unsupported requirement_type: {raw_type}")
    return normalized


def parse_requirements(raw_text: str) -> list[dict[str, str]]:
    """Extract requirement rows from model output."""
    raw_requirements = parse_model_json(raw_text).get("requirements", [])

    if not isinstance(raw_requirements, list):
        raise ValueError("Model output field 'requirements' must be a list")

    rows: list[dict[str, str]] = []
    for item in raw_requirements:
        if not isinstance(item, dict):
            continue

        raw_type = str(item.get("requirement_type", "")).strip()
        requirement = reduce_whitespace(str(item.get("requirement", "")))
        quote = reduce_whitespace(str(item.get("exact_text_quote", "")))

        if not raw_type or not requirement or not quote:
            continue

        try:
            requirement_type = normalize_requirement_type(raw_type)
        except ValueError:
            continue

        rows.append(
            {
                "requirement_type": requirement_type,
                "requirement": requirement,
                "exact_text_quote": quote,
            }
        )

    return rows


def main() -> int:
    """Extract functional and non-functional requirements from articles."""
    try:
        ensure_paths(INPUT_DIR, OUTPUT_DIR / "requirements_openai.csv")
        settings = load_settings()
        files = discover_markdown_files(INPUT_DIR)
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Initialization failed: {error}")
        return 1

    if not files:
        print(f"Initialization failed: No markdown files found in {INPUT_DIR}")
        return 1

    analyzers = settings.analyzers
    processed_count = 0
    article_skipped_count = 0
    analyzer_stats = {
        analyzer: {"success": 0, "failed": 0, "no_requirements": 0, "requirements": 0}
        for analyzer in analyzers
    }
    output_files = {
        analyzer: output_file_for_analyzer(OUTPUT_PREFIX, analyzer)
        for analyzer in analyzers
    }

    for analyzer in analyzers:
        try:
            reset_results_csv(output_files[analyzer], CSV_HEADERS)
        except OSError as error:
            print(f"Output initialization failed for analyzer '{analyzer}': {error}")
            return 1

    for file_path in files:
        processed_count += 1
        article_id = file_path.stem

        try:
            article_text = read_article_text(file_path)
        except (OSError, ValueError) as error:
            article_skipped_count += 1
            print(f"Skipped: {file_path.name}; Reason: {error}")
            continue

        user_prompt = build_user_prompt(USER_PROMPT, article_id, article_text)
        with ThreadPoolExecutor(max_workers=len(analyzers)) as executor:
            future_to_analyzer = {
                executor.submit(
                    call_analyzer,
                    settings,
                    analyzer,
                    SYSTEM_PROMPT,
                    user_prompt,
                ): analyzer
                for analyzer in analyzers
            }

            for future in as_completed(future_to_analyzer):
                analyzer = future_to_analyzer[future]

                try:
                    raw_response = future.result()
                    article_rows = parse_requirements(raw_response)

                    rows_to_append = [
                        {
                            "article_ID": article_id,
                            "requirement_type": row["requirement_type"],
                            "requirement": row["requirement"],
                            "exact_text_quote": row["exact_text_quote"],
                        }
                        for row in article_rows
                    ]

                    try:
                        append_results_csv(
                            output_files[analyzer],
                            CSV_HEADERS,
                            rows_to_append,
                        )
                    except OSError as error:
                        print(f"Output write failed for analyzer '{analyzer}': {error}")
                        return 1

                    analyzer_stats[analyzer]["requirements"] += len(article_rows)
                    analyzer_stats[analyzer]["success"] += 1

                    if not article_rows:
                        analyzer_stats[analyzer]["no_requirements"] += 1
                        print(
                            f"Skipped: {file_path.name}; Analyzer: {analyzer}; "
                            "Reason: No requirements extracted"
                        )
                except (OSError, RuntimeError, ValueError) as error:
                    analyzer_stats[analyzer]["failed"] += 1
                    print(
                        f"Failed: {file_path.name}; Analyzer: {analyzer}; "
                        f"Reason: {error}"
                    )

    print(
        f"Processed: {processed_count}; "
        f"Article skipped: {article_skipped_count}; "
        f"Analyzers: {', '.join(analyzers)}"
    )
    for analyzer in analyzers:
        print(
            f"Analyzer: {analyzer}; "
            f"Success: {analyzer_stats[analyzer]['success']}; "
            f"Failed: {analyzer_stats[analyzer]['failed']}; "
            f"No requirements: {analyzer_stats[analyzer]['no_requirements']}; "
            f"Requirements: {analyzer_stats[analyzer]['requirements']}; "
            f"Output file: {output_file_for_analyzer(OUTPUT_PREFIX, analyzer)}"
        )

    has_failure = any(analyzer_stats[analyzer]["failed"] > 0 for analyzer in analyzers)
    return 0 if not has_failure else 1


if __name__ == "__main__":
    raise SystemExit(main())
