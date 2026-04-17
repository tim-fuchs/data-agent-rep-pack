# AI Agent

## Purpose

- This folder provides installation and configuration instructions for the AI agent tools.
- The installation steps focus on the desktop and CLI apps of OpenCode, and the VS Code extension Kilo Code.
  - There are also many other open-source agents such as Roo Code and goose.
  - Most of them have very similar installation and configuration options.
- The configuration steps implement the agent-specific requirements.

## Install

### OpenCode (Desktop App)

### Kilo Code (VS Code Extension)

- **Notes:**
  - Kilo Code settings are available by opening the Kilo Code window in VS Code and clicking on the wheel symbol on the top of the window.
  - The VS Code settings edit the global configuration file for Kilo Code (`~/.config/kilo/kilo.jsonc`).
  - You can also override global settings with a project-specific config (`.kilo/kilo.jsonc` in project root).
  
- Configure LLM provider:

  1. Go to settings > `Providers`.
  2. Connect to your prefered provider via your (e.g., Ollama via `Custom provider` or OpenAI via API key).
  3. Click `Save`.

- Configure directory for skills:

   1. Go to settings > `Agent Behavior` > `Skills` tab.
   2. Add the skills folder path `~/.agents/skills/`.
   3. Click `Save`.

## Configure

### Notes

- Most features of AI agent tools to tweak the agent behavior boil down to prompt engineering.
- This concerns the `AGENTS.md` file, the skills (`SKILL.md` file), custom commands, and custom (sub-)agents.
- These features only differ in their execution triggers.
- We use all of these prompt engineering possibilities to enable the requirements listed below.

### Access Remote Jupyter Lab Server

- Follow instructions in [Jupyter MCP config](../jupyter-mcp/README.md).

### Interact with Notebook Content

- Instruct to use Jupyter MCP in AGENTS.md

### Generate HPC-Optimized Code

- Instruct code conventions in AGENTS.md

### Test Code for Correctness and Safety Risk

- Instruct testing process in AGENTS.md

### Request User Feedback to Guide and Improve Solutions

- Instruct feedback behavior via AGENTS.md

### Adapt Code Style and Explanations to User's Expectations

- Instruct style adaption in AGENTS.md and via a CODE_STYLE directory
- Create an example project, add a CODE_STYLE directory, add a notebook file as example
- Instruct expected explanations in AGENTS.md

### Generate Code Documentation on Project- and Code-Level

- Instruct expected documentation in AGENTS.md
  - Agent should prompt the user for documentation preferences.
  - The prompt should include an option for the CODE_STYLE directory.

### Request Human Approval for Sensitive Actions

- Describe recommended approval configuration via tool settings.
- (Eventually,) instruct use-case-specific instructions for execution environment in AGENTS.md, e.g.:
  - Do not automatically execute heavy-load commands in local environment
  - Do not automatically execute batch jobs

### Access Relevant Context Information Within a Project

- OpenCode and Kilo Code do not require further configuration.
- Both can, in principle, read every file on the local machine (but will request human approval first).
- Both have session-level memory.
- Both auto-compact session information if the context windows is full.
- **Unsure if they have session-overlapping memory** (like GitHub Copilot).

### Decompose a Request into Verifiable Tasks

- Depending on the agent (plan vs. build), LLM (GPT Codex vs. GPT nano), and reasoning level (none vs. high), the tool creates a set of tasks itself.
- Nevertheless, instruct task planning in AGENTS.md to enforce this behavior.

### Work With Up-to-Date Code-Relevant Information

- Instruct to use MCP servers for Grounded Docs, GitHub, GitLab in AGENTS.md

### Close Tasks with Narrative Summaries and Recommended Next Steps

- Instruct closing behavior in AGENTS.md

### Support Responses with Citations, Confidence Levels, or Verification Steps

- Instruct citation and verification behavior in AGENTS.md

### Report Conversations to EuXFEL Staff

- Instruct reporting process in a SKILL.md
- Instruct behavior in AGENTS.md:
  - When task completed, ask user if task summary should be reported.
  - If yes, execute skill.

### Assist in Drafting Scientific Manuscripts

- Instruct drafting process in a SKILL.md

### Recommend Using a Version Control System

- Instruct Git versioning in a SKILL.md:
  - Skill 1: git:init
  - Skill 2: git:commit
- Instruct behavior in AGENTS.md:
  - When user wants to connect to a notebook via Jupyter MCP:
    - Check if Git environment is available on the server (**check if this is possible via Jupyter MCP**).
    - If not, ask user if agent should execute git:init skill.
  - When agent completed a task, ask if agent should execute git:commit skill.
    - If yes and Git environment not available, execute git:init skill beforehand.

### Optimize Latency

- Install the [caveman](https://github.com/JuliusBrussee/caveman) skill.
- Instruct using the caveman skills in lite mode in AGENTS.md.

### Not Share User Data

- Describe configuring local/self-hosted models to avoid third-party data transfer.
- Telemetry:
  - OpenCode does not use telemetry, according to the documents
  - Kilo Code does not provide explicit statements about telemetry.

### Implementation Effort

- This requirement is met by installing a ready-to-use AI agent tool and now only have to configure its behavior via tool settings and prompt engineering.

### Component Replacement Effort

- This requirements is met by installing a popular open-source AI agent tool (e.g., OpenCode, Kilo Code) modeled after another popular (eventually proprietary) tool (e.g., Claude Code, Cursor, Codex), including its architecture, configuration, and extension options.

## Further Reads

- [Leaderboard of popular skills](https://skills.sh)
- [Agent Skills website](https://agentskills.io/skill-creation/best-practices)
- [AGENTS.md with Karpathy-inspired Claude Code guidelines](https://github.com/forrestchang/andrej-karpathy-skills)
