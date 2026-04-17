# GitLab MCP Server

## Troubleshooting

- The GitLab instance of EuXFEL either has not [GitLab Duo or experimental tools enabled](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server_troubleshooting/#404-not-found-when-starting-the-gitlab-mcp-server). Hence, access via the official GitLab MCP server is not possible.
- Using the [GitLab MCP server by PolyMCP](https://github.com/poly-mcp/GitLab-MCP-Server) does not work due to internal bugs in the project.
- Hence, at the moment, we cannot establish a connection to GitLab via MCP.

## Purpose

- This folder provides instructions to connect the AI agent tool to the [official MCP server of GitLab](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/).
- The instructions focus on connecting to the remote MCP server hosted at GitLab, not to the local one hosted on your machine.
- The server enables many possibilities, including creating merge requests with the agent. We, however, focus on the server's read-only tools, as we require it only to read up-to-date code and documentation.

## Prerequisites

- User account on a GitLab instance, e.g., [EuXFEL GitLab](https://git.xfel.eu)
- GitLab must have [GitLab Duo and experimental features](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/#prerequisites) turned on.
- Basic terminal access

## Configure the MCP Client

1. Add entry to the config file:

   - **File location Open Code:**
     - Global: `~/.config/opencode/opencode.json`
     - Project: `opencode.json` in project root
   - **File location Kilo Code:**
     - Global: `~/.config/kilo/kilo.jsonc`
     - Project: `.kilo/kilo.jsonc` in project root
   - **File entry:**

     ```json
     {
       "mcpServers": {
         "gitlab-mcp": {
           "type": "http",
           "url": "https://YOUR_GITLAB_INSTANCE/api/v4/mcp"
         }
       }
     }
     ```

2. Start the authentication process via the OpenCode CLI app: `opencode mcp auth gitlab-mcp`
