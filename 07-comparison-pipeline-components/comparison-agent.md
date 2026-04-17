# Comparison of Candidates for the Agent Component

## Notes

- Considered agentic tools: Kilo Code, OpenCode, goose, Roo Code, Deep Agents, Jupyter AI
- Ratings focus on only on free, open-source features. Premium features, such as KiloClaw by Kilo, are not considered.
- General constraint: The quality of tool output depends strongly on model choice and prompt quality.
- General configuration options:
  - Most tools provide multiple options to configure global and project-level agent workflows.
  - Common examples: `AGENTS.md` files, `SKILL.md` files, custom agents, custom commands
  - Additional possibilities, such as `.goosehints` file (goose) and `rules` directory (Roo Code), are usually near-duplicates that we expect to be removed in future releases.
  - We refer to such possibilities when we say that users can configure a specific behavior.

## Candidates

- **Kilo Code**
  - What:
    - Ready-to-use, model-agnostic agentic AI system ("agent harness")
    - Interactivity:
      - VS Code extension (first class)
      - CLI app
    - Now a fork of OpenCode. Formerly a fork of Roo Code.

- **OpenCode**
  - What:
    - Ready-to-use, model-agnostic agentic AI system ("agent harness")
    - Interactivity:
      - CLI app (first class)
      - Desktop app
      - IDE extension
      - Web app
      - GitHub Actions and GitLab Runners workflow (for issue management)

- **goose**
  - What:
    - Ready-to-use, model-agnostic agentic AI system ("agent harness")
    - Interactivity:
      - CLI app (first class)
      - Desktop app

- **Jupyter AI**
  - What:
    - Extension for Jupyter Lab
    - Built by Jupyter-affiliated developers
    - Does not provide an agent out-of-the-box
    - User can install Jupyternaut agent (authored by the same developers) or install common agents (OpenCode, Claude Code, etc.).
  - Important limitation for our use case:
    - The existing user environment is a remote Jupyter Lab server hosted on the HPC cluster of EuXFEL/DESY.
    - A user cannot access specific configuration files on the server and also cannot install external agents (such as OpenCode) via `npx` commands.
    - A user can only install Jupyternaut via `pip`, but the agent lacks behind OpenCode and others.

- **DeepAgents (by LangChain)**
  - What:
    - Framework to create agentic AI systems
    - Based on LangChain's LangGraph framework
    - Interactivity via local endpoint (reachable via CLI or IDE extension (e.g., Continue))
  - Summarized requirements analysis (arguments are mostly the same across all requirements):
    - Rating: -/--
    - Strengths:
      - User has maximum flexibility to create a tailored agentic AI tool.
    - Weaknesses:
      - User must design, implement, deploy, and maintain the full agent system themselves.

- **Alternative candidates to Kilo Code, OpenCode, goose, Roo Code, Jupyter AI**
  - What do they have in common: ready-to-use, open-source, login-free, model-agnostic agentic AI system ("agent harness")
  - There are further such tools available. The [Agent Skills website](https://agentskills.io/clients) lists many of them. As they are usually similar in features and architecture, we do not list them here explicitly.

- **Alternative candidates to DeepAgents**
  - What do they have in common:
    - They are all frameworks for agentic AI systems.
    - Hence, they provide flexible options to implement a multi-agent workflow.
    - However, implementing this workflow involves an effort that is difficult to estimate.
    - Also, the app that represents the implemented workflow requires manual deployment. Hence, the running app can be reached with a local or remote URI, via CLI or an IDE extension (e.g., Jupyter AI, Continue).
  - [LangGraph (by LangChain)](https://www.langchain.com/langgraph)
    - What: State-focused mult-agent framework. The lower-level base of DeepAgents.
  - [LlamaAgents (by LlamaIndex)](https://developers.llamaindex.ai/python/llamaagents/overview/)
    - What: Multi-agent framework
    - Note: One can use the Agent Builder in LlamaCloud to create (and deploy) an app simply based on a prompt about the agent's purpose. LlamaCloud has a free tier.
  - [CrewAI](https://crewai.com):
    - What: conversation-focused multi-agent framework
  - [MetaGPT](https://docs.deepwisdom.ai/main/en/)
    - What: conversation-focused multi-agent framework with prepared sub-agent personas
  - [Pydantic AI](https://ai.pydantic.dev)
    - What: Python-focused multi-agent framework by Pydantic community
  - [Agent Framework (by Microsoft)](https://learn.microsoft.com/en-us/agent-framework/overview/?pivots=programming-language-csharp):
    - What: multi-agent framework focused a lot on Microsoft environment, including .NET.
  - [Strands (by AWS)](https://strandsagents.com)
    - What: multi-agent framework
  - [OpenAgents](https://openagents.org):
    - What: Framework to create a network of agent systems. Could be an overkill for our use case.
    - See a [blog post](https://openagents.org/blog/posts/2026-02-23-open-source-ai-agent-frameworks-compared) comparing OpenAgent, LangGraph, etc.

- **Irrelevant candidates**
  - [Letta Code](https://docs.letta.com/letta-code)
    - Interactivity: via CLI app
    - Downside: Requires logging in to a free Letta account.
  - GitHub Copilot
    - Requires a paid subscription
    - Is not open-source
  - OpenAI Codex
    - Requires a paid subscription
    - Is not open-source
  - Claude Code
    - Requires a paid subscription
    - Is not open-source

## Requirements Analysis

### Access Remote Jupyter Lab Server

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool can use MCP-provided tools to interact with a notebook stored on the remote server.
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: ++
  - Strengths:
    - Tool can use MCP-provided tools to interact with a notebook stored on the remote server.
  - Weaknesses:
    - None

### Interact with Notebook Content

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool can use MCP-provided tools to interact with a notebook stored on the remote server.
    - Tool can access a locally stored notebook out of the box.
  - Weaknesses:
    - None.

- **Jupyter AI**
  - Rating: ++
  - Strengths:
    - Tool can use MCP-provided tools to interact with a notebook stored on the remote server.
  - Weaknesses:
    - None.

### Generate HPC-Optimized Code

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: +
  - Strengths:
    - User can configure the enforcement of HPC coding conventions.
  - Weaknesses:
    - Tool is not optimized for HPC computing out of the box.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - User can prompt the agent to enforce HPC coding conventions.
  - Weaknesses:
    - Tool is not optimized for HPC computing out of the box.

### Test Code for Correctness and Safety Risk

- **Kilo Code**
  - Rating: +
  - Strengths:
    - Tool has built-in agent workflows for linting and testing.
    - User can configure more detailed workflows.
  - Weaknesses:
    - Tool does not guarantee safety testing out of the box.

- **OpenCode**
  - Rating: +
  - Strengths:
    - Tool has built-in agent workflows for linting and testing.
    - User can configure more detailed workflows.
  - Weaknesses:
    - Tool does not guarantee safety testing out of the box.

- **goose**
  - Rating: +
  - Strengths:
    - Tool has built-in agent workflows for linting and testing.
    - User can configure more detailed workflows.
  - Weaknesses:
    - Tool does not guarantee safety testing out of the box.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool has built-in agent workflows for linting and testing.
    - User can configure more detailed workflows.
  - Weaknesses:
    - Tool does not guarantee safety testing out of the box.

- **Deep Agents**
  - Rating: -
  - Strengths:
    - User can implement agent workflows that enforce linting, testing, and safety scanning.
  - Weaknesses:
    - User must implement this feature first.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - User can prompt the agent for linting, testing, and safety scanning.
  - Weaknesses:
    - Tool has no linting, testing, or safety-scanning workflows out of the box.

### Request User Feedback to Guide and Improve Solutions

- **Kilo Code**
  - Rating: ++
  - Strengths:
    - Tool asks clarification questions and supports iterative approval checkpoints.
    - User can configure feedback behavior through task/todo controls and workflow settings.
  - Weaknesses:
    - Aggressive auto-approval settings can reduce human checkpoints.

- **OpenCode**
  - Rating: ++
  - Strengths:
    - Tool asks clarification questions and supports iterative approval checkpoints.
    - User can configure feedback behavior via planning agents and `AGENT.md`.
  - Weaknesses:
    - None.

- **goose**
  - Rating: +
  - Strengths:
    - Tool can ask follow-up questions and support iterative feedback loops.
    - User can configure feedback behavior through project guidance.
  - Weaknesses:
    - Tool provides fewer built-in planning and approval controls than top alternatives.

- **Roo Code**
  - Rating: ++
  - Strengths:
    - Tool asks clarification questions and supports iterative approval checkpoints.
    - User can configure feedback behavior through modes and permission settings.
  - Weaknesses:
    - User must maintain permission settings carefully to preserve approval checkpoints.

- **Deep Agents**
  - Rating: +
  - Strengths:
    - User can implement explicit human-in-the-loop checkpoints in agent workflows.
    - User can configure when feedback or approval is required before transitions.
  - Weaknesses:
    - Framework does not provide built-in feedback workflows out of the box.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool supports iterative feedback through persistent chat threads.
    - User can prompt the agent to request approval before sensitive actions.
  - Weaknesses:
    - Tool does not provide dedicated planning and approval workflows out of the box.
    - Approval behavior can vary by selected persona and server policy.

### Adapt Code Style and Explanations to User's Expectations

- **Kilo Code**
  - Rating: ++
  - Strengths:
    - User can configure code style and explanation details.
  - Weaknesses:
    - None

- **OpenCode**
  - Rating: ++
  - Strengths:
    - User can configure code style and explanation details.
  - Weaknesses:
    - None

- **goose**
  - Rating: ++
  - Strengths:
    - User can configure code style and explanation details.
  - Weaknesses:
    - None

- **Roo Code**
  - Rating: ++
  - Strengths:
    - User can configure code style and explanation details.
  - Weaknesses:
    - None

- **Deep Agents**
  - Rating: -
  - Strengths:
    - User can implement agent workflow enforce code style and explanation details.
  - Weaknesses:
    - User must implement this feature first.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - User can prompt the tool to follow code style and explanation details.
  - Weaknesses:
    - User must specify code style and explanation details each session.

### Generate Code Documentation on Project- and Code-Level

- **Kilo Code**
  - Rating: ++
  - Strengths:
    - Tool can generate project-level and inline code documentation.
    - User can configure documentation behavior through instruction files, skills, and subagents.
  - Weaknesses:
    - Output quality depends on prompt quality and selected model.

- **OpenCode**
  - Rating: ++
  - Strengths:
    - Tool can generate project-level and inline code documentation.
    - User can configure documentation behavior via `AGENT.md` and reusable commands/skills.
  - Weaknesses:
    - None.

- **goose**
  - Rating: +
  - Strengths:
    - Tool can generate project-level and inline code documentation.
    - User can configure documentation behavior through project guidance.
  - Weaknesses:
    - Tool does not enforce documentation standards out of the box.

- **Roo Code**
  - Rating: ++
  - Strengths:
    - Tool can generate project-level and inline code documentation.
    - User can configure documentation behavior through custom rules and modes.
  - Weaknesses:
    - Documentation consistency depends on project-specific configuration.

- **Deep Agents**
  - Rating: +
  - Strengths:
    - User can implement agent workflows for project-level and inline code documentation.
    - User can configure documentation templates and quality checks.
  - Weaknesses:
    - User must implement this feature first.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool can generate notebook narratives and inline code documentation.
    - User can prompt the agent for project-level and code-level documentation content.
  - Weaknesses:
    - Tool does not enforce project-wide documentation standards out of the box.

### Request Human Approval for Sensitive Actions

- **Kilo Code**
  - Rating: +
  - Strengths:
    - Tool can request human approval for sensitive actions through granular permission controls.
    - Tool can check execution-environment assumptions through shell commands.
  - Weaknesses:
    - Default permission settings can remain permissive unless user hardens policy.

- **OpenCode**
  - Rating: +
  - Strengths:
    - User can configure approval levels for sensitive actions through agent permission controls.
    - Tool can check execution-environment assumptions through shell commands.
  - Weaknesses:
    - Tool is not sandboxed out of the box; host-level guardrails are recommended.

- **goose**
  - Rating: +
  - Strengths:
    - Tool can request human approval for sensitive actions through permission prompts.
    - Tool can check execution-environment assumptions through shell commands.
  - Weaknesses:
    - Permission and environment controls are less granular than in tools with richer policy layers.

- **Roo Code**
  - Rating: ++
  - Strengths:
    - Tool can request human approval for sensitive actions through strong action-gating controls.
    - Tool can check execution-environment assumptions through shell commands.
  - Weaknesses:
    - Safety posture depends on correct user/admin configuration.

- **Deep Agents**
  - Rating: -
  - Strengths:
    - User can implement explicit human approval checkpoints in custom workflows.
  - Weaknesses:
    - Framework does not provide built-in approval and sandbox workflows out of the box.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool can request human approval for sensitive actions through persona permission flows.
    - Tool can check execution-environment assumptions through shell commands.
  - Weaknesses:
    - Approval behavior can vary by selected persona and server policy.
    - Some personas may not request permissions consistently.

### Access Relevant Context Information Within a Project

- **Kilo Code**
  - Rating: ++
  - Strengths:
    - Tool maintains context across conversation turns, files, and resumable sessions.
    - User can compact long context to reduce token load.
  - Weaknesses:
    - Very large contexts still require active context management by user.

- **OpenCode**
  - Rating: ++
  - Strengths:
    - Tool maintains context across conversation turns, files, and project sessions.
    - User can create, resume, and compact sessions.
  - Weaknesses:
    - None.

- **goose**
  - Rating: +
  - Strengths:
    - Tool maintains context across conversation turns and active workflows.
    - Tool can read project files on demand to refresh context.
  - Weaknesses:
    - Tool provides weaker long-horizon session controls than stronger session-centric alternatives.

- **Roo Code**
  - Rating: ++
  - Strengths:
    - Tool maintains context across conversation turns, files, and sessions.
    - User can manage long-running context through modes and workflow controls.
  - Weaknesses:
    - Context quality can degrade in very long sessions without active curation.

- **Deep Agents**
  - Rating: ++
  - Strengths:
    - Framework supports explicit state persistence and context routing across agent nodes.
    - User can implement long-horizon context management in workflow design.
  - Weaknesses:
    - Session continuity depends on how the framework application is implemented.

- **Jupyter AI**
  - Rating: ++
  - Strengths:
    - Tool stores chats as `.chat` files and supports chat resumption.
    - Tool supports multiple chat threads with file and cell attachments.
  - Weaknesses:
    - Tool can load large chats slowly, according to troubleshooting guidance.

### Decompose a Request into Verifiable Tasks

- **Kilo Code**
  - Rating: ++
  - Strengths:
    - Tool can decompose requests into verifiable subtasks through delegated subagents.
    - Tool provides a task todo list for checkable subtasks.
  - Weaknesses:
    - Decomposition quality depends on model and prompt quality.

- **OpenCode**
  - Rating: ++
  - Strengths:
    - Tool can decompose requests into verifiable subtasks through built-in planning agents.
    - User can configure dedicated planning agents and verification steps.
  - Weaknesses:
    - None.

- **goose**
  - Rating: +
  - Strengths:
    - Tool can decompose requests into iterative steps and execute checks between steps.
    - User can configure decomposition behavior through project guidance.
  - Weaknesses:
    - Tool provides fewer built-in planning and decomposition controls than top alternatives.

- **Roo Code**
  - Rating: ++
  - Strengths:
    - Tool can decompose requests through mode-driven and structured multi-step workflows.
    - Tool supports verification through task-oriented execution and review loops.
  - Weaknesses:
    - Decomposition quality depends on configuration quality and model choice.

- **Deep Agents**
  - Rating: ++
  - Strengths:
    - Framework is purpose-built for explicit decomposition into graph steps and specialist agents.
    - User can enforce verification gates between steps.
  - Weaknesses:
    - User must design and maintain the decomposition architecture.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - User can prompt stepwise execution and verify results in notebook cells.
    - Notebook tools support iterative decomposition through executable operations.
  - Weaknesses:
    - Tool does not provide a dedicated planning mode with explicit verifiable task lists.
    - Managed EuXFEL setup limits persona extensibility for decomposition workflows.

### Work With Up-to-Date Code-Relevant Information

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool can fetch internet data out of the box.
    - User can configure MCP clients for more specialized information (e.g., RAG for private files).
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - Tool can fetch internet data out of the box.
  - Weaknesses:
    - User cannot configure MCP clients on the remote server.

### Close Tasks with Narrative Summaries and Recommended Next Steps

- **Kilo Code**
  - Rating: +
  - Strengths:
    - Tool can report results with narrative summaries and recommended next steps.
    - User can configure report structure through instructions and skills.
  - Weaknesses:
    - Tool does not enforce standardized reporting templates out of the box.

- **OpenCode**
  - Rating: ++
  - Strengths:
    - Tool can report results with narrative summaries and recommended next steps.
    - User can configure reporting behavior via `AGENTS.md`.
  - Weaknesses:
    - None.

- **goose**
  - Rating: +
  - Strengths:
    - Tool can report results with narrative summaries and recommended next steps.
    - User can configure report structure through prompts and project guidance.
  - Weaknesses:
    - Tool does not enforce standardized reporting templates out of the box.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool can report results with narrative summaries and recommended next steps.
    - User can configure report consistency through custom rules.
  - Weaknesses:
    - Reporting consistency depends on project-specific configuration.

- **Deep Agents**
  - Rating: +
  - Strengths:
    - User can implement reporting nodes for narrative summaries and recommended next steps.
    - User can configure output schemas to match organizational reporting style.
  - Weaknesses:
    - Framework does not provide built-in reporting workflows out of the box.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool can report results with narrative summaries in chat and notebook outputs.
    - User can prompt explicit recommendations for next steps.
  - Weaknesses:
    - Tool does not enforce standardized reporting templates out of the box.

### Support Responses with Citations, Confidence Levels, or Verification Steps

- **Kilo Code**
  - Rating: +
  - Strengths:
    - Tool can report verification steps through testing and review workflows.
    - User can configure external-source access through browser automation and MCP integrations.
  - Weaknesses:
    - Tool does not consistently provide citations or confidence scores out of the box.

- **OpenCode**
  - Rating: +
  - Strengths:
    - Tool can report supporting citations through web-search plugins.
  - Weaknesses:
    - Tool does not consistently provide citations or confidence scores out of the box.

- **goose**
  - Rating: -
  - Strengths:
    - User can prompt the tool to provide verification steps.
  - Weaknesses:
    - Tool does not provide robust citation or confidence reporting out of the box.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool can provide verification steps and source references when prompted.
    - User can configure external tools to ground outputs.
  - Weaknesses:
    - Tool does not consistently provide citations or confidence scores out of the box.

- **Deep Agents**
  - Rating: -
  - Strengths:
    - User can implement citation, confidence, and verification outputs in custom pipelines.
  - Weaknesses:
    - Framework does not provide built-in citation or confidence reporting out of the box.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - Tool can provide verification steps and execute checks within notebook workflows.
  - Weaknesses:
    - Tool does not consistently provide citations or confidence scores out of the box.
    - Citation and confidence behavior depends strongly on model and prompt quality.

### Report Conversations to EuXFEL Staff

- **Kilo Code**
  - Rating: +
  - Strengths:
    - Tool can share conversation history through session links and resumable/forkable sessions.
    - User can configure reporting workflows using stored session history.
  - Weaknesses:
    - Tool does not provide built-in staff-reporting workflows out of the box.

- **OpenCode**
  - Rating: +
  - Strengths:
    - Tool can share conversation history through `/share` and session artifacts.
    - User can configure reporting via storing local files or sending messages via MPC connections.
  - Weaknesses:
    - Tool does not provide built-in staff-reporting workflows out of the box.
    - Share links are public and require governance in sensitive settings.

- **goose**
  - Rating: -
  - Strengths:
    - User can implement manual reporting through exported logs and custom scripts.
  - Weaknesses:
    - Tool does not provide built-in staff-reporting workflows out of the box.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool can share or export conversation history depending on workflow configuration.
    - User can configure reporting integrations through external tools.
  - Weaknesses:
    - Tool does not provide robust built-in staff-reporting workflows out of the box.

- **Deep Agents**
  - Rating: -
  - Strengths:
    - User can implement staff-reporting pipelines through graph nodes (files, APIs, messaging).
  - Weaknesses:
    - Framework does not provide built-in staff-reporting workflows out of the box.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool stores chat history as workspace files for manual handoff and reporting.
    - Tool supports shared review through collaborative chats in one Jupyter environment.
  - Weaknesses:
    - Tool does not provide built-in automated staff-reporting workflows out of the box.

### Assist in Drafting Scientific Manuscripts

- **Kilo Code**
  - Rating: +
  - Strengths:
    - Tool can draft and revise scientific manuscript sections.
    - User can configure structure, tone, and constraints through instruction layers.
  - Weaknesses:
    - Tool is not specialized for scientific-writing quality assurance out of the box.

- **OpenCode**
  - Rating: +
  - Strengths:
    - Tool can draft and revise scientific manuscript sections.
    - User can configure manuscript workflows through commands, skills, and `AGENT.md`.
  - Weaknesses:
    - Tool is not specialized for scientific-writing quality assurance out of the box.
    - User must verify citation quality and domain accuracy.

- **goose**
  - Rating: +
  - Strengths:
    - Tool can draft and revise scientific manuscript sections.
    - User can configure writing constraints through project guidance.
  - Weaknesses:
    - Tool is not specialized for scientific-writing quality assurance out of the box.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool can draft and revise scientific manuscript sections.
    - User can configure writing format and structure through custom guidance.
  - Weaknesses:
    - Tool is not specialized for scientific-writing quality assurance out of the box.
    - User must verify citation quality and domain accuracy.

- **Deep Agents**
  - Rating: +
  - Strengths:
    - User can implement agent workflows for scientific manuscript drafting and review.
    - User can configure domain resources and validation stages.
  - Weaknesses:
    - Framework does not provide built-in scientific-writing workflows out of the box.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool can draft and revise scientific manuscript sections in notebook workflows.
    - User can prompt the agent to mix narrative text with equations, code, and outputs.
  - Weaknesses:
    - Tool is not specialized for scientific-writing quality assurance out of the box.
    - User must verify citation quality and domain accuracy.

### Recommend Using a Version Control System

- **Kilo Code**
  - Rating: +
  - Strengths:
    - Tool supports Git workflows and commit-oriented operations.
    - User can configure commit-related outputs and workflows.
  - Weaknesses:
    - Tool does not consistently recommend version-control usage out of the box.

- **OpenCode**
  - Rating: +
  - Strengths:
    - Tool supports Git workflows and commit preparation.
    - User can configure commit automation via `AGENTS.md`, skills, and commands.
  - Weaknesses:
    - Tool does not consistently recommend version-control usage out of the box.

- **goose**
  - Rating: +
  - Strengths:
    - Tool supports Git workflows and commit preparation.
    - User can configure reproducibility and VCS guidance through prompts.
  - Weaknesses:
    - Tool does not consistently recommend version-control usage out of the box.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool supports Git workflows and commit assistance.
    - User can configure repository-discipline guidance through rules.
  - Weaknesses:
    - Tool does not consistently recommend version-control usage out of the box.

- **Deep Agents**
  - Rating: -
  - Strengths:
    - User can implement Git checks and commit policies as explicit workflow steps.
  - Weaknesses:
    - Framework does not provide built-in version-control recommendation behavior out of the box.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - Tool can interact with repository content through ecosystem components.
  - Weaknesses:
    - Tool does not consistently recommend version-control usage out of the box.
    - Built-in commit and governance UX is limited compared to dedicated coding tools.

### Optimize Latency

- **Kilo Code**
  - Rating: +
  - Strengths:
    - Tool supports latency optimization through streaming and delegated subagents.
    - User can configure model choice for speed and cost trade-offs.
  - Weaknesses:
    - Latency behavior can vary when connected to the remote Jupyter Lab server.

- **OpenCode**
  - Rating: ++
  - Strengths:
    - Tool supports latency optimization through streaming and built-in subagents.
    - User can configure token minimization through available plugins.
  - Weaknesses:
    - None.

- **goose**
  - Rating: +
  - Strengths:
    - Tool supports latency optimization through responsive iterative workflows.
    - User can configure model choice and command workflows to reduce cycle time.
  - Weaknesses:
    - Tool provides fewer built-in latency controls than top alternatives.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool supports latency optimization through streaming and efficient IDE integration.
    - User can configure cloud execution pathways for selected concurrency scenarios.
  - Weaknesses:
    - Local parallel subagent behavior is more constrained than in specialized harnesses.

- **Deep Agents**
  - Rating: +
  - Strengths:
    - Framework supports latency optimization through parallel graph branches.
    - User can configure reasoning depth and tool-routing strategies.
  - Weaknesses:
    - Low-latency performance requires significant workflow engineering.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool supports real-time collaborative chat workflows for iterative work.
    - Tool and notebook are stored on the same server.
  - Weaknesses:
    - Tool has known chat-loading latency issues.
    - Baseline Jupyternaut setup does not provide strong parallel subagent orchestration.

### Not Share User Data

- **Kilo Code**
  - Rating: -
  - Strengths:
    - Tool supports local models and BYOK options.
  - Weaknesses:
    - Tool does not provide a strong no-third-party guarantee out of the box.
    - Session data and provider processing can still involve third parties.

- **OpenCode**
  - Rating: ++
  - Strengths:
    - Tool can avoid third-party data transfer through local/self-hosted model endpoints.
    - Tool reports no telemetry according to official statements and public discussions.
  - Weaknesses:
    - None.

- **goose**
  - Rating: +
  - Strengths:
    - Tool can reduce third-party data transfer through local/self-hosted provider choices.
    - User can run workflows without mandatory cloud-only routing.
  - Weaknesses:
    - Privacy guarantees depend on chosen providers and runtime setup.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool can reduce third-party data transfer through local/self-hosted model pathways.
    - User can configure provider choices to reduce external exposure.
  - Weaknesses:
    - Privacy and telemetry posture is less strict than in fully local-first tools.

- **Deep Agents**
  - Rating: ++
  - Strengths:
    - Framework can avoid third-party data transfer through fully self-hosted deployment.
    - User can configure all data paths in custom deployment architecture.
  - Weaknesses:
    - Misconfigured deployments can still leak data through selected providers or observability tooling.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - Tool can reduce third-party data transfer through local/self-hosted model routes.
    - Design principles emphasize explicit prompting and transparency.
  - Weaknesses:
    - Tool does not provide a strong no-third-party guarantee out of the box.
    - Managed remote JupyterHub setups can limit control over server-side data paths and policy.

### Implementation Effort

- **Kilo Code**
  - Rating: +
  - Strengths:
    - Tool provides ready-to-use agentic workflows with moderate setup effort.
    - User can onboard with broad documentation and straightforward setup paths.
  - Weaknesses:
    - Fully free operation requires additional model configuration.

- **OpenCode**
  - Rating: +
  - Strengths:
    - Tool provides ready-to-use agentic workflows with moderate setup effort.
    - User can configure extensions through `AGENTS.md`, skills, commands, tools, and MCP.
    - Tool has detailed documentation and active OSS maintenance.
  - Weaknesses:
    - Advanced setup options can increase onboarding complexity.
    - Native Windows support limitations can increase setup friction.

- **goose**
  - Rating: +
  - Strengths:
    - Tool provides ready-to-use workflows with moderate setup effort.
    - User can run common coding workflows without custom orchestration code.
  - Weaknesses:
    - Advanced enterprise-style workflows require additional configuration and integration.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool provides ready-to-use VS Code-centered workflows with moderate setup effort.
    - User can configure progressively deeper customization without building a framework app.
  - Weaknesses:
    - Rich feature surface can increase setup and governance complexity.

- **Deep Agents**
  - Rating: --
  - Strengths:
    - Framework provides maximum flexibility for tailored systems.
  - Weaknesses:
    - User must design, implement, and deploy the full agent system.
    - Maintenance burden is significantly higher than in ready-to-use tools.

- **Jupyter AI**
  - Rating: --
  - Strengths:
    - If preinstalled by admins, basic end-user chat workflow is straightforward.
  - Weaknesses:
    - Tool requires extra packages and configuration for many features.
    - Tool may require server restarts and admin-level control for setup changes.
    - Managed EuXFEL restrictions increase setup and extension effort.

### Component Replacement Effort

- **Kilo Code**
  - Rating: ++
  - Strengths:
    - Tool supports component exchange through MCP plus project/global configuration controls.
    - User can reuse interoperable instruction and skill patterns (`AGENTS.md`, skill directories).
  - Weaknesses:
    - Migration still requires adapting tool-specific configuration schema.

- **OpenCode**
  - Rating: ++
  - Strengths:
    - Tool supports component exchange through MCP and transferable instruction patterns.
    - User can reuse familiar skills and command structures across systems.
  - Weaknesses:
    - Migration still requires adapting OpenCode-specific MCP configuration details.

- **goose**
  - Rating: +
  - Strengths:
    - Tool supports component exchange through modular integrations and model/provider interchange.
    - User can configure extensions through guidance and external tooling.
  - Weaknesses:
    - Some extensions remain goose-specific and require adaptation during migration.

- **Roo Code**
  - Rating: ++
  - Strengths:
    - Tool supports component exchange through MCP and customizable behavior layers.
    - User can reuse many cross-ecosystem instruction and tool patterns.
  - Weaknesses:
    - Migration still requires mapping Roo-specific configuration details.

- **Deep Agents**
  - Rating: +
  - Strengths:
    - Framework supports component exchange through modular graph nodes and services.
    - User can integrate heterogeneous tools and protocols with high flexibility.
  - Weaknesses:
    - Component interchangeability is powerful but implementation-heavy in practice.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - Tool supports component exchange through ACP/MCP and custom personas.
  - Weaknesses:
    - Extensibility usually requires package installation, configuration control, and server restart permissions.
    - Managed remote JupyterHub setups increase friction for adding or exchanging components.
