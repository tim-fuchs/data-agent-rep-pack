# AI Agent

## Purpose

- This folder provides installation and configuration instructions for the AI agent tools.
  - We focus on the desktop and CLI apps of OpenCode, and the VS Code extension Kilo Code.
  - There are also many other open-source agents such as Roo Code and goose.
  - Most of them have very similar installation and configuration options.
- This folder also provides a template project with multiple prompt engineering artifacts to implement the requirements of the agent.

## Install and Configure

### OpenCode (Desktop App, CLI App, VS Code Extension)

- **Installation:**
  - Choose your favorite installation option from the [OpenCode website](https://opencode.ai/download).
  - We recommend installing OpenCode Desktop.
  - We recommend installing OpenCode Terminal as well, as it is practical for quick checks. Also, it is (currently) required for any OAuth processes for MCP servers (but this is not required in our setup).
  - You can also install the OpenCode VS Code extension. It looks like OpenCode Terminal, but within VS Code. The other options offer a better UX (in our opinion).

- **Configure LLM provider:**
  1. Click on the app symbol (OpenCode Desktop) or enter `opencode` in the CLI (OpenCode Terminal) to start the app.
  2. Click on setting symbol (OpenCode Desktop) or use `/connect` command (OpenCode Terminal).
  3. Connect to your prefered provider (e.g., Ollama via `Custom provider` or OpenAI via API key).
     - Note: API keys of providers are stored in `~/.local/share/opencode/auth.json`.

- **Notes on configuration:**
  - The global configuration file for OpenCode is stored in your user directory on your machine (`~/.config/opencode/opencode.json`).
  - You can also override global settings with a project-specific config (`.opencode/opencode.json` in project root).

### Kilo Code (VS Code Extension)

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

## Template Project

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

### Preconfiguration

- The configuration files `.opencode/opencode.json` and `.kilo/kilo.jsonc` contain the configuration of the MCP clients, as well as other settings, such as additional plugins, like the [websearch-cited tool](https://github.com/ghoulr/opencode-websearch-cited).
- Hence, the tools are ready to use. You just have to start the MCP servers first (see instructions in the subdirectories `grounded-docs-mcp`, etc.).

### Run the Project

#### OpenCode

1. Open the `template-project` folder in OpenCode Desktop.
2. Check that the MCP servers are available (green or red indicator on the top right).
3. Prompt, "Which notebooks are available on Jupyter Lab?" with the Plan or Build agent.

#### Kilo Code

1. Open the `templace-project` folder VS Code.
2. Check that the MCP servers are available (Kilo Code settings > `Agent Behavior` > `MCP Servers`).
3. Prompt, "Which notebooks are available on Jupyter Lab?" with the Ask, Plan, or Code agent.

## Further Reads

- [OpenCode docs with instructions for custom agents, skills, commands, tools](https://opencode.ai/docs)
- [Kilo Code docs with instructions for custom agents, skills, commands, tools](https://kilo.ai/docs/customize)
- "Find Skills" Skill:
  - Install [Skills CLI tool](https://github.com/vercel-labs/skills) with `npx skills` to streamline finding and installing external skills.
  - Check out the [skills leaderboard](https://skills.sh).
  - Update installed skills: `npx skills update`
- [Agent Skills website](https://agentskills.io/skill-creation/best-practices)
- [AGENTS.md with Karpathy-inspired Claude Code guidelines](https://github.com/forrestchang/andrej-karpathy-skills)
