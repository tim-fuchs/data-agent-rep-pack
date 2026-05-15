# AI Agent

## Purpose

- This README provides installation and configuration instructions for the agentic tool.
  - We focus on the VS Code extension Kilo Code and the desktop and CLI apps of OpenCode.
  - There are many other open-source agents such as goose and Roo Code.
  - Most of them have very similar installation and configuration options.
- This folder is also a template project with multiple prompt engineering artifacts to implement the requirements of the agent.
  - We reused this folder for every user study session.

## Install and Configure Kilo Code

- **Installation:**
  1. Install the [Kilo Code extension](https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code) within VS Code via the extension marketplace.
  2. Tip for a more GitHub Copilot-like UX: Open the chat window by clicking the chat symbol in the search bar at the top of VS Code. Then, drag the Kilo Code symbol into the chat window.
  
- **Configure LLM provider:**

  1. In VS Code, click on the Kilo Code symbol in the left bar.
  2. In the VS Code extension, go to settings > `Providers`.
  3. Connect to your prefered provider (e.g., Ollama via `Custom provider` or OpenAI via API key).
  4. Click `Save`.

- **Configure directory for skills:**

   1. Go to settings > `Agent Behavior` > `Skills` tab.
   2. Add the skills folder path `~/.agents/skills/`.
   3. Click `Save`.

- **Notes on configuration:**
  - The VS Code settings edit the global configuration file for Kilo Code (`~/.config/kilo/kilo.jsonc`).
  - You can also override global settings with a project-specific config (`.kilo/kilo.jsonc` in project root).

## Agent Project

### Configuration File

- The configuration file `.kilo/kilo.jsonc` contains the configuration of the MCP clients and other settings suchs as auto-approved actions.
- You can add further entries as you like (MCP server, approvals, etc.)

### Prompt Engineering Artifacts

- Most features of AI agent tools to tweak the agent behavior boil down to prompt engineering.
- This concerns the `AGENTS.md` file, the skills (`./agents/skills` folder), custom commands, and custom (sub-)agents.
- These features only differ in their execution triggers.
- In this template project, we make use of an `AGENTS.md` file and, additionally, multiple skills to adapt the agent behavior to the data analysis use case at EuXFEL.

- Note about the [caveman](https://github.com/JuliusBrussee/caveman) skill:
  - It can drastically reduce the length of output prompts and, therefore, also the token consumption.
  - We preconfigured it in the template project, but, in principle, you can also download it via the Skills CLI tool: `npx skills add JuliusBrussee/caveman`
    - During the process, you can select between global (recommended) or project-specific install.
    - Location of global install: `~/.agents/skills/`
    - Location of project-specific install: `<project>/.opencode/skills/`
  - Usage:
    - `/caveman lite|full|ultra` (We recommend `lite` for the EuXFEL use case.)
    - Skill must be manually activated every session.
      - Small downside of OpenCode and Kilo Code in comparison to Claude Code, which can activate it automatically.
      - To automate this, we added the skill activation to the `AGENTS.md`.

### Run the Project

1. Start the MCP servers (see instructions in the subdirectories of [grounded-docs-mcp](../grounded-docs-mcp/README.md), etc.).
2. If open, restart VS Code.
3. Open this folder VS Code.
4. Open the Kilo Code chat window.
5. Check that the MCP servers are available (Kilo Code settings > `Agent Behavior` > `MCP Servers`).
6. Open `extra.ipynb`. Prompt, "What is the purpose of extra.ipynb?" with the Ask, Plan, or Code agent.
7. Prompt, "Which notebooks are available on Jupyter Lab?" with the Ask, Plan, or Code agent.

// TODO add instructions about connecting to remote Jupyter kernel / to Jupyter MCP

## Further Reads

- [Kilo Code docs](https://kilo.ai/docs/customize) with instructions for custom agents, skills, commands, tools
- "Find Skills" Skill:
  - Install [Skills CLI tool](https://github.com/vercel-labs/skills) with `npx skills` to streamline finding and installing external skills.
  - Check out the [skills leaderboard](https://skills.sh).
  - Update installed skills: `npx skills update`
- [Agent Skills website](https://agentskills.io/skill-creation/best-practices)
- [Andrej-Karpathy-Skills](https://github.com/forrestchang/andrej-karpathy-skills) (AGENTS.md with coding instructions)
