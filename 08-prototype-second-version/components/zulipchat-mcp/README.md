# Zulip Chat MCP Server

## Purpose

- This folder provides configuration instructions for the [ZulipChat MCP server](https://github.com/akougkas/zulipchat-mcp).
- This server enables your AI agent to send messages to Zulip.
- This is a local MCP server, meaning that you do not have to run a separate server. Instead, you simply have to instruct the MCP client to start the server itself.

## Prerequisites

- AI agent tool that supports MCP, e.g., OpenCode or Kilo Code
- [Zulip](https://zulip.com)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Create a Zulip Bot

1. In Zulip, go to `Settings` > `Personal settings` > `Bot` > `Add a new bot`
2. In the form, detail bot information, and add the bot:
   - Bot type: `Incoming webhook`
   - Name: whatever name you like
   - Bot email: what email you like
3. Download the `zuliprc` file of the bot (it contains the bot email, API key, and Zulip organization).

## Configuring the MCP Client

1. Store the zuliprc file wherever you like on your machine. I recommend the `.agents` folder in your user directory as this folder is used by many AI agents anyway.
2. Add the MCP client entry to the config file of your AI agent:

    **File location Open Code:**

    - Global: `~/.config/opencode/opencode.json`
    - Project: `opencode.json` in project root

    **File location Kilo Code:**

    - Global: `~/.config/kilo/kilo.jsonc`
    - Project: `.kilo/kilo.jsonc` in project root

    **File entry:**

    ```json
    {
        "mcpServers": {
            "zulipchat-mcp": {
            "command": "uvx",
            "args": ["zulipchat-mcp", "--zulip-config-file", "ABSOLUTE_PATH_TO_ZULIPRC/zuliprc"]
            }
        }
    }
    ```

3. Restart your AI agent
4. Ready! Prompt your agent to send a message to Zulip.

## References

- [ZulipChat MCP GitHub Repository](https://github.com/akougkas/zulipchat-mcp)
