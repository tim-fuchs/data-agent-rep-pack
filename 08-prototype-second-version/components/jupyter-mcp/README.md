# Jupyter MCP Server (Docker Compose)

This folder runs the Jupyter MCP server (streamable HTTP transport) with one command, based on section 2 of the [official standalone provider docs](https://jupyter-mcp-server.datalayer.tech/providers/jupyter-streamable-http-standalone/).

## Prerequisite

Start JupyterLab from the sibling `jupyter-lab` project first.

Create a local environment file for this folder:

```bash
cp .env.example .env
```

Then edit `.env` and set all required values.

If any variable is missing, Docker Compose fails fast with an explicit error.

## Installation and Start

From this folder:

```bash
docker compose up -d
```

The MCP server is exposed at:

- `http://localhost:4040/mcp`

## Verify

```bash
curl -i -H "Authorization: Bearer <your-mcp-token>" http://localhost:4040/mcp
```

Expected result for this plain HTTP probe is `406 Not Acceptable`.
That means the endpoint is reachable and token-auth is accepted; full MCP clients then negotiate the streamable protocol.

## Required `.env` variables

```env
JUPYTER_URL=http://host.docker.internal:8888
JUPYTER_TOKEN=replace-with-your-jupyter-token
MCP_TOKEN=replace-with-your-mcp-token
MCP_PORT=4040
```

## Optional overrides

You can still override values inline when starting:

```bash
MCP_TOKEN=my-mcp-token MCP_PORT=4041 docker compose up -d
```

## Stop

```bash
docker compose down
```
