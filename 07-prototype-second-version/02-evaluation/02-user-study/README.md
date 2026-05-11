# User Study to Evaluate Second Prototype

## Demographics

### Profession

- 8 participants with a computer-science-focused profession:
  - 3 data scientists
  - 3 software engineers
  - 2 group managers
- 5 participants with a physics-focused profession:
  - 1 theoretician / data scientist
  - 1 scientist for experiment simulations
  - 2 instrument scientists
  - 1 experimentalist

### Use of Gen AI

- 7 Every day
- 4 Multiple days per week
- 0 Once per week
- 2 Less than once per week
- 0 Never

### AI Assistants

- 11 ChatGPT
- 7 Gemini
- 6 European XFEL RAY (with OpenAI GPT backend)
- 4 Claude
- 3 Mistral
- 3 GitHub Copilot
- 2 Claude Code
- 2 Codex
- 1 Apple Intelligence
- 1 Brave Leo

### Data Analysis

- 5 Every day
- 4 Multiple days per week
- 0 Once per week
- 4 Less than once per week
- 0 Never

## Use Cases

- Analyze SPB data of AGIPD detector
- Calibrate SQS data
- Estimate resolution of a detector used for SCS instrument
- Display geometry of AGIPD-1M and LPD detectors
- Test the new EXtra component [Scan](https://extra.readthedocs.io/en/latest/components/scans/#extra.components.Scan) for data of a motor device
- Open a dataset, do simple computation, make it scalable
- Find cosmic muons in data
- Use the data analysis features of the SCS Toolbox
- Predict diffraction intensity for Bragg peaks
- Execute Slurm batch jobs for running code in parallel
- Calculate intensity of XGM data for a set of runs
- Apple the Proposal component of the EXtra library
- Analyze time-of-flight data
- Process crystallography data with EXtra-xwiz library

## Implemented Improvements

| Improvement                                                          | Participant |
| -------------------------------------------------------------------- | ----------- |
| - Further documentation indexed in Grounded Docs:                    | 1,2,3       |
| - Agent reuses (correct) European XFEL libraries for code generation | 1,2         |
| - Agent creates atomic cells in computational notebook               | 4           |
| - Agent consistently requests to create Git environment and commit   | 1,4         |
| - Agent executes code via notebook, not via sandbox                  |             |
| - Less defensive coding                                              |             |
|                                                                      |             |
|                                                                      |             |
|                                                                      |             |

## Positive Notes

| Positive                             | Participant |
| ------------------------------------ | ----------- |
| - Possibility to index local files   | 1           |
| - Quality of documentation retrieval | 1,2,3,4     |
| - Existence of reporting feature     | 1,2,3,4     |
| - Availability of citations          | 2           |

## Open Improvement Potentials

| Improvement potential                                               | Participant |
| ------------------------------------------------------------------- | ----------- |
| - Tool: Kilo Code asks to but cannot switch from Plan to Code agent | 1, 2        |
| - Report: Evaluate the quality of the report structure in detail    | 1, 2        |
| - Report: Add a problem-focused reporting feature                   | 2,4         |
| - Tool: Configuration of required humal approvals                   | 1,3         |
| - Manuscript draft: feature not tested due to lacking time          | all         |
| - Coding: Explain which parameter values to choose                  | 4           |
|                                                                     |             |
|                                                                     |             |

## Design Recommendations

**System architecture:**

- Decide on agent system architecture based on variance of user workflows.
  - Varying workflows: user-installed agent with flexible agent instructions + deployed MCP servers
  - Rigid workflows: SaaS to automate workflows
  - Participants: 4

**General behavior:**

- Small models are sufficient for knowledge retrieval but insufficient for coding
  - Observations from comparing GPT-5.4-mini vs. GPT-5.4
  - Agent does not adhere to instructions about reusing existing libraries.
  - Agent calls various MCP tools to retrieve knowledge for any small change request.
  - Participants: 2

- In `AGENTS.md`, instruct agent to reuse specific commands and text quotes.
  - Otherwise, agent might not execute the commands, respond to a request with a different text, or ignore the instruction entirely.
  - Reoccuring problems:
    - Request to use Git init and commit after task completion
    - Request to close and reopen the edited notebook file to make code changes of agent visible
  - Solution: In AGENTS.md, explicit quote what to ask the user + explicit answer options.
  - Participants: 1,2,4

- Check if agentic tool has a "human approval" configuration interface.
  - By default, agent will request approval for any MCP tool call, even for read operations.
  - Auto-approve any read operation (at least if they are usually finished quickly).
  - Otherwise, user can be overwhelmed by the mass of approval actions.
  - Participants: 3

**Code generation:**

- Check if agent should test code in its sandbox or with real environment.
  - In principle, availability of sandbox is a great feature for safety and latency.
  - In our case, sandbox was infeasible (data, computational resources, libraries of HPC cluster required).
  - We required explicit instructions to forbid the agent using the internal sandbox.
  - Participants:

- Instruct how the generated code must be structured.
  - By default, agent often put all code into a single notebook cell.
  - This included import commands and long-running analysis steps, as well as plotting commands.
  - For notebooks, atomic cell structure required (separate cells for import, analysis, plotting).
  - Participants: 4

- Instruct to throw errors instead of defensive coding.
  - Agents create complicated code structures to avoid runtime errors.
  - This includes hard-coding default values of expected environment variables (that might contain sensitive data).
  - This does not reflect human-like prototyping but focuses on building production-ready code.
  - You must instruct agent explictly to avoid such defensive coding and, instead, to implement error messages when expected data is unavailable during runtime.
  - Participants: 4
