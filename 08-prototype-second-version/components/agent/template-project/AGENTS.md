# AGENTS.md

## Project Overview

- This project is focused on the [offline data analysis process](https://www.xfel.eu/organization/scientific_and_technical_groups/data_department/data_analysis/documentation_and_training_material/index_eng.html) at [European XFEL (EuXFEL)](https://xfel.eu).
- The user works in this project with one of two workflows:
  1. To use the `jupyter-mcp` server to connect to a Jupyter notebook stored on a remote Jupyter Lab server.
  2. To work on a Jupyter notebook that is stored in this project but is using a kernel stored on a remote Jupyter Lab server.
- This Jupyter Lab server executes its processes on the high-performance computing (HPC) cluster [Maxwell](https://docs.desy.de/maxwell/) to enable resource-demanding data analysis processes.
- Your task: Support the user in data analysis by generating, improving, or explaining code in the notebook.

## Rules

Always follow the steps in the sections below.

### Interact with Notebook Content

- Instruct to use Jupyter MCP in AGENTS.md
- You can read everything available to you via `jupyter-mcp`.
- Never edit files other than Jupyter notebooks and Python files (data types `.ipynb` and `.py`).

### Generate HPC-Optimized Code

- Instruct code conventions in AGENTS.md

### Test Code for Correctness and Safety Risk

- Instruct testing process in AGENTS.md

### Request User Feedback to Guide and Improve Solutions

- Instruct feedback behavior via AGENTS.md

### Adapt Code Style and Explanations to User's Expectations

- Instruct style adaption in AGENTS.md and via a CODE_STYLE directory
- Create an example project, add a CODE_STYLE directory, add a notebook file as example
- Instruct expected explanations in AGENTS.md

### Generate Code Documentation on Project- and Code-Level

- Instruct expected documentation in AGENTS.md
  - Agent should prompt the user for documentation preferences.
  - The prompt should include an option for the CODE_STYLE directory.

### Request Human Approval for Sensitive Actions

- Describe recommended approval configuration via tool settings.
- (Eventually,) instruct use-case-specific instructions for execution environment in AGENTS.md, e.g.:
  - Do not automatically execute heavy-load commands in local environment
  - Do not automatically execute batch jobs

- Stop and ask for permission before:
  - File edits
  - Code execution
  - Dependency upgrades
  - Irreversible changes

### Decompose a Request into Verifiable Tasks

- For every task:
  1. Understand the request.
  2. Inspect relevant files.
  3. Propose a minimal plan.
  4. Make changes.
  5. Validate.
  6. Summarize results.

## Work With Up-to-Date Code-Relevant Information

- For answering user requests focused on software development, data analysis, or European XFEL, follow this order until you received relevant information:

  1. Use the MCP server `grounded-docs` to retrieve docs.
  2. Use the MCP server `github-mcp` to retrieve information from repositories. Focus particularly on repos of the organization `European-XFEL`.
  3. Use the plugin `opencode-websearch-cited`.
  4. Use the tool `webfetch`.

- For answering all other request, follow this order until you received relevant information:

  1. Use the plugin `opencode-websearch-cited`.
  2. Use the tool `webfetch`.

### Close Tasks with Narrative Summaries and Recommended Next Steps

- When task complete, provide:
  - What changed
  - Why it changed
  - Files touched
  - Remaining risks
  - Next steps

### Support Responses with Citations, Confidence Levels, or Verification Steps

- Instruct citation and verification behavior in AGENTS.md

### Report Conversations to EuXFEL Staff

- Instruct reporting process in a SKILL.md
- Instruct behavior in AGENTS.md:
  - When task completed, ask user if task summary should be reported.
  - If yes, execute skill.

### Recommend Using a Version Control System

- Instruct Git versioning in a SKILL.md:
  - Skill 1: git:init
  - Skill 2: git:commit
- Instruct behavior in AGENTS.md:
  - When user wants to connect to a notebook via Jupyter MCP:
    - Check if Git environment is available on the server (**check if this is possible via Jupyter MCP**).
    - If not, ask user if agent should execute git:init skill.
  - When agent completed a task, ask if agent should execute git:commit skill.
    - If yes and Git environment not available, execute git:init skill beforehand.

### Optimize Latency

- Install the [caveman](https://github.com/JuliusBrussee/caveman) skill.
- Instruct using the caveman skills in lite mode in AGENTS.md.

## Improve Latency

- At the beginning of the session, use the skill `/caveman lite` to reduce the length of your responses.
