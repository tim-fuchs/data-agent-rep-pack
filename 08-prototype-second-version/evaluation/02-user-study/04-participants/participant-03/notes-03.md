# Participant 03

Timestamp: 2026-04-22-16:00

## Demographics

What is your job position?
- Software engineer / project coordinator

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- Every day
- -> Multiple days per week
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- Gemini
- RAY
- GitHub Copilot (a bit)
- ChatGPT

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- Few days per month

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

## Knowledge Sources

RAG interaction (via Grounded Docs UI):
- Added EXtra-Geom docs
- Question: Example to display geometry of AGIPD-1M detector
- Answer: Correct chunks. But was sensitive to the "-".

RAG interaction (via agent):

GitLab interaction (via agent):

GitHub interaction (via agent):

## Code Generation/Explanation/Improvement

What was the plan:
- Same as before (AGIPD-1M) + second version for LPD detector

What were the results:
- For AGIPD, it entered a placeholder path to a geom file. That is why we did a second version with a LPD geom file available in the workspace.
- Worked! Just a problem with the SSH connection.

## Reporting

Impression of the feature and report structure:
- Positive: Would be helpful. Can be helpful later on (even in months).

## Drafting Manuscript

Impression of the feature:

## Verdict

Positive:
- Got the correct answers for the questions

Negative:
- Permission prompts were a bit annoying.

What was unexpected:

What features do you miss:

## Internal: Improvement Notes

- Permit Read options 
