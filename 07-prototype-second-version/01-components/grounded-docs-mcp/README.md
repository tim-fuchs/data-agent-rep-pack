# Grounded Docs MCP Server

## Purpose

- This folder provides the Grounded Docs MCP server via Docker Compose.
- Follow the instructions below to install Grounded Docs and index documents to the vector database.

## Prerequisites

- AI agent tool that supports MCP, e.g., OpenCode or Kilo Code
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine + Docker Compose plugin)
- A free local port for Grounded Docs (ideally 6280)
- [Node.js](https://nodejs.org) (for ingesting documents to Grounded Docs)
- Basic terminal access

Verify Docker is available:

```bash
docker --version
docker compose version
```

## Install and Run the MCP Server

1. Create a `.env` file with: `cp .env.example .env`
2. Optionally, set environment variables in `.env` to activate embedding process. If `OPENAI_API_KEY` and `DOCS_MCP_EMBEDDING_MODEL` are empty, Grounded Docs still starts and uses keyword/FTS search.
3. Start Docker container with: `docker compose up -d`

   - Running endpoints:
     - Web UI: `http://localhost:6280`
     - MCP (Streamable HTTP): `http://localhost:6280/mcp`
     - MCP (SSE fallback): `http://localhost:6280/sse`
   - Location of ingested data: `/data`
   - Location of config file: `/config`

4. Optionally, view logs: `docker compose logs -f`
5. Optionally, stop container: `docker compose down`

Note: Telemetry of Grounded Docs is explicitly disabled in `docker-compose.yml` via `DOCS_MCP_TELEMETRY=false`.

## Configure the MCP Client

**File location Open Code:**

- Global: `~/.config/opencode/opencode.json`
- Project: `opencode.json` in project root

**File location Kilo Code:**

- Global: `~/.config/kilo/kilo.jsonc`
- Project: `.kilo/kilo.jsonc` in project root

**File entry:**

```json
{
  "mcp": {
    "grounded-docs": {
      "type": "remote",
      "url": "http://localhost:6280/mcp",
      "enabled": true
    }
  }
}
```

## Index European XFEL Documentation

- We prepared a list of resources that should be indexed by Grounded Docs.
- Execute `sh index-docs.sh`.
- The resources with be stored in a database in `${HOME}/Library/Application Support/docs-mcp-server`.

## References

- [Grounded Docs website](https://grounded.tools)
- [Docs in Grounded Docs GitHub repository](https://github.com/arabold/docs-mcp-server/tree/main/docs)
