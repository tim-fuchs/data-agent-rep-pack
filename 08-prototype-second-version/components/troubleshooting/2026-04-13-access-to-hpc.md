# No Read/Write Access for Notebooks Hosted on HPC Cluster

**Date:** 2026-04-14

## Problem Description

I am running into two very strange and new errors in two ways of connecting to a Jupyter notebook on Maxwell from my local machine.

**The two options are:**

- Via the Jupyter Hub extension of VS Code (see <https://docs.desy.de/maxwell/documentation/miscellaneous/jlab_vscode/>)
- Via the Jupyter MCP server (see <https://jupyter-mcp-server.datalayer.tech>)

I currently experiment with both to read/write/execute notebooks on my Jupyter Lab server on Maxwell from an AI agent on my local machine.
However, the VS Code option could also simply be used to execute a local notebook with a remote Python kernel.

Both options worked until about a week ago, e.g., I could add cells to a remote notebook via MCP or execute the cells of a local notebook in VS Code with the remote kernel.
Now, however, I am running into error messages.

**What (still) works:**

- I can connect via both options to my running Jupyter Lab server (i.e., <https://max-jhub.desy.de/user/USER>).
  - For the VS Code option, I can select from the kernels available on the server.
  - For the MCP option, I received the responses that I was able to connect to the server and to a specific notebook.

**What does not work (anymore):**

- VS Code: Execute notebook cells with a remote kernel. VS Code is running into an infinite loop trying to connect to the kernel.
- MCP: I cannot read/write any data from/to a notebook (that I connected to in the previous step).

## Problem Investigation

**What I already tried to handle the errors:**

- Stop and restart the Jupyter Lab server
- Try different Jupyter Lab tokens that already worked before
- Creating and using new tokens
- Reinstall any related package on my machine

**What I think is the problem:**

- Since I can connect to the server with both options but not execute any read/write/execute options within a notebook, I assume that the server admins adjusted the configuration.
- I read in recent meeting minutes that Landlock was activated on RHEL. I do not know what RHEL is, but Landlock could certainly block commands from my local machine to the Jupyter Server.
