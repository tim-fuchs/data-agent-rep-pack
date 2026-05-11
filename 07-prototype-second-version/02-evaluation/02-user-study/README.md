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

| Improvement                                                                            | Participant      |
| -------------------------------------------------------------------------------------- | ---------------- |
| - Behavior: Agent consistently requests to create Git environment and commit           | 6                |
| - Behavior: Agent consistently requests to close and reopen notebook after code change | 6                |
| - Retrieval: Further documentation indexed in Grounded Docs                            | 1,2,3,5,7,8,9,13 |
| - Retrieval: Agent should check if URL of retrieved chunk is still available           | 7                |
| - Coding: Agent reuses (correct) European XFEL libraries for code generation           | 1,2              |
| - Coding: Agent creates atomic cells in computational notebook                         | 4,7,11           |
| - Coding: Agent executes code via notebook, not via sandbox                            | 6,9,10           |
| - Coding: Agent asks about Jupyter kernel or Python environment for code execution     | 10               |
| - Coding: Less defensive coding, more minimalistic code with error propagation         | 5,10             |
| - Reporting: Agent consistently requests to report conversation to staff               | 6                |
| - Report: Also enable reporting when agent has not generated code                      | 7                |
|                                                                                        |                  |
|                                                                                        |                  |
|                                                                                        |                  |

## Positive Notes

| Positive                                              | Participant     |
| ----------------------------------------------------- | --------------- |
| - Behavior: Agent understood and executed the task    | 7,12,13         |
| - Behavior: Fast performance                          | 7               |
| - Retrieval: Possibility and process to add new files | 1,7             |
| - Retrieval: Quality of documentation retrieval       | 1,2,3,4,5,12,13 |
| - Retrieval: Availability of citations                | 2,7             |
| - Retrieval: No hallucinations                        | 7               |
| - Reporting: Existence of reporting feature           | 1,2,3,4,5,10    |
| - Coding: Code execution on HPC cluster possible      | 9               |

## Open Improvement Potentials

| Improvement potential                                                                   | Participant |
| --------------------------------------------------------------------------------------- | ----------- |
| - Architecture: Agent should support displaying code diffs                              | 6           |
| - Behavior: Enforce behavior via agent hooks instead of AGENTS.md                       | 5           |
| - Behavior: Kilo Code asks to but cannot switch from Plan to Code agent                 | 1,2         |
| - Behavior: Avoid required humal approvals for (fast) read operations                   | 1,3,10      |
| - Retrieval: Make European XFEL docs agent-ready                                        | 12,13       |
| - Behavior: Agent should ask clarification questions (e.g., relevant libraries)         | 7           |
| - Coding: Ask clarification questions for decisions (parameter values, libraries, etc.) | 4,11,12     |
| - Coding: Add LSPs (e.g., Pylance) to improve code testing                              | 5           |
| - Coding: More minimalistic, prototyping-focused coding                                 | 5,6         |
| - Coding: Agent must always display plan and ask for clarifications before coding       | 10,12       |
| - Report: Evaluate and improve quality of the report structure                          | 1,2,6,7     |
| - Report: Add a problem-focused reporting feature                                       | 2,4,6       |
| - Manuscript draft: feature not tested due to lacking time                              | all         |
|                                                                                         |             |
|                                                                                         |             |

## Design Recommendations

**System architecture:**

- Decide on agent system architecture based on variance of user workflows.
  - Varying workflows: user-installed agent with flexible agent instructions + deployed MCP servers
  - Rigid workflows: SaaS to automate workflows

- Check which features users require before recommending an agentic tool. Examples:
  - Display code diffs:
    - Yes: GitHub Copilot
    - No: Kilo Code
  - Display token costs:
    - Yes: Kilo Code
    - No: OpenCode
  - Configuration entirely via GUI:
    - Yes: Kilo Code
    - No: OpenCode
  - Various user interfaces:
    - Yes: OpenCode
    - No: Roo Code

**General agent behavior:**

- In `AGENTS.md`, instruct agent to reuse specific commands and text quotes.
  - Otherwise, agent might not execute the commands, respond to a request with a different text, or ignore the instruction entirely.
  - Reoccuring problems:
    - No request to use Git init and commit after task completion
    - No request to close and reopen the edited notebook file to make code changes of agent visible
    - Varying requests to report conversation to staff (via explicit forms, text-embedded questions, text-embedded information)
  - Solution: In AGENTS.md, explicit quote what to ask the user + explicit answer options.

- Use programatic agent hooks instead of AGENTS.md instructions.
  - Whenever possible.
  - Agent will always execute the hooks, but not always consider all AGENTS.md instructions.
  - Problem: not a common feature yet.
    - OpenCode supports hooks and related plugins.
    - Kilo Code does not provide hooks.

- Preconfigure required human approvals.
  - By default, agent will request approval for any MCP tool call, even for read operations.
  - Auto-approve any read operation (at least if they are usually finished quickly).
  - Otherwise, user can be overwhelmed by the mass of approval actions.

**Knowledge retrieval:**

- Make your documentation agent-ready.
  - Problem:
    - Complex documents (e.g., complicated table structures, relevant text in figures) is hard to analyze computationally.
    - Incomplete API reference documentation let agent speculate about the correct workflow.
    - Superficial API reference documentation (e.g., reoccuring toy examples) let agent speculate about the correct parameter values.
  - Solution:
    - Provide *llm.txt* versions of your documentation.
    - API reference documentation must be available for every library.
    - API reference documentation must provide explanations and useful examples for **each** operation.

- Instruct agent to use specific knowledge sources.
  - Problem:
    - Agent has various knowledge sources available (indexed RAG docs, all public GitHub repos, etc.)
    - Agent might require multiple MCP tool calls to find and retrieve relevant docs.
  - Solution:
    - In AGENTS.md, hint towards relevant documentation:
      - Use specific RAG docs for known workflows.
      - Retrieve knowledge from specific GitHub/GitHub repositories (e.g., European XFEL organization on GitHub).

- Instruct order of knowledge sources:
  - Problem:
    - Instead of quickly retrieving relevant docs from RAG system, agent might conduct complicated web search.
  - Solution:
    - In AGENTS.md, enforce order of knowledge sources:
      1. Available context within current project
      2. RAG system
      3. GitLab
      4. GitHub
      5. Internet

- Enable customization of relevant documentation.
  - Problem:
    - You might have preconfigured a set of relevant documentation.
      - Indexing docs in RAG system
      - Steering to relevant docs in AGENTS.md
    - User needs to steer agent towards further docs (websites, private files, publications).
    - Problem occurs especially for varying use cases for which admin might not be able to recognize and add all relevant docs upfront.
    - In 8 of our sessions, users added further docs to the RAG system.
  - Solution:
    - Allow user to index further docs to RAG system.
    - Allow user to customize AGENTS.md.

- Use small LLM with medium/high reasoning level for retrieval tasks.
  - Problem:
    - Various knowledge sources require many MCP calls
    - Each call costs tokens (and money)
    - Expensive for large LLMs (e.g., GPT-5.4)
  - Solution:
    - Use small LLM (GPT-5.4-mini) with medium/high reasoning level
    - Cheap operations
    - Reasoning leads to good results
    - Also, small model could have lower latency than large model.

- Enforce citations.

- Double-check availability of retrieved and cited resources.
  - Problem:
    - The documentation chunks that the RAG system retrieved might be related to a URL that is not available in the internet anymore.
  - Solution:
    - Instruct agent to check the HTTP status of the URL (200 vs. 404).
    - If 404, search for alternative knowledge resources (e.g., via webfetch).

**Code generation:**

- Enforce spec-driven development.
  - Problem:
    - Code agent might use wrong/no library to implement user request.
    - Code agent might select wrong/unclear parameter values for code operations.
  - Solution:
    - Recommend user to use Plan agent to brainstorm a solution before switching to Code agent.
    - Enforce agent to display its implementation plan and ask clarification questions before starting to code (even if user has not used Plan agent).

- Use large LLM with low/medium reasoning level for coding tasks.
  - Problem (observations from using GPT-5.4-mini with medium reasoning):
    - Agent calls various MCP tools for each small change request (long latency).
    - Agent does not adhere to instructions about reusing existing libraries.
  - Solution (switching to GPT-5.4 with medium reasoning):
    - Agent calls less MCP tools (short latency)
    - Agent adheres to reusing existing libraries.

- Enforce clarification question on execution environment.
  - Problem:
    - By default, agent will execute code in sandbox, not in real environment.
    - In principle, availability of executing code in agent sandbox is a great feature for safety and latency.
    - In our case, sandbox was not practical as data, computational resources, and libraries of HPC cluster were required.
    - Furthermore, if agent executes code in real environment, it might use the wrong Jupyter kernel or Python environment.
  - Solution:
    - We added explicit instructions forbidding the agent to use the internal sandbox, and using the real environment instead.
    - We instructed the agent to ask for the execution environment instead of selecting any available kernel or environment itself.

- Instruct the expected code structure.
  - By default, agent often put all code into a single notebook cell.
  - This included import commands and long-running analysis steps, as well as plotting commands.
  - For notebooks, atomic cell structure required (separate cells for import, analysis, plotting).

- Instruct to propagate errors, and forbid defensive coding.
  - Agents create complicated code structures to avoid runtime errors.
  - This includes hard-coding default values of expected environment variables (that might contain sensitive data).
  - This does not reflect human-like prototyping but focuses on building production-ready code.
  - You must instruct agent explictly to avoid such defensive coding and, instead, to implement error messages when expected data is unavailable during runtime.

- Instruct to create minimalistic, prototyping-focused code.
  - User expectation:
    - First, create a simple solution as proof of concept.
    - Later, create production-ready code (with error handling, refactoring, etc.)
  - Problem:
    - Agent tries to create production-ready code from the start.
    - This results in a lot of code overwhelming the user.
  - Solution:
    - Use and improve the [Andrej Karparthy Skills](https://github.com/forrestchang/andrej-karpathy-skills) instructions.
      - We reused the instructions in the AGENTS.md from the first session.
      - Agent consistently considered some instructions that had very explicit examples, e.g., for goal-driven task execution.
      - However, Agent did not fulfill the simplicity-focused instructions.
    - Make vague instructions more explicit.
      - Always add good and bad examples.
