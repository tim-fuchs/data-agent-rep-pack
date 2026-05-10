# Participant 11

## Demographics

What is your job position?

- Experimentalist + data scientist (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- ChatGPT

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- Load data for a run + run info
- Check data structure
- Analyze and plot time of flight info
- Create coincidence map

## RAG Interaction (via Grounded Docs UI)

- Q (EXtra-data): I want to open a specific remi example run. What do you need as the information to do this?
- A: Reasonable when I know the specific run number, but nothing specific to SQS
- Q (SQS docs): I want to open the remi example data run for N2. I have the proposal and run rumber. Can you give me a specific code to open the run?
- A: Relevant information retrieved

## Code Generation/Explanation/Improvement (via AI agent)

- Q (Ask): I want to open the remi example data run for N2. I have the proposal and run rumber. Can you give me a specific code to open the run?
- A: Provided info how to open a run
- Q: More specific instructions regarding proposal, run, and device
- Q (Plan + Code): Create notebook with this code
- A: Created notebook but did not show the specific device at first.
- Q (Code): Back and forth required to actually display the device.
- Q (Code): Run code to extract info from SQS_REMI_DLD6/DED/TOP detector. From extra component import the delayline detector and create hits info using dld.hits
- A: Almost correct, but had to remove the 'data=raw' parameter again as detector data is not available in the raw part.
- Q: Create a 1D and 2D plot for time-of-flight data
- A: Good result

Further observations:

- Agent provided URL as citation information and checked that URL is still available.
- In Plan mode, the agent creates the plan but does not print it. It just asks if it now should start with the implementation.
- Agent put everything into one code cell (imports, code, prints).

## Reporting

Impression of the feature and report structure:

- Not tested due to limited time

## Verdict

Positive:

- Works well

Negative:

- Agent should ask more clarification questions before editing code.

What was unexpected:

- Nothing

What features do you miss:

- Nothing

## Internal

### Implemented Improvements Before Starting the Session

- AGENTS.md:
  - Updated `Interact with Notebook Content` section
  - Updated `Test Code for Correctness and Safety Risk` section
  - Updated `Generate HPC-Optimized Code` section

### Technical Details

- Timestamp: 2026-05-06-11:00
- Setup:
  - VS Code + remote kernel via SSH to Maxwell Jupyter Lab + Kilo Code
  - Agent instructions: AGENTS.md + skills directory
- LLMs: GPT-5.4

### Improvement Notes

- Rework instructions on how agent should split code cells. In this session, it generated the initial notebook with a single code cell.
- Add instruction that agent should ask clarification questions.
