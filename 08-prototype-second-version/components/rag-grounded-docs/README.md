# Grounded Docs MCP Server (Docker Compose)

This folder provides Grounded Docs via Docker Compose.

## Prerequisites

- Docker Desktop (or Docker Engine + Docker Compose plugin)
- A free local port for Grounded Docs (for example, 6280)
- Basic terminal access

Verify Docker is available:

```bash
docker --version
docker compose version
```

## Installing and Running MCP Server

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

## Configuring MCP Client

### Config OpenCode

File location:

- Global: `~/.config/opencode/opencode.json`
- Project: `opencode.json` in project root

File entry:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "grounded-docs": {
      "type": "remote",
      "url": "http://localhost:6280/mcp",
      "enabled": true
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
    "grounded-docs": {
      "type": "remote",
      "url": "http://localhost:6280/mcp",
      "enabled": true,
      "timeout": 15000
    }
  }
}
```

## Notes

- Telemetry of Grounded Docs is explicitly disabled in `docker-compose.yml` via `DOCS_MCP_TELEMETRY=false`.

## References

- [Grounded Docs website](https://grounded.tools)
- [Docs in Grounded Docs GitHub repository](https://github.com/arabold/docs-mcp-server/tree/main/docs)
