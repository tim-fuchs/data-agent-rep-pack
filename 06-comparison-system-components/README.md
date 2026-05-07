# Comparison of Candidates for Components of the Agentic AI System

- New vision for the agentic AI system:
  - Users operate their favorite AI agent on their computer (Kilo Code, OpenCode, Claude Code, etc.).
  - EuXFEL hosts various MCP servers that provide connections to Jupyter Lab, a RAG system, GitHub, GitLab, Zulip, etc.
  - Users can flexibly connect their agent to the servers (plug-and-play).

- Notes about best candidates:
  - First principle when selecting among the candidates: **"Reach users where they are. Do not force them to use your environment and workflows."**
  - We finalized this analysis mid April 2026. Keep this date in mind as the landscape of agentic AI tool evolves fast.
  - Many of the agentic AI tools are (partially) interoperable and offer similar features. A possible reason is that the tool developer analyze the strengths and weaknesses of competitors and want users to migrate to their tool.
  - We chose the tools that would fit best to the requirements of our use case and the opinions of the domain experts we interviewed. Most other candidates would be strong alternatives.

## Relevant Requirements and System Components

The agentic AI system shall ...

| Requirement                                                                | Jupyter | Agent | Zulip | RAG | GitHub/GitLab |
| -------------------------------------------------------------------------- | ------- | ----- | ----- | --- | ------------- |
| Access the remote Jupyter Lab server                                       | X       | X     |       |     |               |
| Interact with notebook content [^1]                                        | X       | X     |       |     |               |
| Generate code optimized for high-performance computing                     |         | X     |       |     |               |
| Test code for correctness and safety risks                                 |         | X     |       |     |               |
| Request user feedback to guide and improve solutions                       |         | X     |       |     |               |
| Adapt code style and explanations to the user's expectations               |         | X     |       |     |               |
| Generate code documentation on project- and code-level                     |         | X     |       |     |               |
| Request human approval for sensitive actions [^2]                          |         | X     |       |     |               |
| Access relevant context information within a project [^3]                  |         | X     |       |     |               |
| Decompose a request into verifiable goals                                  |         | X     |       |     |               |
| Work with up-to-date information [^4]                                      |         | X     |       | X   | X             |
| Close tasks with narrative summaries and recommended next steps            |         | X     |       |     |               |
| Support responses with citations, confidence levels, or verification steps |         | X     |       |     |               |
| Report conversations between user and agent to EuXFEL staff [^5]           |         | X     | X     |     |               |
| Assist in drafting scientific manuscripts                                  |         | X     |       |     |               |
| Recommend using a version control system [^6]                              |         | X     |       |     |               |
| Optimize latency [^7]                                                      | X       | X     | X     | X   | X             |
| Not share user data with third parties [^8]                                | X       | X     | X     | X   | X             |
| Minimize implementation effort                                             | X       | X     | X     | X   | X             |
| Minimize effort required to replace components [^9]                        | X       | X     | X     | X   | X             |

- [^1] E.g. explain/insert/modify/delete cells, create entire notebooks
- [^2] E.g., file deletion or code execution on HPC cluster
- [^3] E.g., project files, previous messages, other agent conversation
- [^4] E.g., by retrieving external public and private resources
- [^5] Only on user demand
- [^6] To ensure code availability and reproducibility of results
- [^7] E.g., streamed responses, sub-agents executed in parallel, reasoning depth adjusted to task complexity, caching of prompts and responses, token minimization, threads for multiple users
- [^8] E.g., self-hosted LLMs possible, telemetry control, secured API access
- [^9] E.g., potential vendor lock, available migration workflows

## Comparison of Candidates and Selected Candidates

- [Jupyter Lab integration](01-comparison-jupyter.md): **Jupyter Lab API**
- [Agentic AI tool](02-comparison-agent.md): **Kilo Code**
- [RAG integration](03-comparison-rag.md): **Grounded Docs**
- [GitHub and GitLab integration](04-comparison-git.md): **GitHub MCP (by GitHub) + GitLab MCP (by zereight)**
- [Zulip integration](05-comparison-zulip.md): **ZulipChat MCP**

## Possible User Interaction Channels

| Interaction Channel                 | Example                           |
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

... + MCP servers (Jupyter, Zulip, RAG, GitHub, GitLab) + nono (local machine and Jupyter Lab server)

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

<details><summary>Details</summary>

## Official Docs of Candidates

- [OpenCode](https://opencode.ai)
- [Kilo Code](https://kilo.ai)
- [goose](https://goose-docs.ai)
- [DeepAgents](https://www.langchain.com/deep-agents)
- [DeepAgents tutorial by LangChain Academy](https://academy.langchain.com/courses/deep-agents-with-langgraph)
- [Jupyter MCP](https://jupyter-mcp-server.datalayer.tech)
- [ZulipChat MCP](https://github.com/akougkas/zulipchat-mcp/tree/main)
- [Grounded Docs MCP](https://grounded.tools)

### Miscellaneous

- [Blog post](https://docs.bswen.com/blog/2026-03-14-kilo-roocode-opencode-comparison) comparing Roo Code, OpenCode, and Kilo Code
- [Zulip](https://zulip.com)
- [MCP protocol](https://modelcontextprotocol.io)
- [Blog post](https://www.katonic.ai/blog/agent-protocols) comparing the protocols MCP, A2A, ANP, ACP, and AGORA
- [FastMCP](https://gofastmcp.com)
- [FastMCP tutorial](https://www.freecodecamp.org/news/how-to-build-your-first-mcp-server-using-fastmcp) by freeCodeCamp

</details>
