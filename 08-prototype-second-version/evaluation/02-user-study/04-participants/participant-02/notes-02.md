# Participant 02

Timestamp: 2026-04-22-14:00

## Demographics

What is your job position?
- Data scientist (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- Every day
- Multiple days per week
- Once per week
- -> Less than once per week
- Never

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
- SQS: calibrating data
- SCS: estimating resolution of a detector

## Knowledge Sources

- Added the SQS technique oriented docs
- Asked question about it
- Did not find the correct doc, but a near-duplicate, which was incorrect

## Code Generation/Explanation/Improvement

1. GPT-5.4-mini:
  - Same SQS question
  - Answer basically correct. But answer did not contain the EXtra-data code that would solve the problem.
  - After re-prompting, it took a while to come up with an answer. It reused a GitHub repo from DESY FLASH (instead of EuXFEL). Seems to be (conceptually) correct, but not the EuXFEL version described in the SQS docs.
  - At some point, the agent ran into some rate limit error.
  - Produced code was (apparently) correct but just used numpy and neither of the DESY nor EuXFEL libraries.

2. Qwen3-Next-80B-A3B-Thinking
  - Question about SCS instrument
  - Mixed up SCS with SQS
  - At lot of misunderstanding

3. GPT-5.3-Codex
  - Same SCS question again
  - Solution seem to be conceptually correct, but lacks code for every step
  - After re-prompting to produce code for the steps, it provides a lot of code but does not reuse the SCS Toolbox repo from GitLab.
  - After re-prompting it by steering it towards the SCS toolbox on GitLab, it found a better code solution using the library. BUT it actually used a fork of the repo, not the original repo from SCS.

## Reporting

Impression of the feature and report structure:

- Interesting
- Does not have a plan (yet) on how they would react to the report. It is a bit overwhelming.
- Should be focused on reporting problems.

## Drafting Manuscript

Impression of the feature:

## Verdict

Positive:

- Described each step of the solution, even if it could not find the optimal solution
- Provided citations of original docs

Negative:

- Did not always provide full-code solutions
- Did not always found the correct source (docs, repository)

What was unexpected:

- Many agent modes (Ask, Plan, Code) - a bit confusing

What features do you miss:

- None

## Internal: Improvement Notes

- Add [SQS technique-oriented docs](https://dataanalysis.pages.xfel.eu/techniques-docs/sqs/) to Grounded Docs
- AGENTS.md: Steer it towards important GitLab groups and repository (e.g., SCS Toolbox)
