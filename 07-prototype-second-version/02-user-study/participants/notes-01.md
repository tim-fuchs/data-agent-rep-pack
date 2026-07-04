# User Study - Participant 01

## Demographics

What is your job position?

- Data scientist (with physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code, RAY)?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- RAY
- Mistral (online version)

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- Yes, own use case: analyzing AGIPD data for SPB instrument

## RAG Interaction (via Grounded Docs UI)

- Participant added [EXtra docs](https://extra.readthedocs.io/en/latest/).
- Q (EXtra-data): **What options to open a run are available for open_run?**
- Q (Extra-data): **How to compute the summed intensity of all AGIPD datasets in a run in SPB?**

## Code Generation/Explanation/Improvement (via AI agent)

- Q: **I am a new user at European XFEL. I am taking part in an experiment at SPB endstation. How to compute the summed intensity of all AGIPD datasets in a run in SPB?**
- A:
  - First version of code: okayish. The agent did not know about Pasha library of European XFEL at first. Used the more generic Pool library instead.
  - Second version: Looked better. Did not work though.
  - Third version: Agent fixed the bug. Solutions worked.

Further observations:

- UX bug:
  - Ask mode was good. Plan+Code modes took a lot of time. Participant could have just copy-pasted the solutions from the Ask agent.
  - Plan agent asked if it should implement code now (Yes/No/Else answer options). Participants clicked Yes. However, tool did not switch to Code mode, and asked the same question over and over again. Participant finally sent a new message to Code agent to start the implementation.
- Flaw in agent workflow: Agent requested to create git environment (and created it). Afterward, it did not request to commit the changes (although instructed in AGENTS.md). Hence, user could not check the diffs between v1, 2, and 3.

## Reporting

Impression of the feature and report structure:

- Good level of detail.
- Agent-own steps at the end were unnecessary (e.g., "Sending the report").

## Verdict

Positive:

- Indexing local data sources: good as this helps to retrieve docs
- Retrieving relevant information: good

Negative:

- Code implementation part (Code agent): took too long

What was unexpected:

- Agent got stuck in loops when it requested to change agent modes.
- High number of Accept/Deny interactions
- Agent created git environment, but did not execute a git commit.

What features do you miss:

- None

## Internal

### Implemented Improvements Before Starting the Session

- None (it was the first session)

### Technical Details

- Timestamp: 2026-04-26-11:00
- Setup:
  - VS Code + Jupyter Lab API + Kilo Code
  - Agent instructions: AGENTS.md + skills directory
  - Note: Agent could not execute code itself as it missed instructions on how to use remote Jupyter kernel.
- LLMs: GPT-5.4-mini

### Improvement Notes

- Add [EXtra library](https://extra.readthedocs.io/en/latest/) to RAG indexing script.
- Update AGENTS.md:
  - Agent should **always** request to git-commit after completing an edit.
  - Regarding reporting the conversation, agent should ignore its own final steps in the summary (i.e., preparing and sending the report).
- Update kilo.jsonc: Preconfigure permissions by auto-accepting read actions for any MCP server tool.
- Be aware of Kilo Code UX bug:
  - Tool cannot switch agent modes when it asks user via a radio-button form if it should switch.
  - Instead, user should ignore the form and send a normal message with the changed mode.
