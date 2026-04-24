# Agent Setup Options for the User Study Sessions

## 1. Kilo Code + Local VS Code + Remote Kernel

1. SSH into Maxwell (+ forward the Jupyter Lab port to port 8888 on my machine (relevant for step 3)): `ssh -L 8888:localhost:45123 max-exfl-display.desy.de`
2. Load current EuXFEL Python module `module load exfel exfel-python/202601`
3. Start Jupyter with fixed token: `jupyter lab --no-browser --ip 0.0.0.0 --port 45123 --IdentityProvider.token="your-secure-jlab-token"`
4. (Optional) check if Jupyter Lab is available: <http://localhost:8888/lab?token=your-secure-jlab-token>
5. In VS Code, open a local notebook, click the kernel selection button, add the Jupyter Lab as remote Jupyter Lab server:
   - Name: `Local Maxwell`
   - URL: `http://localhost:8888/lab?token=your-secure-jlab-token`

Kilo Code version: `7.2.20`

## 2. OpenCode + Remote VS Code

**Note:** Did not work properly

1. SSH into Maxwell (+ forward the Jupyter Lab port to port 8888 on my machine (relevant for step 3)): `ssh -L 8888:localhost:45123 max-exfl-display.desy.de`
2. Load current EuXFEL Python module `module load exfel exfel-python/202601`
3. Install pip packages required for Jupyter MCP Server:

   ```bash
   pip install 'jupyterlab>=4.4.1' 'jupyter-collaboration>=4.0.2' 'jupyter-mcp-tools>=0.1.4' ipykernel && \
   pip uninstall -y pycrdt datalayer_pycrdt && \
   pip install 'datalayer_pycrdt>=0.12.17'
   ```

   Note: The uninstall was actually not possible due to missing permission.

4. Start Jupyter with fixed token: `jupyter lab --no-browser --ip 0.0.0.0 --port 45123 --IdentityProvider.token="your-secure-jlab-token"`
5. (Optional) check if Jupyter Lab is available: <http://localhost:8888/lab?token=your-secure-jlab-token>
6. Start `jupyter-mcp-local` container (should point to `http://localhost:8888/lab?token=your-secure-jlab-token`).
7. Start VS Code. Start remote session to Maxwell. Open a notebook.
8. Do this once: Add `jupyter-mcp-local` client to OpenCode config:

   ```bash
   jupyter-mcp-server start \
   --transport streamable-http \
   --jupyter-url http://localhost:8888 \
   --jupyter-token your-secure-jlab-token \
   --mcp-token ${MCP_TOKEN} \
   --port 4040
   ```

9. Start OpenCode. Check that the Prompt it to connect to the same notebook.

Why it did not work:

- Despite updating the collaboration package, it sends collaboration-related 404 responses when prompting it to execute notebook cells:

  ```bash
  use_notebook succeeds, but all cell ops fail with same error:
  404... /api/collaboration/session/extradata.ipynb
  Means MCP cannot open notebook collaboration session, so I cannot run execute_cell from
  ```

- But it can run all cells by misusing `jupyter nbcovert`: It converts the notebook into a notebook and executes the cells during the process. This is a workaround, but not a good one.
