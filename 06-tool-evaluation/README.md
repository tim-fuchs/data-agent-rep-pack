# Evaluation of Solutions for Agentic AI System Components

- New vision for the agentic AI system:
  - Users operate their favorite AI agent on their computer (Kilo Code, OpenCode, Claude Code, etc.).
  - EuXFEL hosts various [MCP](https://modelcontextprotocol.io) servers that provide connections to Jupyter Lab, a RAG system, GitHub, GitLab, [Zulip](https://zulip.com), etc.
  - Users can flexibly connect their agent to the servers (plug-and-play).

- Notes about best candidates:
  - We finalized this analysis mid April 2026. Keep this date in mind as the landscape of agentic AI tool evolves fast.
  - Many of the agentic AI tools are (partially) interoperable and offer similar features. A possible reason is that the tool developer analyze the strengths and weaknesses of competitors and want users to migrate to their tool.
  - We chose the tools that would fit best to the requirements of our use case and the opinions of the domain experts we interviewed. Most other candidates would be strong alternatives.

## Relevant Requirements and System Components

The agentic AI system shall ...

| Requirement                                                      | Jupyter | Agent | Zulip | RAG | GitHub/GitLab |
| ---------------------------------------------------------------- | ------- | ----- | ----- | --- | ------------- |
| Access the high-performance computing cluster                    | X       | X     |       |     |               |
| Optimize latency [^1]                                            | X       | X     | X     | X   | X             |
| Not share user data with third parties [^2]                      | X       | X     | X     | X   | X             |
| Require minimal implementation effort                            | X       | X     | X     | X   | X             |
| Require minimal effort to replace components [^3]                | X       | X     | X     | X   | X             |
| Interact with notebook content [^4]                              | X       | X     |       |     |               |
| Decompose a request into verifiable goals                        |         | X     |       |     |               |
| Request human approval to guide and improve solutions            |         | X     |       |     |               |
| Close task with narrative summary and recommended steps          |         | X     |       |     |               |
| Use concise language                                             |         | X     |       |     |               |
| Retrieve up-to-date information [^5]                             |         | X     |       | X   | X             |
| Access relevant context information within a project [^6]        |         | X     |       |     |               |
| Provide citations, confidence levels, and verification steps     |         | X     |       |     |               |
| Generate code optimized for high-performance computing           |         | X     |       |     |               |
| Test code for correctness and safety risks                       |         | X     |       |     |               |
| Request human approval for sensitive actions [^7]                |         | X     |       |     |               |
| Adapt code style and explanations to the user's expectations     |         | X     |       |     |               |
| Generate code documentation on project- and code-level           |         | X     |       |     |               |
| Recommend using a version control system [^8]                    |         | X     |       |     |               |
| Report conversations between user and agent to EuXFEL staff [^9] |         | X     | X     |     |               |
| Assist in drafting scientific manuscripts                        |         | X     |       |     |               |

- [^1] E.g., streamed responses, sub-agents executed in parallel, reasoning depth adjusted to task complexity, caching of prompts and responses, token minimization, threads for multiple users
- [^2] E.g., self-hosted LLMs possible, telemetry control, secured API access
- [^3] E.g., potential vendor lock, available migration workflows
- [^4] E.g. explain/insert/modify/delete cells, create entire notebooks
- [^5] E.g., by retrieving external public and private resources
- [^6] E.g., project files, previous messages, other agent conversation
- [^7] E.g., file deletion or code execution on HPC cluster
- [^8] To ensure code availability and reproducibility of results
- [^9] Only on user demand

## Comparison of Candidates and Selected Candidates

- [Agentic AI tool](01-agent.md): **Kilo Code**
- [HPC integration](02-hpc.md): **Jupyter Lab API**
- [RAG integration](03-rag.md): **Grounded Docs**
- [GitHub and GitLab integration](04-git.md): **GitHub MCP (by GitHub) + GitLab MCP (by zereight)**
- [Zulip integration](05-zulip.md): **ZulipChat MCP**

## Possible Combinations of User Interfaces

| Interface                           | Example                           |
| ----------------------------------- | --------------------------------- |
| Browser tab                         | Jupyter Lab + Jupyter AI          |
| Browser tab + IDE extension         | Jupyter Lab + Roo Code            |
| Browser tab + CLI                   | Jupyter Lab + OpenCode (CLI app)  |
| Browser tab + standalone app        | Jupyter Lab + goose (desktop app) |
| Browser tab + browser tab (desktop) | Jupyter Lab + OpenCode (web app)  |
| Browser tab + browser tab (mobile)  | Jupyter Lab + OpenCode (web app)  |
| IDE + IDE extension                 | VS Code + Kilo Code               |
| IDE + CLI                           | VS Code + goose (CLI app)         |
| IDE + standalone app                | VS Code + OpenCode (desktop app)  |
| IDE + browser tab (desktop)         | VS Code + OpenCode (web app)      |
| IDE + browser tab (mobile)          | VS Code + OpenCode (web app)      |

... + MCP servers (Jupyter, Zulip, RAG, GitHub, GitLab)

## Workflow Automation as Alternative Approach to User-Installed Agentic AI System

<details><summary>Details</summary>

- Possible scenario:
  1. User sends request to agent via Zulip messenger.
  2. Messenger forwards request to agent.
  3. Agent processes the request and can access Jupyter Lab and the RAG component via MCP servers.
  4. Agent reports results to user via Zulip.

- Advantages:
  - Automated logging for user and EuXFEL staff due to Zulip conversation
  - Workflow fully integrated into EuXFEL software environment

- Disadvantages:
  - User cannot access typical features of agentic systems such as agent modes (e.g., plan vs. build), switching between LLMs (e.g., switching to more powerful models).
  - User cannot "bring their own agent (BYOA)" due to the fully integrated workflow. They might already use agentic AI systems (e.g., Claude Code) and would like to continue using them.
  - Developer would have to create and maintain many custom features to address both disadvantages.

- Blockers:
  - Agentic AI systems are usually built as stateful applications to enable multi-turn conversations and memory. Hence, they usually cannot be accessed via API calls. A counterexample is OpenClaw.

- Tool candidates:
  - [n8n](https://github.com/n8n-io/n8n)
  - [activepieces](https://github.com/activepieces/activepieces)
  - [OpenClaw](https://openclaw.ai)

</details>

## References

- [Blog post](https://www.katonic.ai/blog/agent-protocols) comparing the protocols MCP, A2A, ANP, ACP, and AGORA
- [FastMCP](https://gofastmcp.com)
- [FastMCP tutorial](https://www.freecodecamp.org/news/how-to-build-your-first-mcp-server-using-fastmcp) by freeCodeCamp
