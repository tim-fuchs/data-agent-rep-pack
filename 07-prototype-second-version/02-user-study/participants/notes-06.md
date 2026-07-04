# Participant 06

## Demographics

What is your job position?

- Group leader (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- OpenAI (API, ChatGPT, Codex)
- Apple Intelligence
- Gemini

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- Every day
- Multiple days per week
- Once per week
- **Less than once per week**
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- Find cosmic muons in some data

## RAG Interaction (via Grounded Docs UI)

- Q (User docs): Are there any dark images or dark data sets in the example data?
- A: RAG could not answer this question.

## Code Generation/Explanation/Improvement (via AI agent)

- Q: Do you have access to the European XFEL example data sets and if so, which?
- A: No, as Kilo Code did not have direct access to Maxwell
- Q: Reuse the proposal in extra.ipynb to check its data sources. AGIPD will be one of them. Create the per-pixel, per memory ...
- A: Wanted to create an internal Python package that could not access extra-data.
- Q: Create a new notebook instead
- A: New notebook. One error (index out of range) because it misunderstood the pulse attribute in the dataset. Error was fixed after a few edits by user and agent.
- Q: Are you displaying dark images?
- A: Agent checked correctly if dark images selected
- Q: Can you create an algorithm to find cosmic muons?
- A: Yes. Created the algorithm.
- Q: Create an interactive overview plot for the candidates you find.
- A: Plot contains an error. Was fixed after user asked agent to fix the error. Interactive plot works. BUT: the data does not contain dark images.

Further observations:

- Agent has not asked about Git environment.
- Agent did not tell the user to re-open the notebook to see the changes it made.
- Agent created too much boilerplate code (model: GTP-5.3-Codex)
- Agent did not prompt the options for sending the report as a form, just as text.

## Reporting

Impression of the feature and report structure:

- Could be useful
- Quite verbose
- Should focus more on the generated data (the algorithm, etc.)
- Less on small fixes

## Verdict

Positive:

- Final output worked

Negative:

- For user who has not worked with AI-assisted coding, the interaction might be complicated.
- Agent created boilerplate code
- Agent did not check by itself if created code contained errors.
- Kilo Code does not display the diff within the chat window, just the numbers of new and deleted lines.

What was unexpected:

- Agent-notebook interaction should be improved (run generated code in the notebook directly; close and re-open the notebook automatically)

What features do you miss:

- Agent should be aware of the example datasets to know which proposals and runs to use for specific requests.

## Internal

### Implemented Improvements Before Starting the Session

- Converted rules in AGENTS.md to Kilo Code-supported rule files in `.kilo/rules`.
- Added European XFEL website and [offline calibration](https://calibration.pages.xfel.eu/pycalibration/) to RAG system.

### Technical Details

- Timestamp: 2026-04-29-11:00
- Setup:
  - VS Code + Jupyter Lab API + Kilo Code
  - Agent instructions: AGENTS.md + skills directory + rules directory
  - Note: Agent could not execute code itself as it missed instructions on how to use remote Jupyter kernel.
- LLMs: GPT-5.3-Codex

### Improvement Notes

- Instruct agent to create code files (e.g., Jupyter notebook) to execute and review the generated code, instead of trying to execute the code within its sandbox.
  - Reason: Within its sandbox, the agent cannot access the remote kernel.
- After the agent made changes to a Jupyter notebook, it should close the file without saving and re-open it to display the changes.
