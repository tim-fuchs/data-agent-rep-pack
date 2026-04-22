# User Study - Participant 01

Timestamp: 2026-04-26-11:00

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

## Demographics

What is your job position?

- Data scientist (with physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code, RAY)?

- -> Every day
- Multiple days per week
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- RAY
- Mistral (online version)

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- Daily usage

## Knowledge Sources

RAG interaction (via Grounded Docs UI):

- EXtra-data: what options to open a run are available for open_run?
- added EXtra documentation (<https://extra.readthedocs.io/en/latest/>)
- Extra-data: How to compute the summed intensity of all AGIPD datasets in a run in SPB?

RAG interaction (via agent):

- I am a new user at EuXFEL. I am taking part in an experiment at SPB endstation. How to compute the summed intensity of all AGIPD datasets in a run in SPB?

GitLab interaction (via agent):

GitHub interaction (via agent):

## Code Generation/Explanation/Improvement

What was the plan:

- Implement SPB use case above

What were the results:

- We could have just copy+paste the solution from the Ask mode.
- Plan+Code mode took a while.
- Result of first version: Okayish, but agent did not know about Pasha library at first. Used Pool instead
- Result of second version: looked better. Did not work though.
- Agent tried to fix the bug, but could not as participant could not switch from Ask to Code mode at first.
- Agent seemed to fix the bug
- Problem: Initial version was not git-committed. Could not check the diffs between v1 and v2.

## Reporting

Impression of the feature and report structure:

- Details of report were good
- Agent-own steps at the end were unnecessary

## Drafting Manuscript

Impression of the feature:

## Verdict

Positive:

- Finding information: good
- Indexing of local data sources: good as this helps to retrieve the docs

Negative:

- Coding part: took too long

What was unexpected:

- Agent get stuck in loops when in wrong mode
- The amount of Accept/Deny interactions
- Did not do the git commit

What features do you miss:

- None

## Internal: Improvement Notes

- Added docs of EXtra library (read-the-docs website)
- Update AGENTS.md: Always git commit after edit!
- Update kilo.jsonc: Preconfigure permission (auto-accept read actions).
