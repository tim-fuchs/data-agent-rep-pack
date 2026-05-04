# Jupyter MCP Server

## Purpose

This folder provides instructions to install a Jupyter MCP server (connected to a local Jupyter Lab server) and configure the corresponding MCP client in an AI agent tool.

## Prerequisites

- AI agent tool that supports MCP, e.g., OpenCode or Kilo Code
- Docker Desktop (or Docker Engine + Docker Compose plugin)
- A free local port for Jupyter MCP (for example, 4040)
- Basic terminal access

Verify Docker is available:

```bash
docker --version
docker compose version
```

## Install and Run the MCP Server

1. Configure environment variables

   - Create a local environment file for this folder: `cp .env.example .env`
   - Set all required values in `.env` (i.e., the Jupyter URL and token).
   - If any variable is missing, Docker Compose fails fast with an explicit error.

2. Start JupyterLab from the sibling `jupyter-lab` project first.
3. From this folder, start the Jupyter MCP server with `docker compose up -d`.

   - The MCP server is exposed at: `http://localhost:4040/mcp`

4. Optionally, verify the running server with `curl -i -H "Authorization: Bearer <your-mcp-token>" http://localhost:4040/mcp`.

   - Expected result for this plain HTTP probe is `406 Not Acceptable`.
   - That means the endpoint is reachable and token-auth is accepted; full MCP clients then negotiate the streamable protocol.

5. Optionally, stop the server again with `docker compose down`.

## Configure the MCP Client

1. Add the MCP client entry to the config file of your AI agent:

   **File location OpenCode:**

   - Global: `~/.config/opencode/opencode.json`
   - Project: `opencode.json` in project root

   **File location Kilo Code:**

   - Global: `~/.config/kilo/kilo.jsonc`
   - Project: `.kilo/kilo.jsonc` in project root

   **File entry:**

   ```json
   {
   "mcp": {
         "jupyter-mcp-local": {
            "type": "remote",
            "url": "http://127.0.0.1:4040/mcp",
            "enabled": true,
            "headers": {
                  "Authorization": "Bearer your-jupyter-mcp-token"
            }
         }
      }
   }
   ```

2. Restart your AI agent.
3. Ready! Prompt your agent to connect to a Jupyter notebook.

## References

- [Jupyter MCP](https://jupyter-mcp-server.datalayer.tech/providers/jupyter-streamable-http-standalone/) (see Section 2)
