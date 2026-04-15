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

## Installation and Start

1. Configure environment variables

   - Create a local environment file for this folder: `cp .env.example .env`
   - Set all required values in `.env`.
   - If any variable is missing, Docker Compose fails fast with an explicit error.

2. Start JupyterLab from the sibling `jupyter-lab` project first.
3. From this folder, execute: `docker compose up -d`

The MCP server is exposed at: `http://localhost:4040/mcp`

## Verify

```bash
curl -i -H "Authorization: Bearer <your-mcp-token>" http://localhost:4040/mcp
```

Expected result for this plain HTTP probe is `406 Not Acceptable`.
That means the endpoint is reachable and token-auth is accepted; full MCP clients then negotiate the streamable protocol.

## Optional overrides

You can still override values inline when starting:

```bash
MCP_TOKEN=my-mcp-token MCP_PORT=4041 docker compose up -d
```

## Stop

```bash
docker compose down
```
