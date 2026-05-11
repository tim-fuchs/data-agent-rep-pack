# Participant 03

## Demographics

What is your job position?

- Software engineer / project coordinator

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- Every day
- **Multiple days per week**
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- Gemini
- RAY
- GitHub Copilot (a bit)
- ChatGPT

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- Every day
- Multiple days per week
- Once per week
- **Less than once per week**
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- Yes, displaying geometry of AGIPD-1M and LPD detectors.

## RAG Interaction (via Grounded Docs UI)

- Participant added [EXtra-Geom docs](https://extra-geom.readthedocs.io/en/latest/index.html)
- Q (EXtra-geom): **Can you provide an example of how to display the geometry of the AGIPD-1M detector?**
- A: Correct chunks. But order of chunks was sensitive to the "-".

## Code Generation/Explanation/Improvement (via AI agent)

- Q (Code): Same question as before (AGIPD-1M) + second version for LPD detector
- A: For the AGIPD version, it entered a placeholder path to a geom file.
- Q: Since participant brought a geom file for LPD, they requested a second version with a LPD geom file.
- A: Fully correct solution.

Further observations:

- SSH connection sometimes brakes. Eventually, when closing the laptop.

## Reporting

Impression of the feature and report structure:

- Positive: Would be helpful. Can be helpful later on (even in months).

## Verdict

Positive:

- Got the correct answers for the questions

Negative:

- Permission prompts were a bit annoying.

What was unexpected:

- None

What features do you miss:

- None

## Internal

### Implemented Improvements Before Starting the Session

- Kilo Code read permissions: Previous user auto-permitted many read actions. We kept them.
- Added SQS technique-oriented docs to RAG system
- Use 5.3-Codex instead of 5.4-mini

### Technical Details

- Timestamp: 2026-04-22-16:00
- Setup:
  - VS Code + Jupyter Lab API + Kilo Code
  - Agent instructions: AGENTS.md + skills directory
  - Note: Agent could not execute code itself as it missed instructions on how to use remote Jupyter kernel.
- LLMs: GPT-5.3-Codex

### Improvement Notes

- Work on a solution that enables agent to execute code via the remote kernel.
- Permit the agent to conduct all read options (clicking `Accept` is a bit annoying).
- Add [EXtra-Geom docs](https://extra-geom.readthedocs.io/en/latest/index.html) to RAG ingestion script.
- Be aware of a possible connection issue to SSH when closing the laptop.
