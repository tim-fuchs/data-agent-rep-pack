# Participant 12

## Demographics

What is your job position?

- Software developer and data scientist (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- Every day
- **Multiple days per week**
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- Codex
- Claude Code
- ChatGPT

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- Every day
- **Multiple days per week**
- Once per week
- Less than once per week
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- SCS Toolbox: Using generated data for further processing (correlation)

## RAG Interaction (via Grounded Docs UI)

- Q (SCS Toolbox): I want to load data with digitizers to correlate it with an XGM. I am curious about which data is loaded when I use toolbox_scs.open(). Can you please walk me through it? Maybe use FastADC (or something similar) for the digitizer and XGM (or SCS SA3).
- A: Provided a chunk that contained relevant webpage

## Code Generation/Explanation/Improvement (via AI agent)

- Q (Ask): I want to load data with digitizers to correlate it with an XGM. I am curious about which data is loaded when I use toolbox_scs.open(). Can you please walk me through it? Maybe use FastADC (or something similar) for the digitizer and XGM (or SCS SA3).
- A: Corrected flaw in the participant's question. Provided mostly relevant and correct information. One hint to an EXtra component was incorrect.
- Q: Request to correct specific flaws in the agent response
- A: Improved the information. Quite verbose though.
- Q: Create a code snippet
- A: Created code
- Q (Code): Generate notebook with that code
- A: Created notebook. Could not test it due to missing toolbox_scs package.
- Q: Install the missing package.
- A: Worked. Notebook looked good overall. We could not fully test all cells due to missing data in the test datasets.

- Further observations:
  - Initial prompt was very detailed. This steered the agent to a good direction.
  - Agent corrected flaw in participant's request.

## Reporting

Impression of the feature and report structure:

- Not tested due to lacking time

## Verdict

Positive:

- Good that agent uses context information
- Retrieves relevant documentation
- Promising prototype

Negative:

- Agent response was quite noisy/vague. Agent should ask more follow-up question to steer the data analysis process.

What was unexpected:

- Nothing

What features do you miss:

- Documentation must become agent-ready.

## Internal

### Implemented Improvements Before Starting the Session

- `AGENTS.md`:
  - Updated `Generate HPC-Optimized Code` section to clarify need for atomic code components
  - Updated `Request User Feedback to Guide and Improve Solutions` section with hardened instructions for asking clarification questions

### Technical Details

- Timestamp: 2026-05-07-11:00
- Setup:
  - VS Code + Jupyter Lab API + Kilo Code
  - Agent instructions: AGENTS.md + skills directory
- LLMs: GPT-5.4

### Improvement Notes

- Agent should ask more questions to clarify the user's analysis goal
