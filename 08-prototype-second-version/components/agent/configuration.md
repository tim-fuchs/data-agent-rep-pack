# Configuration of System Components

## Agentic AI Component

### General Information on OpenCode Configuration

- Location of global config:
  - `~/.opencode/opencode.json`
  - `~/.config/opencode/`
- Location of project-specific config:
  - `<project>/opencode.json`
  - `<project>/.opencode/`
- Options how to add LLM providers (see [docs](https://opencode.ai/docs/providers)):
  1. Use built-in commands `\connect` or `\model`. API keys of providers will be stored in `~/.local/share/opencode/auth.json`.
  2. Add configuration to `opencode.json`.
- Agent customization options:
  - [(Sub-)Agents](https://opencode.ai/docs/agents/)
  - [Commands](https://opencode.ai/docs/commands/)
  - [Skills](https://opencode.ai/docs/skills/)
  - [Tools](https://opencode.ai/docs/custom-tools/)

### "Find Skills" Skill

- Install [Skills CLI](https://github.com/vercel-labs/skills) with `npx skills` to streamline finding and installing external skills.
- Check out the [skills leaderboard](https://skills.sh).
- Update installed skills: `npx skills update`

### "Caveman" Skill

- Can drastically reduce the length of output prompts and, therefore, also the token consumption.
- See [repo](https://github.com/JuliusBrussee/caveman)
- Install it for "universal agent support" via Skills plugin: `npx skills add JuliusBrussee/caveman`
  - During the process, you can select between global (recommended) or project-specific install.
  - Location of global install: `~/.agents/skills/`
  - Location of project-specific install: `<project>/.opencode/skills/`
- Usage:
  - `/caveman lite|full|ultra` (`lite` recommended for EuXFEL use case)
  - Must be manually activated every session.
    - Small downside of OpenCode in comparison to Claude Code, which can activate it automatically.
    - Adding instructions to the agent system prompt (as explained in the Caveman repo) does not work properly, as system prompt cannot access the skill yet.

### "Websearch-Cited" Tool

- See [repo](https://github.com/ghoulr/opencode-websearch-cited)
- Install via `opencode.json`:
  
  ```json
  {
    "provider": {
      "openai": {
        "options": {
          "websearch_cited": {
            "model": "gpt-5.4-nano"
          }
        }
      }
    },
    ...
    "plugin": [
      "opencode-websearch-cited"
    ]
  }
  ```

## Configuration of Standalone Jupyter MCP Server and MCP Client

- Follow [Step 3](https://jupyter-mcp-server.datalayer.tech/providers/jupyterhub-streamable-http/#3-api-token-configuration) for Jupyter Hub config, which is token creation on Jupyter Hub with the scope `access:servers!server=USER/` (USER is your user name).
- Follow [Step 2 and 3](https://jupyter-mcp-server.datalayer.tech/providers/jupyter-streamable-http-standalone/#2-start-jupyter-mcp-server) for the standalone MCP server to configure start the Jupyter MCP server on your machine and add the server connection to your client, e.g., OpenCode or goose.

  - Commands to start the server (replace `USER` and `TOKEN_JUPYER` with your Jupyter Lab user name and token, and `TOKEN_MCP_CLIENT` with a self-created token that the MCP client must enter to connect):

    ```bash
    source .venv/bin/activate &&
    pip install jupyter-mcp-server &&
    jupyter-mcp-server start \
        --transport streamable-http \
        --mcp-token TOKEN_MCP_CLIENT \
        --jupyter-url https://max-jhub.desy.de/user/USER \
        --jupyter-token TOKEN_JUPYTER \
        --port 4040
    ```

  - MCP client config for [`opencode.json`](https://opencode.ai/docs/mcp-servers) of OpenCode Desktop app (slighty differs from Claude Code config described in the Jupyter MCP Server documentation):

    ```json
    {
        "$schema": "https://opencode.ai/config.json",
        "mcp": {
            "jupyter": {
                "type": "remote",
                "url": "http://127.0.0.1:4040/mcp",
                "enabled": true,
                "headers": {
                    "Authorization": "Bearer TOKEN_MCP_CLIENT"
                }
            }
        },
        "agent": {
            "build": {
                "prompt": "When calling the MCP prompt jupyter_cite, always pass notebook_name as an empty string or 'default' unless the user explicitly provides a connected notebook name. Never pass unresolved placeholders like $1, $2, or $3 as notebook_name."
            }
        }
    }
    ```

    The prompt is there to suppress an internal problem of the interaction between Jupyter MCP Server and OpenCode.
