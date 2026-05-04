# Applicability of nono

- Running OpenCode with the connected MCP servers was not possible via this nono command:

  ```bash
   nono run --profile opencode --allow-cwd --allow ~/.local/bin -- opencode
  ```

- With `--allow ~/.local/bin`, my aim was to allow the `uvx` command that is required to start the local ZulipChat MCP server.
- Besides that, I receive an error message when the GitHub MCP server config is placed in `opencode.json`, as nono does not permit access to the `github-mcp-pat` file (also not with `allow ~/.secrets`).

- Solution:
  - Potentially, there is a solution for this problem.
  - However, at the moment, the effort is higher than the value, as nono can help only with restricting the agent to access to local files, not to files on the Jupyter Lab server.
