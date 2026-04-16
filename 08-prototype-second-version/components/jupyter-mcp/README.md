# Jupyter MCP Server

This folder runs the Jupyter MCP server (streamable HTTP transport) with one command, based on section 2 of the [official standalone provider docs](https://jupyter-mcp-server.datalayer.tech/providers/jupyter-streamable-http-standalone/).

## Prerequisites

- Docker Desktop (or Docker Engine + Docker Compose plugin)
- A free local port for Jupyter MCP (for example, 4040)
- Basic terminal access

Verify Docker is available:

```bash
docker --version
docker compose version
```

## Installing and Running the MCP Server

1. Configure environment variables

   - Create a local environment file for this folder: `cp .env.example .env`
   - Set all required values in `.env`.
   - If any variable is missing, Docker Compose fails fast with an explicit error.

2. Start JupyterLab from the sibling `jupyter-lab` project first.
3. From this folder, start the Jupyter MCP server with `docker compose up -d`.

   - The MCP server is exposed at: `http://localhost:4040/mcp`

4. Optionally, verify the running server with `curl -i -H "Authorization: Bearer <your-mcp-token>" http://localhost:4040/mcp`.

   - Expected result for this plain HTTP probe is `406 Not Acceptable`.
   - That means the endpoint is reachable and token-auth is accepted; full MCP clients then negotiate the streamable protocol.

5. Optionally, stop the server again with `docker compose down`.

## Configuring the MCP Client

### Config OpenCode

File location:

- Global: `~/.config/opencode/opencode.json`
- Project: `opencode.json` in project root

File entry:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
      "jupyter": {
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

### Config Kilo Code

File location:

- Global: `~/.config/kilo/kilo.jsonc`
- Project: `.kilo/kilo.jsonc` in project root

Entry:

```json
{
  "mcp": {
      "jupyter": {
         "type": "remote",
         "url": "http://127.0.0.1:4040/mcp",
         "enabled": true,
         "headers": {
            "Authorization": "Bearer your-jupyter-mcp-token",
         },
      }
   }
}
```
