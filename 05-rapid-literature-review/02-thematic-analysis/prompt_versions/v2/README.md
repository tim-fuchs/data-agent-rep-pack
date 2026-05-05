# Notes for Version 2

- Prompts only created for analyze_relevance and analyze_requirements
- Prompts optimized with more structured instructions and examples.
- Results only obtained from OpenAI

## analyze_relevance

```python
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
```

## analyze_requirements

```python
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
```
