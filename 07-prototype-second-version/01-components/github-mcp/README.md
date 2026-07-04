# GitHub MCP Server

## Purpose

- This folder provides instructions to connect the AI agent tool to the [official MCP server of GitHub](https://github.com/github/github-mcp-server).
- The instructions focus on connecting to the remote MCP server hosted at GitHub, not to the local one hosted on your machine.
- The server enables many possibilities, including creating pull requests with the agent. We, however, focus on the server's read-only mode, as we require it only to read up-to-date code and documentation.

## Prerequisites

- Access to a GitHub account
- AI agent tool that supports MCP, e.g., OpenCode or Kilo Code
- Basic terminal access

## Configure the MCP Client

1. Create a personal access token (PAT) on GitHub

   - Go to the [GitHub Developer Settings](https://github.com/settings/developers)
   - Generate a new fine-grained token
     - Name and expiration date: whatever you prefer
     - Repository access: Public repositories (sufficient for the European XFEL use case)

2. In your root directory of your user, create a `github-mcp-pat` file in the (new) directory `.secrets`, and add your PAT to the file:

   ```bash
   printf "%s" "YOUR_GITHUB_PAT" > ~/.secrets/github-mcp-pat
   chmod 600 ~/.secrets/github-mcp-pat
   ```

   - You can store the PAT wherever you like. The `.secrets` directory is just an example. A separate file instead of the typical `.env` file is required as Kilo Code and the desktop version of OpenCode cannot access environment variables (at least when not started via the CLI).
   - Make sure there is no trailing line in the file.
   - The `chmod 600` commands restricts read/write access to your own user.

3. Add entry to the config file:

   - **File location Open Code:**
     - Global: `~/.config/opencode/opencode.json`
     - Project: `opencode.json` in project root
   - **File location Kilo Code:**
     - Global: `~/.config/kilo/kilo.jsonc`
     - Project: `.kilo/kilo.jsonc` in project root
   - **File entry:**

     ```json
     {
       "mcp": {
         "github-mcp": {
            "type": "remote",
            "url": "https://api.githubcopilot.com/mcp/x/all/readonly",
            "enabled": true,
            "headers": {
                "Authorization": "Bearer {file:~/.secrets/github-mcp-pat}"
            }
         }
       }
     }
     ```

   - **Note:** The `.../readonly` URL restricts the server to read-only access. Use `https://api.githubcopilot.com/mcp/` if you also require write access.

## References

- [Tutorial for creating a PAT on GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)
- [Configuration details for the GitHub MCP server](https://github.com/github/github-mcp-server/blob/main/docs/server-configuration.md)
