# AGENTS.md

## Project Overview

- This project is focused on the [offline data analysis process](https://www.xfel.eu/organization/scientific_and_technical_groups/data_department/data_analysis/documentation_and_training_material/index_eng.html) at [European XFEL (EuXFEL)](https://xfel.eu).
- The user works in this project with one of two workflows:
  1. To work on a Jupyter notebook that is stored locally in this project but is using a kernel stored on a remote Jupyter Lab server.
  2. To use the `jupyter-mcp` server to connect to a Jupyter notebook stored on a remote Jupyter Lab server.
- This Jupyter Lab server executes its processes on the high-performance computing (HPC) cluster [Maxwell](https://docs.desy.de/maxwell/) to enable resource-demanding data analysis processes.
- Your task: Support the user in data analysis by generating, improving, or explaining code in the notebook.

## Rules

Always follow the steps in the sections below.

### Use Concise Language

- At the beginning of the session, activate the skill `/caveman lite` to reduce the length of your responses.

### Interact with Notebook Content

- If you are asked to edit code but a specific location is not provided, always assume first that the edit must be done in the file currently open and active in the editor.

- If you are asked to list available Jupyter notebooks, connect a notebook, or interact with a notebook, check the following locations (in this order):
  1. The currently open workspace
  2. The MCP server `jupyter-mcp-hpc`
  3. The MCP server `jupyter-mcp-local`
- Never edit files other than Jupyter notebooks, Python files, and Markdown files (data types `.ipynb`, `.py`, and `.md`).

- If you edited a Jupyter notebook file that is currently opened in the VS Code editor, report the following text:
  `**Important:** Notebook edited. You must close the file without saving it and then reopen it to see the changes made.`

### Generate HPC-Optimized Code

- If not requested otherwise, you work with Jupyter notebooks by default.

**Use EXtra-data library for data access**

- If you read and transform data from European XFEL, always use the features of the `extra-data` library.

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- No defensive coding with hard-coded default values for environment variables. If an environment variable is unavailable, the code should throw an error to the user.
- If you write 200 lines and it could be 50, rewrite it.
- Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.
- When your changes create orphans:
  - Remove imports/variables/functions that YOUR changes made unused.
  - Don't remove pre-existing dead code unless asked.
  - The test: Every changed line should trace directly to the user's request.

**Create atomic code components.**

- When generating a Jupyter notebook, spread the code as logical, atomic units across notebook cells.
- Good examples:
  - All `import` commands in a single cell, other code in subsequent cells
  - Creation + printing of a Dataframe object in a single cell
- Bad example:
  - `import` commands + further logic in a single cell
  - Printing commands + subsequent commands in a single cell

### Execute and Test Code on HPC Cluster

Always follow these steps when you generated code:

1. DO NOT test the code by executing it in your internal sandbox. Instead, create a new code file or edit an existing one (e.g., a Jupyter notebook) and execute the file with an available Jupyter kernel or Python environment.
   - ALWAYS ask the user first, which Jupyter kernel or Python environment you should use to execute the code.
   - You MUST NOT execute the code in your internal sandbox as the sandbox does not have access to the data and computational environment of the HPC cluster.
2. Review if any errors appeared (e.g., error messages in notebook cell output).
3. If errors appeared, rework your code and start again with step 1.

### Request User Feedback to Guide and Improve Solutions

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

- State your assumptions explicitly.
- If multiple interpretations of the request exist, present them and ask for a choice. Do not pick silently.
- If a simpler approach than requested exists, say so. Push back when warranted.
- If something is unclear, stop. Name what is confusing. Ask.

### Adapt Code Style and Explanations to User's Expectations

1. Check if the directory `CODE_STYLE` contains files.
2. If yes, reuse the coding style within these files as model for your edits. Particularly regarding the code design and documentation.

### Generate Code Documentation on Project- and Code-Level

- When you work with a Jupyter notebook, always create Markdown cells that describe the purpose of the code cells below.
- When you create a class, function, or method, always add a documentation comment.
- Ask if you should document the project with a README.md. Include the sections "What is this project about", "Prerequisites", "Install", "Start".

### Decompose a Request into Verifiable Goals

Examples:

- From "Add validation" to "Write tests for invalid inputs, then make them pass"
- From "Fix the bug" to "Write a test that reproduces it, then make it pass"
- From "Refactor X" to "Ensure tests pass before and after"
- For multi-step tasks, state a brief plan:

  ```bash
  1. [Step] > verify: [check]
  2. [Step] > verify: [check]
  3. [Step] > verify: [check]
  ```

## Work With Up-to-Date Information

- For answering user requests, follow this order until you received relevant information:

  1. Use information from the project context.
  2. Use the MCP server `grounded-docs` to retrieve relevant docs from the available libraries.
  3. Use the MCP server `github-mcp` to retrieve information from public code repositories. Focus particularly on repos of the organization `European-XFEL`.
  4. Use the MCP server `gitlab-mcp` to retrieve information from internal code repositories of European XFEL.
  5. Use the tool `webfetch`.

### Provide and Verify Citations

- ALWAYS provide at least one full URL as citation if you answered a prompt via information from `grounded-docs`, `github-mcp`, `gitlab-mcp`, or `webfetch`.
- ALWAYS verify if the URLs are still available with HTTP response `200`. If HTTP response `404`, find and verify alternative citation.

### Close Task with Narrative Summary and Recommended Steps

- When you completed an edit, always summarize:
  - What changed
  - Why it changed
  - Files touched
  - Next steps

### Report Conversations to EuXFEL Staff

- Instruct reporting process in a SKILL.md
- Instruct behavior in AGENTS.md:
  - When task completed, ask user if task summary should be reported.
  - If yes, execute skill.

### Recommend Using a Version Control System

ALWAYS do after each logical task chunk: Check if your edited files are recognized by a Git environment.

- If Git environment is not available, ask once per session if you should create a Git environment (Answer options: Yes, No). If yes, create the Git environment and commit the current changes to Git.
- If Git environment is available, ask if you should commit the current changes to Git (Answer options: Yes, No). If yes, commit the changes.
