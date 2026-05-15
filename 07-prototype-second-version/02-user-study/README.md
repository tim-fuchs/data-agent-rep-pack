# Summary of User Study to Evaluate Second Prototype

## File Overview

// TODO

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
| - Reporting: Also enable reporting when agent has not generated code                   | 7                |

## Positive Notes

| Positive                                              | Participant     |
| ----------------------------------------------------- | --------------- |
| - Behavior: Agent understood and executed the task    | 7,12,13         |
| - Behavior: Fast performance                          | 7               |
| - Retrieval: Possibility and process to add new files | 1,7             |
| - Retrieval: Quality of documentation retrieval       | 1,2,3,4,5,12,13 |
| - Retrieval: Availability of citations                | 2,7             |
| - Retrieval: No hallucinations                        | 7               |
| - Coding: Code execution on HPC cluster possible      | 9               |
| - Reporting: Existence of reporting feature           | 1,2,3,4,5,10    |

## Open Improvement Potentials

| Improvement potential                                                                  | Participant |
| -------------------------------------------------------------------------------------- | ----------- |
| - Architecture: Agent should support displaying code diffs                             | 6           |
| - Behavior: Force behavior via agent hooks instead of AGENTS.md                        | 5           |
| - Behavior: Kilo Code asks to but cannot switch from Plan to Code agent                | 1,2         |
| - Behavior: Notebook changes of Kilo Code not visible until user reopens notebook file | 8           |
| - Behavior: Avoid required humal approvals for (fast) read operations                  | 1,3,10      |
| - Retrieval: Make European XFEL docs agent-ready                                       | 12,13       |
| - Retrieval: Inform user about outdated documentation (HTTP status 404)                | -           |
| - Behavior: Agent should ask clarification questions (e.g., relevant libraries)        | 7           |
| - Coding: Force spec-driven development                                                | 4,11,12     |
| - Coding: Add LSPs (e.g., Pylance) to improve code testing                             | 5           |
| - Coding: More minimalistic, prototyping-focused coding                                | 5,6         |
| - Coding: Agent must always display plan and ask for clarifications before coding      | 10,12       |
| - Report: Evaluate and improve quality of the report structure                         | 1,2,6,7     |
| - Report: Add a problem-focused reporting feature                                      | 2,4,6       |
| - Manuscript draft: feature not tested due to lacking time                             | all         |

## Design Recommendations

### System Architecture

- Decide on system architecture based on variance of user workflows.
  - Process:
    - Data analysis processes of different facilities, as well as instruments and experiment types at one facility differ from each other.
    - Hence, the agent must support a varying number of analysis workflows.
    - Number of workflows at some facilities might be low and the workflows rigid.
    - At European XFEL, the number is high and the users with diverse skills and objectives require adaptable workflows.
  - Solution:
    - For rigid workflows: decide to develop a SaaS that automates the workflows (e.g., with n8n)
    - For flexible workflows: decide to recommend a user-installed agentic tool and prepare a basis for further refinement (AGENTS.md, skills, MCP servers)

- Check user's tool expectations before recommending agentic tool.
  - Problem:
    - Different users are used to or require different user interfaces (CLI, GUI, IDE extension, experience with specific agents)
    - Agentic tools are mostly interoperable, but differ in their user interfaces and specific features. Examples:
      - Displays code diffs:
        - Yes: GitHub Copilot
        - No: Kilo Code
      - Displays token costs:
        - Yes: Kilo Code
        - No: OpenCode
      - Configuration entirely via GUI:
        - Yes: Kilo Code
        - No: OpenCode
      - Provides various user interfaces:
        - Yes: OpenCode
        - No: Roo Code
  - Solution:
    - Refer to our description for possible combinations of user interfaces, e.g., web browser + standalone agent desktop app.
    - Provide user with an overview of recommended tools for specific workflows.

### General Agent Behavior

- Use programmatic hooks to force the agent to adhere to behavior.
  - Problem:
    - Different models and models with different reasoning levels adhere to natural-language instructions differently.
    - In our study, even the large GPT-5.3-Codex model ignored some of our instructions.
    - Examples that reoccured multiple times during user study:
      - Agent does not request to create Git environment and commit changes after task completion.
      - Agent does not request user to close and reopen the edited notebook file to make code changes visible to user.
      - Agent requests to create and send the conversation report, but requests in varying ways:
        - Explicit form a user must answer (best option)
        - Text-embedded questions
        - Text-embedded information (worst option)
  - Solution:
    - Recommend user to use an agentic tool that supports agent hooks (and not just AGENTS.md instructions).
      - OpenCode supports hooks via plugins and even provides a plugin marketplace.
      - Kilo Code does not support hooks.
    - You or user can add code plugins to the hooks to ensure that the agent will always execute specific workflows.
    - If agentic tool does not support hooks, add detailed instructions in AGENTS.md:
      - Instruct on reoccuring workflows, including single workflow steps and conditions.
      - Instruct on responding with defined formulations.
      - Instruct with providing good and bad examples for each workflow.
      - Instruct on decomposing a request into verifiable goals to provide users with transparency regarding the agent workflow, including any verification steps and results.
      - Throughout the user study sessions with Kilo Code, we could solve the recurring problems via these instructions.

- Configure required types of human approvals in advance.
  - Problem:
    - We started the first session without configuring any auto-approvals.
    - Therefore, Kilo Code requested approval for any MCP tool call, even for simple read operations.
    - Participant was annoyed and overwhelmed by the mass of approval actions quickly. At some point, they just approved without even reading the request.
  - Solution:
    - Prepare an agent config file (e.g., `kilo.jsonc` or `opencode.json`) that contains auto-approval entries for uncritical actions.

### Knowledge Retrieval

- Make available documentation agent-ready.
  - Problem:
    - Complex documents (e.g., complicated table structures, relevant text in figures) are hard to analyze computationally.
    - Incomplete API reference documentation lets agent speculate about the correct workflow.
    - Superficial API reference documentation (e.g., reoccuring toy examples) lets agent speculate about the correct parameter values.
  - Solution:
    - Provide *llm.txt* versions of your documentation.
    - API reference documentation must be available for every software library.
    - API reference documentation must provide explanations and useful examples for **each** operation.

- Steer agent toward relevant knowledge sources.
  - Problem:
    - Agent has various knowledge sources available (indexed RAG docs, all public GitHub repos, etc.)
    - Agent might require multiple MCP tool calls to find and retrieve relevant docs.
    - Agent might use irrelevant docs.
  - Solution:
    - In AGENTS.md, steer agent toward relevant documentation:
      - Refer to use specific docs indexed in RAG system.
      - Refer to specific GitHub/GitHub repositories (e.g., of European XFEL organization on GitHub).

- Force order of knowledge sources during knowledge retrieval.
  - Problem:
    - Agent might conduct complicated web search, instead of quickly retrieving relevant docs from RAG system.
  - Solution:
    - In AGENTS.md, force the order of knowledge sources for knowledge retrieval.
    - We forced the following order:
      1. Available context within current project
      2. RAG system
      3. GitLab
      4. GitHub
      5. Internet

- Enable user to customize knowledge retrieval workflow.
  - Problem:
    - You might have configured a workflow for knowledge retrieval:
      - Various docs in RAG system
      - Instructions in AGENTS.md to define the workflow.
    - However, user might need to steer agent towards further docs (websites, private files, publications).
      - Problem occurs especially for a high number of workflows or workflow variants.
      - Admin might not be able to recognize and add all relevant docs upfront.
      - Example: In 8 of 13 user study sessions, users added further docs to the RAG system.
  - Solution:
    - Make the interface of the RAG system available to the user.
    - Allow user to add further documents to the RAG system, or to add their own RAG system to the agentic system.
    - Allow user to customize retrieval workflow (e.g., via local AGENTS.md or agent hooks).

- Use small LLM with medium/high reasoning for knowledge retrieval.
  - Problem:
    - Existence of various knowledge sources can lead to many MCP tool calls.
    - Each call requires tokens (and costs money).
    - This leads to expensive sessions when using a large LLM (e.g., GPT-5.4).
  - Solution:
    - Use a small LLM (GPT-5.4-mini) with medium/high reasoning level.
    - The small LLM is much cheaper.
    - Reasoning process usually leads to good results.
    - Also, small model could have lower latency than large model.

### Code Generation

- Force spec-driven development.
  - Problem:
    - Code agent might use wrong/no library to implement user request.
    - Code agent might select wrong/unclear parameter values for code operations.
    - User must request corrections or additional explanations.
  - Solution:
    - Recommend the user to use the Plan agent to brainstorm a solution before switching to the Code agent.
    - Force the agent to always display its implementation plan and to ask clarification questions before starting to code, even if the user has not used Plan agent.

- Force iterative prototyping of minimal solutions.
  - Problem:
    - User expectation:
      - First, create a simple solution as proof of concept.
      - Later, create production-ready code (with error handling, default values, etc.)
    - Default agent behavior:
      - Create production-ready code as response to first user request.
      - This results in a lot of code that is overwhelming the user and mismatches their expectations.
  - Solution:
    - Instruct agent to deliver minimal solution first. Provide production-ready code only on explicit demand.
    - Eventually adopt and adjust the instructions of the [Andrej Karparthy Skills](https://github.com/forrestchang/andrej-karpathy-skills) repository.
      - In our user study, the agent consistently considered the instructions that provided explicit examples, e.g., for goal-driven task execution.
      - However, the agent ignored more vague instructions, e.g., instructions focused on simplicity.
      - If you want to reuse such instructions, ensure and test that they are specific enough.

- Forbid hard-coding default values for mandatory user input.
  - Problem:
    - By default, agent focuses on defensive programming.
    - Hence, agent creates complicated code structures to avoid any runtime errors.
    - This included hard-coding default parameter values of mandatory environment variables, including ports of servers or even sensitive API tokens.
  - Solution:
    - Forbid the agent from hard-coding default values for mandatory environment variables.
    - Instruct the agent to implement error messages if such environment variables are unavailable.

- Force request to clarify the execution environment.
  - Problem:
    - By default, agent will execute code in sandbox, not in real environment.
    - In principle, availability of executing code in agent sandbox is a great feature for safety and latency.
    - In our case, sandbox was not practical as data, computational resources, and libraries of HPC cluster were required.
    - Furthermore, if agent executes code in real environment, it might use the wrong Jupyter kernel or Python environment.
  - Solution:
    - We added explicit instructions forbidding the agent to use the internal sandbox, and using the real environment instead.
    - We instructed the agent to ask for the execution environment instead of selecting any available kernel or environment itself.

- Use large LLM with low/medium reasoning for code generation.
  - Problem (our observations from using GPT-5.4-mini with medium reasoning):
    - Agent invoked various MCP tools for each change request, resulting in high latency.
    - Agent did not adhere to our instructions regarding the reuse of specific libraries from the European XFEL.
  - Solution (switching to GPT-5.4 with medium reasoning):
    - Agent invoked less MCP tools, resulting to shorter latency.
    - Agent reused European XFEL libraries.
