# Participant 02

Timestamp: 2026-04-22-14:00

## Demographics

What is your job position?
- Data scientist (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- Every day
- Multiple days per week
- Once per week
- Less than once per week
- -> Never

With what AI assistants have you worked before?

- RAY (just trying)

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- -> Every day
- Multiple days per week
- Once per week
- Less than once per week
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?
- SQS: Calibrating data

## Knowledge Sources

- Added the SQS technique oriented docs
- Asked question about it

## Code Generation/Explanation/Improvement

1. GPT-5.4-mini:
  - Same SQS question
  - Answer basically correct. But answer does not contain the EXtra-data code that would solve the problem.
  - After re-prompting, it took a while to come up with an answer. It reused a GitHub repo from DESY (instead of EuXFEL). Seems to be (conceptually) correct, but not the EuXFEL version described in the SQS docs.
  - At some point, the agent ran into some rate limit error

2. Qwen3-Next-80B-A3B-Thinking
  - Question about SCS instrument
  - Mixed up SCS with SQS
  - At lot of misunderstanding

3. GPT-5.3-Codex
  - Same SCS question again
  - Solution seem to be conceptually correct, but lacks code for every step
  - After re-prompting to produce code for the steps, it provides a lot of code but does not reuse the SCS repos from GitLab. 
  - After re-prompting it by steering it towards the SCS toolbox on GitLab, it found a better code solution using the library. Still, a bit too much code.

## Reporting

Impression of the feature and report structure:
- Interesting
- Does not have a plan (yet) on how they would react to the report. It is a bit overwhelming.
- Should be focused on reporting problems.

## Drafting Manuscript

Impression of the feature:

## Verdict

Positive:

Negative:

What was unexpected:

What features do you miss:

## Internal: Improvement Notes

- Added SQS technique-oriented docs to Grounded Docs
- AGENTS.md: Steer it towards important GitLab groups and repository (e.g., SCS Toolbox)