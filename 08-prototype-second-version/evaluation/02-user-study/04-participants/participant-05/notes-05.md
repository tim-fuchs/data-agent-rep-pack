# Participant 05

## Demographics

What is your job position?

-

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- Every day
- Multiple days per week
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

-

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- Every day
- Multiple days per week
- Once per week
- Less than once per week
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

-

## RAG Interaction (via Grounded Docs UI)

-

## Code Generation/Explanation/Improvement (via AI agent)

What was the plan:

-

What were the results:

-

Further observations:

-

## Reporting

Impression of the feature and report structure:

-

## Drafting Manuscript

Impression of the feature:

-

## Verdict

Positive:

-

Negative:

-

What was unexpected:

-

What features do you miss:

-

## Internal

### Implemented Improvements Before Starting the Session

- Kilo Code read permissions: Previous user auto-permitted many read actions. We kept them.
- AGENTS.md:
  - Capitalized "ALWAYS" in the initial instruction that it should always follow the subsequent instructions.
  - Edit to "Work with up-to-date information":
  
    ```bash
    [...]
    6. Use your internal knowledge.
    - If you use your internal knowledge, use `webfetch` to retrieve related sources that you can cite in your response.
    ```

### Technical Details

- Timestamp: 2026-MM-DD-TT:00
- Setup:
  - VS Code + remote kernel via SSH to Maxwell Jupyter Lab + Kilo Code
  - Note: Agent could not execute code itself as it is outside the SSH environment and did not have access to the kernel.
- LLMs: GPT-5.3-Codex

### Improvement Notes

-
