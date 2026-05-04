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
)


CSV_HEADERS = ["article_ID", "relevance_score", "justification"]
SYSTEM_PROMPT = (
    "Return only a valid JSON object with keys "
    "'relevance_score' and 'justification'."
)
USER_PROMPT = (
    "You are assisting with a systematic literature review.\n"
    "Judge how relevant the provided article text is to the target system by providing a relevance score.\n\n"
    "Target system:\n"
    "Agentic AI system that support data scientists and natural scientists in writing source code for data analysis.\n\n"
    "Scoring rules:\n"
    "- High score: Directly addresses agentic AI for scientific/data analysis code generation\n"
    "- Medium score: Partially related (e.g., only AI for code generation or only scientific AI)\n"
    "- Low score: Only loosely related (e.g., general AI, unrelated domains, or non-code tools).\n\n"
    "Output format:\n"
    "Return ONLY a valid JSON object with these keys:\n"
    "- relevance_score: number between 0 and 1\n"
    "- justification: string with 1-2 concise sentences explaining the relevance for the target system\n\n"
    "Validation:\n"
    "- Score is between 0 and 1.\n"
    "- Justification refers to the target system.\n"
    "- JSON is valid.\n"
)

OUTPUT_PREFIX = "relevance"


def parse_relevance(raw_text: str) -> tuple[str, str]:
    """Extract relevance score and justification from model output."""
    parsed = parse_model_json(raw_text)

    if "relevance_score" not in parsed:
        raise ValueError("Model output is missing 'relevance_score'")

    try:
        score_value = float(parsed["relevance_score"])
    except (TypeError, ValueError) as error:
        raise ValueError("relevance_score must be numeric") from error

    score_value = max(0.0, min(1.0, score_value))
    score = f"{score_value:.2f}"

    justification = str(parsed.get("justification", "")).strip()
    if not justification:
        justification = "Model did not provide a justification."

    return score, justification


def main() -> int:
    """Analyze article relevance and export CSV results."""
    try:
        ensure_paths(INPUT_DIR, OUTPUT_DIR / "relevance_openai.csv")
        settings = load_settings()
        files = discover_markdown_files(INPUT_DIR)
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Initialization failed: {error}")
        return 1

    analyzers = settings.analyzers
    processed_count = 0
    article_skipped_count = 0
    analyzer_stats = {analyzer: {"success": 0, "failed": 0} for analyzer in analyzers}
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
                    relevance_score, justification = parse_relevance(raw_response)
                    analyzer_stats[analyzer]["success"] += 1
                except (OSError, RuntimeError, ValueError) as error:
                    analyzer_stats[analyzer]["failed"] += 1
                    relevance_score = ""
                    justification = f"ERROR: {error}"
                    print(
                        f"Failed: {file_path.name}; Analyzer: {analyzer}; "
                        f"Reason: {error}"
                    )

                try:
                    append_results_csv(
                        output_files[analyzer],
                        CSV_HEADERS,
                        [
                            {
                                "article_ID": article_id,
                                "relevance_score": relevance_score,
                                "justification": justification,
                            }
                        ],
                    )
                except OSError as error:
                    print(f"Output write failed for analyzer '{analyzer}': {error}")
                    return 1

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
            f"Output file: {output_file_for_analyzer(OUTPUT_PREFIX, analyzer)}"
        )

    has_failure = any(analyzer_stats[analyzer]["failed"] > 0 for analyzer in analyzers)
    return 0 if not has_failure else 1


if __name__ == "__main__":
    raise SystemExit(main())
