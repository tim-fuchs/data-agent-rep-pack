# Comparison of Candidates for Connecting to HPC Cluster

## Notes

- Use case:
  - Agent must connect to a remote Jupyter Lab server hosted on the HPC cluster of EuXFEL.
  - User can start this server manually via the Jupyter Hub server operated by EuXFEL.
  - User has only limited options, to install/update any pip packages on Jupyter Lab.

## Candidates

- **[Jupyter Lab API](https://jupyterlab.readthedocs.io/en/latest/)**
  - Version: 4.1.6
  - What:
    - User can set a Jupyter Lab token and use it, e.g., in VS Code to connect a local Jupyter notebook file with the remote Jupyter Lab kernel.
    - User can then use VS Code and a local agentic tool to edit and execute the notebook file.
    - EuXFEL provides (slightly outdated) [docs](https://docs.desy.de/maxwell/documentation/miscellaneous/jlab_vscode/) for this process, focused on for their Jupyter Hub/Lab server.

- **[Jupyter MCP](https://jupyter-mcp-server.datalayer.tech)**
  - Version: 0.22.1
  - What:
    - MCP server providing tools to access, read, and edit files of a Jupyter Lab server via a agentic tool
    - User could connect their local agentic tool with Jupyter MCP to edit notebook files on the remote Jupyter Lab server.
    - The Jupyter AI extension for Jupyter Lab also uses Jupyter MCP to access the notebook files of the server.

- **[VS Code Remote](https://code.visualstudio.com/docs/remote/ssh)**
  - Version: 0.122.0
  - What:
    - SSH access to the HPC cluster via VS Code Remote extension (`ssh $USER@max-exfl-display.desy.de`)
    - See [docs](https://dataanalysis.pages.xfel.eu/user-documentation/offline/#getting-access) of EuXFEL Data Analysis group.

## Requirements Analysis

### Access HPC Cluster

- **Jupyter Lab API**
  - Rating: +
  - Strengths:
    - User can store the notebook on local machine.
    - User can flexibly switch between remote and local kernels as the notebook is stored on local machine.
  - Weaknesses:
    - User might need to have the IDE as well as the web browser open to work on the notebook and browse the data via a GUI.
      - The files of the Jupyter Lab server are not visible in the VS Code file browser.
      - They can only be accessed via commands in the notebook cells.
    - User cannot store the notebook on the HPC cluster.

- **Jupyter MCP Server**
  - Rating: -
  - Strengths:
    - User can work in the regular Jupyter Lab environment to interact with the notebook and data.
  - Weaknesses:
    - User needs to have the agentic standalone tool/IDE extension as well as the web browser open to interact with the agent and inspect the notebook, which could be confusing or feel disconnected.

- **VS Code Remote**
  - Rating: +
  - Strengths:
    - User can store the notebook on the HPC cluster.
    - User can browse all data of the Jupyter Lab server via the VS Code file browser.
  - Weaknesses:
    - SSH connection can break quickly, e.g., when briefly locking the computer.

### Interact with Notebook Content

- **Jupyter Lab API**
  - Rating: ++
  - Strengths:
    - User can use an agentic tool on their computer to interact with the notebook.
  - Weaknesses:
    - User must start the Jupyter Lab server first via the browser.

- **Jupyter MCP Server**
  - Rating: ++
  - Strengths:
    - User can use an agentic tool on their computer to interact with the notebook.
  - Weaknesses:
    - User must start the Jupyter Lab server first via the browser.

- **VS Code Remote**
  - Rating: +
  - Strengths:
    - User can use an agentic tool within VS Code to interact with the notebook.
  - Weaknesses:
    - Agentic tools that start a local server (e.g., to handle background tasks of sub-agents) might not work in the SSH session (e.g., Kilo Code).
    - Selection of agentic tools is restricted to VS Code extensions.

### Latency Optimization

- **Jupyter Lab API**
  - Rating: -
  - Strengths:
    - Notebook file is directly connected to the remote Jupyter kernel.
  - Weaknesses:
    - Agentic tool needs to execute the notebook with the remote kernel to test the correctness of the code if data, software, or computational resources of the HPC cluster are required. Agent must not use its internal sandbox then.

- **Jupyter MCP Server**
  - Rating: +
  - Strengths:
    - Agentic tool can use tools of Jupyter MCP to execute code.
  - Weaknesses:
    - Overhead due to MCP execution process

- **VS Code Remote**
  - Rating: -
  - Strengths:
    - Notebook file is directly connected to the remote Jupyter kernel.
  - Weaknesses:
    - Agentic tool needs to execute the notebook with the remote kernel to test the correctness of the code if data, software, or computational resources of the HPC cluster are required. Agent must not use its internal sandbox then.

### Not Share User Data

- **Jupyter Lab API**
  - Rating: +
  - Strengths:
    - No telemetry in Jupyter Lab, as far as we know.
    - Telemetry of VS Code can be deactivated.
  - Weaknesses:
    - None

- **Jupyter MCP Server**
  - Rating: ++
  - Strengths:
    - No telemetry in Jupyter MCP Server, as far as we know from the documentation.
  - Weaknesses:
    - None

- **VS Code Remote**
  - Rating: +
  - Strengths:
    - Telemetry of VS Code can be deactivated.
  - Weaknesses:
    - None

### Implementation Effort

- **Jupyter Lab API**
  - Rating: ++
  - Strengths:
    - Quick setup
  - Weaknesses:
    - None

- **Jupyter MCP Server**
  - Rating: +
  - Strengths:
    - Server admins could deploy the MCP server directly on the Jupyter Lab server.
    - Multiple agentic tools can use the global config of the MCP client.
  - Weaknesses:
    - Server admins must install MCP-related pip packages on the Jupyter server.
    - User must configure an MCP client in the agentic tool to connect to the Jupyter MCP Server.

- **VS Code Remote**
  - Rating: ++
  - Strengths:
    - Quick setup
  - Weaknesses:
    - None

### Component Replacement Effort

- **Jupyter Lab API**
  - Rating: -
  - Strengths:
    - User could quickly switch to the SSH connection.
  - Weaknesses:
    - User would have to upload their entire code project to the Jupyter Lab server first.

- **Jupyter MCP Server**
  - Rating: +
  - Strengths:
    - User could select another MCP server establishing a connection to Jupyter Lab.
  - Weaknesses:
    - There is no true alternative MCP server.

- **VS Code Remote**
  - Rating: +
  - Strengths:
    - User could quickly switch to the API connection.
  - Weaknesses:
    - User would have to download the notebook file first.
