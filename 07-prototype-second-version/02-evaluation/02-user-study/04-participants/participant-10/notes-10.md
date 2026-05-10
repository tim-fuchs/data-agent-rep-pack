# Participant 10

## Demographics

What is your job position?

- Group manager (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- Every day
- **Multiple days per week**
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- Gemini
- RAY
- ChatGPT

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- Every day
- Multiple days per week
- Once per week
- **Less than once per week**
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- Yes:
  - Calculate intensity for a set of runs via XGM component
  - Proposal API

## RAG Interaction (via Grounded Docs UI)

- EXtra: Proposal
- EXtra: What is the pulse energy

## Code Generation/Explanation/Improvement (via AI agent)

- Q (Ask): How can I get the XFEL pulse energy for proposal 8034
- R: Good instructions, but low-level code. Agent did not provide high-level XGM component code.
- Q: I think there is a simpler (less code) way to get this quantity.
- R: Did not provide the solution
- Q: Steering towards EXtra library and XGM component
- R: Found the high-level solution
- Q (Plan): Can you generate a notebook in which XGM pulse energy for proposal 7000001 run 2, 3, and 4 is read and plotted
- R: Did not share the plan and just asked to implement the solution
- Q (Code): Start implementation
- R: A lot of back and worth until agent created a good solution (used the wrong kernel in the beginning, produced a lot of boilerplate code for defensive coding, user fault: proposal 700001 not available).
- Q: (further coding request for Proposal API)
- R: Good code

Further observations:

- Agent continued to reuse the wrong Python kernel. It should ask the user which kernel it should use instead of assuming a kernel.
- Agent should not focus on defensive coding but on throwing error messages when information is missing.
- Agent tries to read GPFS data within its sandbox. Instead, it should always use Python files or notebooks connected to the Jupyter kernel to read the data.

## Reporting

Impression of the feature and report structure:

- Convenient feature. In general, this can be useful.

## Verdict

Positive:

- I got what I wanted in a notebook

Negative:

- All the MCP calls documented in the session is too much information
- To get to the solution, I needed a lot of prompting and steering
- Defensive coding of the agent is annoying (simple solutions with error messages over long, more robust solutions)
- Too much text. Highlight important notes in the summary.

What was unexpected:

- Close notebook and reopen it again -> Agent should explicitly ask if it should close and reopen the notebook itself
- Many explicit "Accept" button clicks

What features do you miss:

- Nothing

## Internal

### Implemented Improvements Before Starting the Session

- RAG:
  - Updated Maxwell docs
  - Added Slurm docs
- AGENTS.md: Updated the citation section - Agent should check if URLs are still available.

### Technical Details

- Timestamp: 2026-MM-DD-TT:00
- Setup:
  - VS Code + remote kernel via SSH to Maxwell Jupyter Lab + Kilo Code
  - Agent instructions: AGENTS.md + skills directory
- LLMs: GPT-5.4

### Improvement Notes

- Agent must always ask the user which Python environment or Jupyter kernel it should use. It should never just choose one of the environments or kernels.
- Agent must not follow defensive coding with default parameter values. Instead, agent should throw error messages if parameter values are missing.
- Agent must not use its internal environment to read any data from European XFEL. Instead, it must generate code in (temporary) Python or Jupyter notebook files that are connected to a Jupyter kernel to read the data. It should ask which Jupyter kernel it shall pick.
