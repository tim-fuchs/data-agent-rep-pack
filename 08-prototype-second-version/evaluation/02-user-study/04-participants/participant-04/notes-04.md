# Participant 04

## Demographics

What is your job position?

- Data scientist (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- Every day
- **Multiple days per week**
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- Claude Web
- Mistral Web
- ChatGPT
- RAY

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- Yes, two use cases:
  - Testing a new EXtra component (Scan) and apply it to a motor component.
  - (Time-series problem)

## RAG Interaction (via Grounded Docs UI)

- Question: I want to use extra.components.scan to analyze an extra_data run that has a motor source in it.
- Responses: Required info was part of the first chunk.
- Question: I want to use extra.components.scan to analyze an extra_data run that has a motor source in it. I am interested in the Scann class *not* Scantool.
- Responses: Required info was part of the first chunk.

## Code Generation/Explanation/Improvement (via AI agent)

- **Question:** I want to use extra.components.scan to analyze an extra_data run that has a motor source in it. I am interested in the Scann class *not* Scantool.
- **Response:** was good and in code. However, participant found it concerning that it did not provide additional information about the parameter values it chose as default. It should provide more information about replacing the default values.
- **Question:** Generate a notebook based on this code. Open proposal 700005 run number 4. Look at motor source SXP_LAS_... .
- **Response:**
  - Generate notebook looks reasonable.
  - Unnecessary `run.info` (but the info does not hurt).
  - Could execute the notebook. But ran into a problem because of unavailability of specific motor data in the run.
  - But it should not combine that many commands in one cell. Not more than one "edit" command in one cell.

- **Potential further question (but not asked):** Find runs that include the required motor data.

Further observations:

- Agent did not ask to create a git environment and commit.

## Reporting

Impression of the feature and report structure:

- Local+external report sent.
- Important caviats should be highlighted better.
- Content pretty good.
- Report to myLog "is not bad".

Potential value of a problem report:

- Be careful, as DA members might not want to debug any non-DA problems (connection problems to Maxwell, bad prompts to the agent, etc.).
  - Split report into DA-related problems (EXtra, etc.) and agent-related problems.

## Drafting Manuscript

Impression of the feature:

- 

## Verdict

Positive:

- Agent behaved as expected.
- Grounded Docs worked well (and it is nice that it is also usable without an agent).
- Agent architecture is better than a rigid architecture. More flexible.

Negative:

- Nothing else

What was unexpected:

- No

What features do you miss:

- None

Other:

- Maybe it is good if the agent cannot run the code, as the user should understand what code the agent produced (overreliance).
- On the other side, running the code could lead to automatically fixing the bugs.

## Internal

### Implemented Improvements Before Starting the Session

- Kilo Code read permissions: Previous user auto-permitted many read actions. We kept them.

### Technical Details

- Timestamp: 2026-MM-DD-TT:00
- Setup:
  - VS Code + remote kernel via SSH to Maxwell Jupyter Lab + Kilo Code
  - Note: Agent could not execute code itself as it is outside the SSH environment and did not have access to the kernel.
- LLMs: GPT-5.3-Codex

### Improvement Notes

- 
