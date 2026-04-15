# Comparison of Candidates for Integrating Jupyter Lab

## Notes

- Use case:
  - Agent has to connect to a remote Jupyter Lab server hosted on the HPC cluster of EuXFEL/DESY.
  - A user can start this server manually via a remote Jupyter Hub server (also hosted by EuXFEL/DESY).

## Candidates

- **Jupyter Hub API + agentic VS Code extension (e.g., Continue)**
  - Overview:
    - EuXFEL provides [connectivity](https://docs.desy.de/maxwell/documentation/miscellaneous/jlab_vscode/) from its Jupyter Hub/Lab server to VS Code (documentation is slightly outdated).
    - [Continue](https://github.com/continuedev/continue/blob/main/extensions/vscode/README.md) is an actively maintained open source project.
  - Tested Versions:
    - EuXFEL-Own Solution: ?
    - Continue: 1.3.38
  - Date of Test: 2025-03-31
  - Documentation:
    - [EuXFEL documentation](https://docs.desy.de/maxwell/documentation/miscellaneous/jlab_vscode/)
    - [Continue documentation](https://docs.continue.dev/guides/ollama-guide#method-3-manual-configuration)

- **Jupyter AI (extension for Jupyter Lab)**
  - Overview: [Jupyter AI](https://jupyter-ai.readthedocs.io/en/v3/index.html) is an actively maintained open source project by Jupyter-affiliated developers.
  - Tested Version: 2.31.1
  - Date of Test: 2025-03-31
  - Documentation: [Jupyter AI documentation](https://jupyter-ai.readthedocs.io/en/v3/index.html)

- **Jupyter MCP Server (by Datalayer) + agentic standalone tool (e.g., OpenCode) or agentic VS Code extension (e.g., Continue)**
  - Overview:
    - [Jupyter MCP Server](https://jupyter-mcp-server.datalayer.tech) is an actively maintained open source project.
    - [OpenCode](https://opencode.ai) is an agentic harness, i.e., a standalone tool providing a multi-agent workflow.
    - [Continue](https://github.com/continuedev/continue/blob/main/extensions/vscode/README.md) is an actively maintained open source project.
  - Tested Versions:
    - Jupyter MCP Server: 0.22.1
    - OpenCode: ?
    - Continue: 1.3.38
  - Date of Test: 2025-03-31
  - Documentation:
    - [Jupyter MCP Server documentation](https://jupyter-mcp-server.datalayer.tech)
    - [OpenCode documentation](https://opencode.ai)
    - [Continue documentation](https://docs.continue.dev/guides/ollama-guide#method-3-manual-configuration)

- **Alternatives to VS Code extension Continue**
  - Why they are alternatives:
    - Offer state-of-the-art copilot features for VS Code
    - Are open-source
    - Can work with local endpoints
  - [Roo Code](https://roocode.com)
    - Could be even simpler in configuration than Continue
    - UI also displays token and credit use.
  - [Kilo](https://kilo.ai)
    - Heavy marketing focus on their subscription model and cloud features
  - [Cline](https://cline.bot)
    - Was buggy in our code generation tests
    - Provided an outdated list of models for providers OpenAI and Nebius in our tests. Heavy focus on Anthropic models.
  - [Tabby](https://www.tabbyml.com)
    - Requires starting and configuring a Tabby server first

## Requirements Analysis

### Access Remote Jupyter Lab Server

- **Jupyter Hub API + Continue**
  - Rating: -
  - Strengths:
    - User can flexibly switch between remote and local kernels as the notebook is stored on local machine.
  - Weaknesses:
    - User might need to have the IDE as well as the web browser open to work on the notebook and also browse the data.
      - By default, the file system of the HPC cluster (incl. dataset) is not available via the VS Code file browser, only via commands in the notebook cells.
      - User could add file browsing via the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension and [SSH access to HPC cluster](https://dataanalysis.pages.xfel.eu/user-documentation/offline/#ssh-access), but the connection was buggy in our experiments.
    - User cannot store the notebook on the HPC cluster (if no SSH connection established).

- **Jupyter AI**
  - Rating: ++
  - Strengths:
    - User can use the regular Jupyter Lab interface in the web browser to send prompts to the agent via the chat in the sidepanel or the `%%ai` cell command.
  - Weaknesses:
    - None

- **Jupyter MCP Server + OpenCode/Continue**
  - Rating: -
  - Strengths:
    - User can work in the regular Jupyter Lab environment to interact with the notebook and data.
  - Weaknesses:
    - User needs to have the agentic standalone tool/IDE extension as well as the web browser open to interact with the agent and inspect the notebook, which could be confusing or feel disconnected.

### Interact with Notebook Content

- **Jupyter Hub API + Continue**
  - Rating: ++
  - Strengths:
    - User can use a state-of-the-art copilot to interact with the notebook.
  - Weaknesses:
    - User must start the Jupyter Lab server first via the browser.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - User can request the agent to insert the response into a code cell, and can also request to generate an entire notebook.
    - User can select a single cell to ask questions about its content.
  - Weaknesses:
    - User must explicitly request the insertion into a cell. Otherwise, the response appears within the sidepanel or as cell output.
    - If the response contains code and text, either the code is formatted incorrectly in the cell output or the text is not converted to an inline comment in the code cell (at least in our experiments).

- **Jupyter MCP Server + OpenCode/Continue**
  - Rating: ++
  - Strengths:
    - User can use a state-of-the-art copilot to interact with the notebook.
  - Weaknesses:
    - User must start the Jupyter Lab server first via the browser.

### Latency Optimization

- **Jupyter Hub API + Continue**
  - Rating: ++
  - Strengths:
    - Continue supports streaming of responses, displaying the reasoning process, and all other state-of-the-art features.
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool supports streaming of responses.
  - Weaknesses:
    - Tool does not display the reasoning process of a multi-agent system.

- **Jupyter MCP Server + OpenCode/Continue**
  - Rating: ++
  - Strengths:
    - OpenCode runs subagents when necessary and supports any state-of-the-art copilot features.
    - Continue supports streaming of responses, displaying the reasoning process, and all other state-of-the-art features.
  - Weaknesses:
    - None

### Not Share User Data

- **Jupyter Hub API + Continue**
  - Rating: ++
  - Strengths:
    - EuXFEL: No third party involved, as far as we know.
    - Continue: [Telemetry can be deactivated in the UI.](https://docs.continue.dev/customize/telemetry)
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: ++
  - Strengths:
    - No telemetry involved, as far as we know from the documentation.
  - Weaknesses:
    - None

- **Jupyter MCP Server + OpenCode/Continue**
  - Rating: ++
  - Strengths:
    - Jupyter MCP Server: No telemetry involved, as far as we know from the documentation.
    - OpenCode: According to a [GitHub issue thread](https://github.com/anomalyco/opencode/issues/5554) and the [official documentation](https://opencode.ai), OpenCode does not use any telemetry.
    - Continue: [Telemetry can be deactivated in the UI.](https://docs.continue.dev/customize/telemetry)
  - Weaknesses:
    - None

### Implementation Effort

- **Jupyter Hub API + Continue**
  - Rating: +
  - Strengths:
    - Connection to Jupyter is provided and recommended by EuXFEL server admins.
    - User can configure everything by themselves and via a UI.
    - Continue provides out-of-the-box state-of-the-art copilot features to interact with the notebook.
  - Weaknesses:
    - Connection to Jupyter could be removed by admins without further notice.
    - User must install VS Code, the [JupyterHub extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-hub), and Continue.
    - User must configure the connection to the [Jupyter Lab server](https://docs.desy.de/maxwell/documentation/miscellaneous/jlab_vscode/) and the connection to the agent endpoint in [Continue](https://docs.continue.dev/guides/ollama-guide#method-3-manual-configuration) manually.

- **Jupyter AI**
  - Rating: --
  - Strengths:
    - User only needs to open Jupyter Lab in the web browser.
    - User can configure the LLM and its endpoint via a UI.
  - Weaknesses:
    - User or EuXFEL admins must install the Jupyter AI extension on the Jupyter server.
    - User must configure the connection to the agent endpoint and must enter a command in the notebook to activate the ``%%ai`` command.
    - EuXFEL admin could add predefined agents (e.g., OpenCode, Codex, Claude Code), but only via installation of additional libraries. User cannot do this.
    - EuXFEL admin could define and add custom agents (e.g., to our own agent endpoint), but only via complicated coding and deployment. User cannot do this.
    - In our experiments, the chat interface installed on the EuXFEL Jupyter Lab server was the old version, despite an up-to-date Lab server with version 4.x and an up-to-date Jupyter AI extension. We could not resolve this problem.
    - Feature set lacks behind GitHub Copilot and other competitors, e.g., user cannot select between predefined agent interaction modes such as "ask, plan, and implement" like in GitHub Copilot or OpenAI Codex.
    - Developers regularly publish breaking changes in the UI and configuration options.

- **Jupyter MCP Server + OpenCode/Continue**
  - Rating: +
  - Strengths:
    - User can configure everything by themselves (via terminal + UI).
    - OpenCode/Continue provides out-of-the-box state-of-the-art copilot features to interact with the notebook.
  - Weaknesses:
    - User must install MCP-related pip packages on the Jupyter server.
    - User must configure and start an MCP server on their local machine and configure an MCP client in OpenCode/Continue to connect to the EuXFEL Jupyter Lab via Jupyter MCP Server. We  prepared an [instructions file](config_mcp_jupyter.md) to document this process as the official documentation lacks detail and the Claude-focused MCP client configuration is not directly applicable to OpenCode/Continue.
    - User must configure the connection to the agent endpoint in [Continue](https://docs.continue.dev/guides/ollama-guide#method-3-manual-configuration).

### Component Replacement Effort

TODO
