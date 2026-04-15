import json
from collections.abc import Iterator
from difflib import SequenceMatcher
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


INPUT_FILE = OUTPUT_DIR / "requirements_combined.csv"
OUTPUT_FILE = OUTPUT_DIR / "synthesis_thematically_final.csv"
INTERMEDIATE_FILE = OUTPUT_DIR / "synthesis_thematically_initial.csv"

REQUIRED_COLUMNS = [
    "article_ID",
    "requirement_type",
    "requirement",
    "exact_text_quote",
]
OUTPUT_COLUMNS = [
    "article_ID",
    "requirement_type",
    "initial_theme",
    "final_theme",
    "requirement",
    "exact_text_quote",
]

INITIAL_THEME_CHUNK_SIZE = 30
NEAR_DUPLICATE_QUOTE_SIMILARITY_THRESHOLD = 0.92
MIN_NEAR_DUPLICATE_QUOTE_LENGTH = 24

THEME_HINTS: dict[str, list[str]] = {
    "functional": [
        "user interaction",
        "business logic",
        "system behavior",
        "data processing",
        "integration",
        "reporting",
        "administration",
    ],
    "non-functional": [
        "performance",
        "scalability",
        "availability",
        "reliability",
        "security",
        "usability",
        "maintainability",
        "portability",
        "compatibility",
        "compliance",
        "internationalization",
        "safety",
    ],
}

INITIAL_THEME_SYSTEM_PROMPT = (
    "Return only a valid JSON object with key 'items'. "
    "Each item must include row_id and initial_theme."
)
CONSOLIDATION_SYSTEM_PROMPT = (
    "Return only a valid JSON object with key 'items'. "
    "Each item must include initial_theme and theme."
)
INITIAL_THEME_USER_PROMPT = (
    "You are assisting with thematic analysis for a systematic literature review.\n"
    "Assign one concise initial theme to each requirement row.\n\n"
    "Requirement type: {requirement_type}\n"
    "Theme naming guidance:\n"
    "- Preferred hint set: {hint_set}\n"
    "- You may use a precise out-of-list theme when it is clearly better supported by the text.\n"
    "- Keep each theme short (2-5 words), specific, and reusable.\n"
    "- Do not include explanations.\n\n"
    "Output rules:\n"
    "- Return ONLY one JSON object in this format:\n"
    "{{\n"
    '  "items": [\n'
    "    {{\n"
    '      "row_id": 1,\n'
    '      "initial_theme": "theme label"\n'
    "    }}\n"
    "  ]\n"
    "}}\n"
    "- Include every row_id exactly once.\n"
    "- Preserve row_id values exactly.\n\n"
    "Rows JSON:\n{rows_json}"
)
CONSOLIDATION_USER_PROMPT = (
    "You are assisting with thematic synthesis for a systematic literature review.\n"
    "Consolidate similar initial themes into reusable final themes with minimal overlap.\n\n"
    "Requirement type: {requirement_type}\n"
    "Theme naming guidance:\n"
    "- Preferred hint set: {hint_set}\n"
    "- Use hint-set names where suitable.\n"
    "- If a hint-set name is not suitable, use a clearer final theme.\n"
    "- Final themes must be mutually distinct.\n"
    "- Keep final themes concise and reusable across studies.\n\n"
    "Output rules:\n"
    "- Return ONLY one valid JSON object in this format:\n"
    "{{\n"
    '  "items": [\n'
    "    {{\n"
    '      "initial_theme": "source theme",\n'
    '      "theme": "consolidated theme"\n'
    "    }}\n"
    "  ]\n"
    "}}\n"
    "- Omitting or merging any initial_theme is not allowed. Each initial_theme must appear exactly once in the output.\n"
    "- Preserve initial_theme labels exactly as provided.\n\n"
    "Initial themes JSON:\n{initial_themes_json}"
)


def chunk_dataframe(dataframe: pd.DataFrame, chunk_size: int) -> Iterator[pd.DataFrame]:
    """Yield fixed-size slices of a dataframe."""
    for start in range(0, len(dataframe), chunk_size):
        yield cast(pd.DataFrame, dataframe.iloc[start : start + chunk_size])


def hint_text_for_requirement_type(requirement_type: str) -> str:
    """Return hint text for one requirement type."""
    hints = THEME_HINTS.get(requirement_type.casefold(), [])
    if not hints:
        return "No predefined hint list for this requirement type."
    return ", ".join(hints)


def load_requirements_dataframe(input_file: Path) -> tuple[pd.DataFrame, int]:
    """Load and validate requirements input CSV for thematic synthesis."""
    if not input_file.exists() or not input_file.is_file():
        raise FileNotFoundError(f"Required input file not found: {input_file}")

    try:
        dataframe = pd.read_csv(input_file, dtype=str, keep_default_na=False)
    except (OSError, pd.errors.ParserError) as error:
        raise ValueError(f"Failed reading input CSV: {error}") from error

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in dataframe]
    if missing_columns:
        raise ValueError(
            "Input CSV is missing required column(s): " f"{', '.join(missing_columns)}"
        )

    dataframe = dataframe[REQUIRED_COLUMNS].copy()
    for column in REQUIRED_COLUMNS:
        dataframe[column] = dataframe[column].map(lambda value: str(value).strip())

    valid_rows_mask = (
        dataframe["article_ID"].astype(bool)
        & dataframe["requirement_type"].astype(bool)
        & dataframe["requirement"].astype(bool)
    )
    skipped_rows = int((~valid_rows_mask).sum())

    dataframe = dataframe.loc[valid_rows_mask].copy()
    if dataframe.empty:
        raise ValueError(
            "Input CSV does not contain any usable rows with "
            "article_ID, requirement_type, and requirement"
        )

    dataframe.insert(0, "row_id", range(1, len(dataframe) + 1))
    return dataframe, skipped_rows


def normalize_quote_for_similarity(value: str) -> str:
    """Normalize quote text for duplicate and near-duplicate detection."""
    normalized = reduce_whitespace(value).casefold()
    return "".join(
        character
        for character in normalized
        if character.isalnum() or character.isspace()
    )


def quote_is_duplicate_or_near_duplicate(left_quote: str, right_quote: str) -> bool:
    """Check if two quotes are duplicates or near-duplicates."""
    if not left_quote or not right_quote:
        return False

    if left_quote == right_quote:
        return True

    minimum_length = min(len(left_quote), len(right_quote))
    if minimum_length < MIN_NEAR_DUPLICATE_QUOTE_LENGTH:
        return False

    if left_quote in right_quote or right_quote in left_quote:
        return True

    similarity = SequenceMatcher(None, left_quote, right_quote).ratio()
    return similarity >= NEAR_DUPLICATE_QUOTE_SIMILARITY_THRESHOLD


def build_duplicate_group_lookup(dataframe: pd.DataFrame) -> tuple[dict[int, int], int]:
    """Build row_id mapping and count detected duplicate/near-duplicate pairs."""
    parent: dict[int, int] = {
        int(str(row_id)): int(str(row_id)) for row_id in dataframe["row_id"].tolist()
    }
    detected_duplicate_pairs = 0

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(left_node: int, right_node: int) -> None:
        left_root = find(left_node)
        right_root = find(right_node)
        if left_root == right_root:
            return
        if left_root < right_root:
            parent[right_root] = left_root
        else:
            parent[left_root] = right_root

    grouped_by_article = dataframe.groupby("article_ID", sort=False)
    for _, article_group in grouped_by_article:
        records = cast(list[dict[str, Any]], article_group.to_dict(orient="records"))
        normalized_records = [
            (
                int(str(record["row_id"])),
                normalize_quote_for_similarity(str(record.get("exact_text_quote", ""))),
            )
            for record in records
        ]

        for index, (left_row_id, left_quote) in enumerate(normalized_records):
            for right_row_id, right_quote in normalized_records[index + 1 :]:
                if quote_is_duplicate_or_near_duplicate(left_quote, right_quote):
                    detected_duplicate_pairs += 1
                    union(left_row_id, right_row_id)

    return {row_id: find(row_id) for row_id in parent}, detected_duplicate_pairs


def build_initial_theme_user_prompt(
    requirement_type: str,
    chunk: pd.DataFrame,
) -> str:
    """Build a prompt that assigns one initial theme to each row in a chunk."""
    records = cast(list[dict[str, Any]], chunk.to_dict(orient="records"))
    payload = [
        {
            "row_id": int(str(record["row_id"]).strip()),
            "requirement": reduce_whitespace(str(record["requirement"])),
            "exact_text_quote": reduce_whitespace(str(record["exact_text_quote"])),
        }
        for record in records
    ]

    return INITIAL_THEME_USER_PROMPT.format(
        requirement_type=requirement_type,
        hint_set=hint_text_for_requirement_type(requirement_type),
        rows_json=json.dumps(payload, ensure_ascii=True),
    )


def build_consolidation_user_prompt(
    requirement_type: str,
    initial_themes: list[str],
) -> str:
    """Build a prompt that consolidates similar initial themes."""
    return CONSOLIDATION_USER_PROMPT.format(
        requirement_type=requirement_type,
        hint_set=hint_text_for_requirement_type(requirement_type),
        initial_themes_json=json.dumps(initial_themes, ensure_ascii=True),
    )


def parse_initial_theme_items(raw_text: str) -> dict[int, str]:
    """Parse initial-theme assignments from model JSON output."""
    parsed = parse_model_json(raw_text)
    items = parsed.get("items", [])
    if not isinstance(items, list):
        raise ValueError("Model output field 'items' must be a list")

    row_to_theme: dict[int, str] = {}
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Each item in model output must be an object")

        row_id_raw = str(item.get("row_id", "")).strip()
        if not row_id_raw.isdigit():
            raise ValueError(f"Invalid row_id in model output: {row_id_raw}")

        row_id = int(row_id_raw)
        initial_theme = reduce_whitespace(str(item.get("initial_theme", ""))).lower()
        if not initial_theme:
            raise ValueError(f"Missing initial_theme for row_id {row_id}")

        if row_id in row_to_theme:
            raise ValueError(f"Duplicate row_id in model output: {row_id}")

        row_to_theme[row_id] = initial_theme

    return row_to_theme


def build_casefold_lookup(values: list[str]) -> dict[str, str]:
    """Build a case-insensitive lookup and reject ambiguous keys."""
    lookup: dict[str, str] = {}
    for value in values:
        key = value.casefold()
        existing = lookup.get(key)
        if existing is not None and existing != value:
            raise ValueError(
                "Theme labels differ only by letter case and cannot be matched "
                f"reliably: '{existing}' and '{value}'"
            )
        lookup[key] = value
    return lookup


def parse_consolidation_items(
    raw_text: str, expected_themes: list[str]
) -> dict[str, str]:
    """Parse and align consolidation mappings from model output."""
    parsed = parse_model_json(raw_text)
    items = parsed.get("items", [])
    if not isinstance(items, list):
        raise ValueError("Model output field 'items' must be a list")

    expected_lookup = build_casefold_lookup(expected_themes)
    consolidated_map: dict[str, str] = {}

    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Each item in model output must be an object")

        initial_theme_raw = reduce_whitespace(str(item.get("initial_theme", "")))
        final_theme = reduce_whitespace(str(item.get("theme", "")))

        if not initial_theme_raw:
            raise ValueError("Missing initial_theme in consolidation output")
        if not final_theme:
            raise ValueError(
                f"Missing theme in consolidation output for '{initial_theme_raw}'"
            )

        matched_theme = expected_lookup.get(initial_theme_raw.casefold())
        if matched_theme is None:
            raise ValueError(
                "Consolidation output references unknown initial_theme: "
                f"{initial_theme_raw}"
            )

        if matched_theme in consolidated_map:
            raise ValueError(
                "Duplicate initial_theme in consolidation output: " f"{matched_theme}"
            )

        consolidated_map[matched_theme] = final_theme

    return consolidated_map


def assign_initial_themes(
    provider: ProviderConfig,
    requirement_type: str,
    group: pd.DataFrame,
) -> dict[int, str]:
    """Assign initial themes to all rows in one requirement-type group."""
    assignments: dict[int, str] = {}

    representative_rows = (
        group.sort_values(by=["row_id"])
        .drop_duplicates(subset=["duplicate_group_id"], keep="first")
        .copy()
    )

    representative_to_group: dict[int, int] = {
        int(str(row_id)): int(str(group_id))
        for row_id, group_id in zip(
            representative_rows["row_id"].tolist(),
            representative_rows["duplicate_group_id"].tolist(),
        )
    }

    group_to_representative_theme: dict[int, str] = {}

    for chunk in chunk_dataframe(representative_rows, INITIAL_THEME_CHUNK_SIZE):
        chunk_frame = cast(pd.DataFrame, chunk)
        user_prompt = build_initial_theme_user_prompt(requirement_type, chunk_frame)
        raw_response = call_chat_completions(
            provider,
            INITIAL_THEME_SYSTEM_PROMPT,
            user_prompt,
        )

        chunk_assignments = parse_initial_theme_items(raw_response)
        expected_row_ids = {
            int(str(row_id).strip()) for row_id in chunk_frame["row_id"].tolist()
        }
        received_row_ids = set(chunk_assignments)

        if received_row_ids != expected_row_ids:
            missing = sorted(expected_row_ids - received_row_ids)
            extra = sorted(received_row_ids - expected_row_ids)
            raise ValueError(
                "Initial-theme response row mismatch; "
                f"missing row_id(s): {missing}; extra row_id(s): {extra}"
            )

        for representative_row_id, initial_theme in chunk_assignments.items():
            duplicate_group_id = representative_to_group[representative_row_id]
            group_to_representative_theme[duplicate_group_id] = initial_theme

    for row_id, duplicate_group_id in zip(
        group["row_id"].tolist(),
        group["duplicate_group_id"].tolist(),
    ):
        normalized_row_id = int(str(row_id).strip())
        normalized_group_id = int(str(duplicate_group_id).strip())
        try:
            assignments[normalized_row_id] = group_to_representative_theme[
                normalized_group_id
            ]
        except KeyError as error:
            raise ValueError(
                "Missing initial theme assignment for duplicate_group_id "
                f"{normalized_group_id}"
            ) from error

    return assignments


def consolidate_themes(
    provider: ProviderConfig,
    requirement_type: str,
    initial_themes: list[str],
) -> dict[str, str]:
    """Consolidate initial themes into reusable low-overlap final themes."""
    if not initial_themes:
        return {}

    if len(initial_themes) == 1:
        only_theme = initial_themes[0]
        return {only_theme: only_theme}

    user_prompt = build_consolidation_user_prompt(requirement_type, initial_themes)
    raw_response = call_chat_completions(
        provider,
        CONSOLIDATION_SYSTEM_PROMPT,
        user_prompt,
    )

    consolidation_map = parse_consolidation_items(raw_response, initial_themes)
    expected = set(initial_themes)
    received = set(consolidation_map)

    if expected != received:
        missing = sorted(expected - received)
        extra = sorted(received - expected)
        raise ValueError(
            "Consolidation response theme mismatch; "
            f"missing initial_theme(s): {missing}; extra initial_theme(s): {extra}"
        )

    return consolidation_map


def sort_output_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Sort output rows by requirement_type, final_theme, and requirement."""
    sorted_dataframe = dataframe.assign(
        _sort_requirement_type=dataframe["requirement_type"].str.casefold(),
        _sort_final_theme=dataframe["final_theme"].str.casefold(),
        _sort_requirement=dataframe["requirement"].str.casefold(),
    ).sort_values(
        by=[
            "_sort_requirement_type",
            "_sort_final_theme",
            "_sort_requirement",
            "article_ID",
        ],
        kind="mergesort",
    )

    return sorted_dataframe.drop(
        columns=["_sort_requirement_type", "_sort_final_theme", "_sort_requirement"]
    )


def main(skip_initial_themes: bool = False) -> int:
    """Synthesize requirement themes through a two-pass LLM workflow, with optional skipping of initial theme assignment."""
    provider = None
    dataframe = None
    skipped_rows = 0
    duplicate_group_lookup = None
    detected_duplicate_pairs = 0
    stats = {}

    if not skip_initial_themes:
        # Step 1: Load requirements and assign initial themes
        try:
            provider = load_synthesis_provider()
            dataframe, skipped_rows = load_requirements_dataframe(INPUT_FILE)
            duplicate_group_lookup, detected_duplicate_pairs = (
                build_duplicate_group_lookup(dataframe)
            )
        except (FileNotFoundError, OSError, ValueError) as error:
            print(f"Initialization failed: {error}")
            return 1

        dataframe["duplicate_group_id"] = dataframe["row_id"].map(
            duplicate_group_lookup
        )
        if dataframe["duplicate_group_id"].isna().any():
            print("Initialization failed: Missing duplicate group assignments")
            return 1

        stats = {
            "rows_read": len(dataframe) + skipped_rows,
            "rows_skipped_missing_required_fields": skipped_rows,
        }

        row_to_initial_theme: dict[int, str] = {}

        try:
            grouped = dataframe.groupby("requirement_type", sort=False)
            for requirement_type, group in grouped:
                requirement_type_text = str(requirement_type).strip()
                group_frame = (
                    group.to_frame().T
                    if isinstance(group, pd.Series)
                    else pd.DataFrame(group)
                )

                initial_assignments = assign_initial_themes(
                    provider,
                    requirement_type_text,
                    group_frame,
                )

                for row_id, initial_theme in initial_assignments.items():
                    row_to_initial_theme[row_id] = initial_theme
        except (RuntimeError, ValueError) as error:
            print(f"Initial theme assignment failed: {error}")
            return 1

        dataframe["initial_theme"] = dataframe["row_id"].map(row_to_initial_theme)
        dataframe["initial_theme"] = dataframe["initial_theme"].map(reduce_whitespace)

        # Write intermediate file
        try:
            INTERMEDIATE_FILE.parent.mkdir(parents=True, exist_ok=True)
            dataframe.to_csv(INTERMEDIATE_FILE, index=False)
        except OSError as error:
            print(f"Intermediate output write failed: {error}")
            return 1

        print(f"Initial themes written to: {INTERMEDIATE_FILE}")
    else:
        # Step 2: Load from intermediate file
        try:
            dataframe = pd.read_csv(INTERMEDIATE_FILE, dtype=str, keep_default_na=False)
        except (OSError, pd.errors.ParserError) as error:
            print(f"Failed to read intermediate file: {error}")
            return 1
        required_cols = set(
            REQUIRED_COLUMNS + ["row_id", "initial_theme", "requirement_type"]
        )
        missing_cols = required_cols - set(dataframe.columns)
        if missing_cols:
            print(f"Intermediate file missing required columns: {missing_cols}")
            return 1
        dataframe["row_id"] = dataframe["row_id"].astype(int)
        print(f"Loaded initial themes from: {INTERMEDIATE_FILE}")

    # Step 3: Final theme consolidation
    provider = provider or load_synthesis_provider()
    row_to_final_theme: dict[int, str] = {}

    try:
        grouped = dataframe.groupby("requirement_type", sort=False)
        for requirement_type, group in grouped:
            requirement_type_text = str(requirement_type).strip()
            group_frame = (
                group.to_frame().T
                if isinstance(group, pd.Series)
                else pd.DataFrame(group)
            )

            # Use initial_theme column for consolidation
            unique_initial_themes = sorted(
                set(group_frame["initial_theme"].map(reduce_whitespace))
            )
            consolidation_map = consolidate_themes(
                provider,
                requirement_type_text,
                unique_initial_themes,
            )

            for row_id, initial_theme in zip(
                group_frame["row_id"], group_frame["initial_theme"]
            ):
                row_to_final_theme[int(str(row_id).strip())] = consolidation_map[
                    reduce_whitespace(str(initial_theme))
                ]
    except (RuntimeError, ValueError) as error:
        print(f"Final theme consolidation failed: {error}")
        return 1

    dataframe["final_theme"] = dataframe["row_id"].map(row_to_final_theme)
    dataframe["final_theme"] = dataframe["final_theme"].map(reduce_whitespace)

    output_dataframe = pd.DataFrame(dataframe, columns=OUTPUT_COLUMNS).copy()
    output_dataframe = sort_output_dataframe(output_dataframe)

    try:
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        output_dataframe.to_csv(OUTPUT_FILE, index=False)
    except OSError as error:
        print(f"Output write failed: {error}")
        return 1

    if not skip_initial_themes:
        print(f"Rows read: {stats['rows_read']}")
        print(
            "Rows skipped (missing article_ID, requirement_type, or requirement): "
            f"{stats['rows_skipped_missing_required_fields']}"
        )
        print(f"Duplicate pairs detected: {detected_duplicate_pairs}")
    print(f"Rows written: {len(output_dataframe)}")
    print(f"Output file: {OUTPUT_FILE}")

    return 0


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Synthesize requirement themes with optional skipping of initial theme assignment."
    )
    parser.add_argument(
        "--skip-initial-themes",
        action="store_true",
        help="Skip initial theme assignment and start from intermediate file.",
    )
    args = parser.parse_args()
    raise SystemExit(main(skip_initial_themes=args.skip_initial_themes))
