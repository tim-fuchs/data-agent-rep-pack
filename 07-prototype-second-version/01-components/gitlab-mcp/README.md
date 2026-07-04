# GitLab MCP Server

## Purpose

- This folder provides instructions to connect the AI agent tool to the [GitLab MCP server by zereight](https://github.com/zereight/gitlab-mcp).
- The server enables many possibilities, including creating merge requests with the agent. We, however, focus on the server's read-only tools, as we require it only to read up-to-date code and documentation.

## Prerequisites

- User account on a GitLab instance, e.g., [European XFEL GitLab](https://git.xfel.eu)
- AI agent tool that supports MCP, e.g., OpenCode or Kilo Code
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine + Docker Compose plugin)
- A free local port for GitLab MCP (ideally 3002)
- Basic terminal access

Verify Docker is available:

```bash
docker --version
docker compose version
```

## Install and Run the MCP Server

1. Create a personal access token (PAT) on your GitLab instance:

   - Go to the `Access tokens` section in your user settings: <https://YOUR_GITLAB_INSTANCE/-/user_settings/personal_access_tokens>
   - Click `Add new token` to configure access token:
     - Name and expiration date: whatever you prefer
     - Activate scopes: `read_api`, `read_user`, `read_repository`

2. Create a `.env` file with `cp .env.example .env`.
3. Set environment variables in `.env` (personal access token, GitLab API URL).
4. Start Docker container with: `docker compose up -d`

   - Running endpoint (Streamable HTTP): `http://localhost:3002/mcp`

5. Optionally, view logs: `docker compose logs -f`
6. Optionally, stop container: `docker compose down`

## Configure MCP Client

1. Add the MCP client entry to the config file of your AI agent:

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
       "gitlab-mcp": {
         "type": "remote",
         "url": "http://localhost:3002/mcp",
         "enabled": true
       }
     }
   }
   ```

2. Restart your AI agent.
3. Ready! Prompt your agent to retrieve a repository name via gitlab-mcp.
