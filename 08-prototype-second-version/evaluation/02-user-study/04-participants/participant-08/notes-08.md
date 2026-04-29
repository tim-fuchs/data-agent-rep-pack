# Participant 08

## Demographics

What is your job position?

- scientist for experiment simulation (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- ChatGPT
- Gemini
- Claude

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- Develop method to predict diffraction intensity precisely for Bragg peak

## RAG Interaction (via Grounded Docs UI)

- Not required

## Code Generation/Explanation/Improvement (via AI agent)

- Q (Plan): I would like to estimate the (110) diffraction Bragg peak intensity of a P63 crystal deposited on a pixelized detector with pixel size of 200 um, sample to detector distance 12 mm and photon energy of 12 keV. Please compare the numerical ground truth with analytical results.
- R: Asked clarification question about P63 crystal via form. Afterward, created reasonable plan.
- Q (Code): Start implementation.
- R: Created a new notebook, executed the cells to test if errors exist. Result was as expected. BUT: it did not use SciPy (as participant expected) but used NumPy instead.
- Q: Estimate the peak width in reciprocal space using Gaussian function, select the pixels within the 3-sigma range in the reciprocal space as the detector ROI for numerical ground truth. Reduce the pixel siye to 10 um.
- Q (Ask): What is the orientation of the crystal and the incident beam direction and the normal direction of the detector?
- R: Reasonable
- Q (Code): Can you align the crystal c axis along the z direction and redo the calculation?
- R: Reasoning was not fully as expected at first. Further Q+R in Ask mode and then in Code mode followed. Result was overall good.

Further observations:

- Agent successfully executed code in notebook to check if it works correctly.
- Agent mixed library import and function defintions in a single cell.
- Agent did not use SciPy as it could not find it in the Jupyter kernel (although it was installed). Eventually, there was a connection problem with the server.
- Git:
  - Agent only asked to create Git environment after second change. But then, it asked after every change if it should create the environment.
  - It also asked to create a commit, but only once (after it created the Git environment.) and only a few changes later again.

## Reporting

Impression of the feature and report structure:

- Not tested due to limited time

## Verdict

Positive:

- Agent understood participant's questions.
- Agent gave relevant feedback and asked for clarification.
- Fast performance

Negative:

- Nothing

What was unexpected:

- Server connection problem

What features do you miss:

- Nothing

## Internal

### Implemented Improvements Before Starting the Session

- In the reporting skill, I removed the requirement that the agent must have edited code.

### Technical Details

- Timestamp: 2026-04-29-16:00
- Setup:
  - VS Code + remote kernel via SSH to Maxwell Jupyter Lab + Kilo Code
  - Agent instructions: AGENTS.md + skills directory
  - Note: Agent could not execute code itself as it is outside the SSH environment and did not have access to the kernel.
- LLMs: GPT-5.4

### Improvement Notes

- Agent should always put library imports in a dedicated cells in the beginning of the notebook.
