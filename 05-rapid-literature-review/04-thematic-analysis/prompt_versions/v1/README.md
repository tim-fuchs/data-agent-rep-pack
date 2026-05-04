# Notes for Version 1

- Prompts only created for analyze_relevance and analyze_requirements
- Initial, non-optimized prompts
- Results only obtained from OpenAI

## analyze_relevance

```python
SYSTEM_PROMPT = (
    "Return only a valid JSON object with keys "
    "'relevance_score' and 'justification'."
)

USER_PROMPT = (
    "You are helping with a rapid literature review.\n"
    "Evaluate how relevant the article is to the research question.\n"
    "Return ONLY a valid JSON object with these keys:\n"
    "- relevance_score: number between 0 and 1\n"
    "- justification: concise explanation (1-2 sentences)\n\n"
    "Research question:\n"
    "What are functional and non-functional requirements for the agentic AI systems "
    "that support data scientists and natural scientists during data analysis?\n"
)
```

## analyze_requirements

```python
SYSTEM_PROMPT = (
    "Return only a valid JSON object with key 'requirements'. "
    "Each item must include requirement_type, requirement, and exact_text_quote."
)

USER_PROMPT = (
    "You are helping with a literature review.\n"
    "Extract only requirements grounded in the article text.\n"
    "Extract only requirements that adhere to the research question.\n"
    "Return ONLY a valid JSON object with this schema:\n"
    "{\n"
    '  "requirements": [\n'
    "    {\n"
    '      "requirement_type": "functional or non-functional",\n'
    '      "requirement": "concise requirement statement",\n'
    '      "exact_text_quote": "verbatim quote from article evidence"\n'
    "    }\n"
    "  ]\n"
    "}\n\n"
    "Rules:\n"
    "- requirement_type must be either functional or non-functional.\n"
    "- exact_text_quote must come from the article text.\n"
    "- Skip unclear claims not supported by explicit evidence.\n"
    '- If no requirements are found, return {"requirements": []}.\n\n'
    "Research question:\n"
    "What are functional and non-functional requirements for the agentic AI systems "
    "that support data scientists and natural scientists in writing source code "
    "for data analysis?\n"
)
```
