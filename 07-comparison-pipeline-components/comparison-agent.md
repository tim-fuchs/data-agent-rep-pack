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
    - A user can only install Jupyternaut via `pip`, but the agent lacks behind the server-based capabilities of OpenCode and others.

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
      - Tool is less interoperatable with other agentic AI tools. Agent is rather embedded in code or available as HTTP endpoint than a standalone tool, like the other tools.

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
    - Tool can use an MCP server to connect to a remote server.
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: ++
  - Strengths:
    - Tool is running on the remote server.
  - Weaknesses:
    - None

### Interact with Notebook Content

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool can use an MCP server to interact with a notebook stored on the remote server.
    - Tool can interact with a locally stored notebook that is connected to a remote kernel.
  - Weaknesses:
    - None.

- **Jupyter AI**
  - Rating: ++
  - Strengths:
    - Tool uses an MCP server out-of-the-box to interact with a notebook stored on the remote server.
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
    - User must instruct the agent every session.

### Test Code for Correctness and Safety Risk

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: +
  - Strengths:
    - Tool has built-in agent workflows for linting and testing.
    - User can configure more detailed workflows.
  - Weaknesses:
    - Tool does not guarantee safety testing out of the box.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - User can prompt the agent for linting, testing, and safety scanning.
  - Weaknesses:
    - Tool has no linting, testing, or safety-scanning workflows out of the box.
    - User must instruct the agent every session.

### Request User Feedback to Guide and Improve Solutions

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool asks clarification questions and supports iterative approval checkpoints.
    - Tool provides planning mode focused on planning the solution before starting the implementation.
    - User can configure feedback behavior.
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - Tool asks clarification questions and supports iterative approval checkpoints.
  - Weaknesses:
    - Tool does not provide dedicated planning and approval workflows out of the box.

### Adapt Code Style and Explanations to User's Expectations

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - User can configure code style and explanation details.
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - User can prompt the tool to follow code style and explanation details.
  - Weaknesses:
    - User must instruct the agent every session.

### Generate Code Documentation on Project- and Code-Level

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool generates (a certain level of) project-level and inline code documentation out of the box.
    - User can configure documentation behavior.
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool generates (a certain level of) project-level and inline code documentation out of the box.
    - User can prompt the agent for project-level and code-level documentation content.
  - Weaknesses:
    - User must instruct the agent every session.

### Request Human Approval for Sensitive Actions

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: +
  - Strengths:
    - Tool has built-in approval workflow for sensitive actions.
    - Tool can check correct execution environment through shell commands.
    - User can configure approval workflow.
  - Weaknesses:
    - Tool is not sandboxed out of the box. User should configure server-level guardrails.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool has (a vague) built-in approval workflow for sensitive actions.
    - Tool can check correct execution environment through shell commands.
    - User can prompt the agent to request approval before conducting sensitive actions.
  - Weaknesses:
    - Tool is not sandboxed out of the box. User should configure server-level guardrails.
    - User must instruct the agent every session.

### Access Relevant Context Information Within a Project

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool maintains context across many conversation turns, all project files, and resumable sessions.
    - User can compact long session context to reduce token load.
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: ++
  - Strengths:
    - Tool maintains context across many conversation turns, all project files, and resumable sessions.
    - Tool transparently stores sessions as `.chat` files supports chat resumption.
  - Weaknesses:
    - None

### Decompose a Request into Verifiable Goals

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool decomposes requests into verifiable subtasks through built-in planning agent.
    - User can configure planning workflows.
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - User can prompt the agent to decompose tasks and verify results.
  - Weaknesses:
    - Tool does not provide a dedicated planning mode.
    - User must instruct the agent every session.

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

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool reports results with narrative summaries and recommendeds next steps out of the box.
    - User can configure specific reporting behavior.
  - Weaknesses:
    - None

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool reports results with narrative summaries and recommendeds next steps out of the box.
    - User can prompt the agent for specific reporting behavior.
  - Weaknesses:
    - User must instruct the agent every session.

### Support Responses with Citations, Confidence Levels, or Verification Steps

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: +
  - Strengths:
    - Tool can report verification steps through testing and review workflows.
    - Tool can cite sources.
    - User can configure response behavior.
  - Weaknesses:
    - Tool does not consistently provide citations out of the box.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool can report verification steps through testing and review workflows.
    - Tool can cite sources.
    - User can prompt the agent for verification and citation behavior.
    - User can add documents to a built-in vector database and ask questions about the documents.
  - Weaknesses:
    - User must instruct the agent every session.

### Report Conversations to EuXFEL Staff

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: +
  - Strengths:
    - User can configure reporting workflows.
    - Tool can send reports to external systems via MCP.
    - Tool can store reports as files in the workspace, which enables manual handoff and reporting.
  - Weaknesses:
    - Tool does not provide reporting workflow out of the box.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool stores chat history as files in the workspace out of the box, which enables manual handoff and reporting.
  - Weaknesses:
    - Tool does not support reporting to external systems.

### Assist in Drafting Scientific Manuscripts

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: +
  - Strengths:
    - User can configure drafting workflow.
  - Weaknesses:
    - Tool is not provide drafting workflow out of the box.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - User can prompt the agent to draft a manuscript.
  - Weaknesses:
    - User must instruct the agent every session.

### Recommend Using a Version Control System

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: +
  - Strengths:
    - Tool can execute Git workflows and operations.
    - User can configure git-focused workflows.
  - Weaknesses:
    - Tool does not consistently recommend version-control usage out of the box.

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - Tool can execute notebook cells to generate notebook checkpoints
  - Weaknesses:
    - Tool cannot execute Git workflows and operations.

### Optimize Latency

- **Kilo Code, OpenCode, goose**
  - Rating: +
  - Strengths:
    - Tool supports response streaming.
    - Tool optimizes latency through delegated sub-agents.
    - User can configure agent workflow and response behavior to optimize latency.
  - Weaknesses:
    - Latency behavior can vary when connected to the remote Jupyter Lab server via MCP.

- **Roo Code**
  - Rating: +
  - Strengths:
    - Tool supports response streaming.
    - User can configure agent workflow and response behavior to optimize latency.
  - Weaknesses:
    - Tool cannot execute sub-agents in parallel.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool supports response streaming.
    - Tool and notebook are stored on the same server, which improves latency.
  - Weaknesses:
    - Tool cannot execute sub-agents in parallel.

### Not Share User Data

- **Kilo Code, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool supports local LLMs.
    - User can configure the tool to deactivate telemetry (see [Kilo Code](https://github.com/Kilo-Org/kilocode/issues/8171), [goose](https://goose-docs.ai/docs/guides/usage-data/), [Roo Code](https://github.com/RooCodeInc/Roo-Code/blob/main/PRIVACY.md)).
  - Weaknesses:
    - None

- **OpenCode**
  - Rating: ++
  - Strengths:
    - Tool supports local LLMs.
    - Tool has no telemetry setting. [Docs](https://opencode.ai) state that there is no telemetry feature.
  - Weaknesses:
    - Assurances in docs are not a guarantee.

- **Jupyter AI**
  - Rating: +
  - Strengths:
    - Tool supports local LLMs.
  - Weaknesses:
    - Unclear what data is reported to third parties.

### Implementation Effort

- **Roo Code**
  - Rating: ++
  - Strengths:
    - Tool provides ready-to-use agentic workflows.
    - User can onboard with broad documentation and moderate setup effort.
    - User can configure every setting via UI.
    - Tool is actively maintained by a large OSS community.
  - Weaknesses:
    - None

- **Kilo Code, OpenCode, goose**
  - Rating: +
  - Strengths:
    - Tool provides ready-to-use agentic workflows.
    - User can onboard with broad documentation and moderate setup effort.
    - User can configure most settings via UI or interactive CLI.
    - Tool is actively maintained by a large OSS community.
  - Weaknesses:
    - User must get to know and work with special directories and files to add special settings (e.g., custom skills and agents).

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - Tool provides ready-to-use (restricted) agentic workflows.
  - Weaknesses:
    - User cannot install other agents (OpenCode, etc.) on the remote Jupyter Lab server.
    - User cannot access configuration files on the remote Jupyter Lab server.

### Component Replacement Effort

- **Kilo Code, OpenCode, goose, Roo Code**
  - Rating: ++
  - Strengths:
    - Tool is interoperable with other agentic AI tools through MCP support and transferable instruction patterns.
    - User can reuse familiar skills and command structures across systems.
  - Weaknesses:
    - User must adapt some tool-specific configuration details (e.g., MCP client config).

- **Jupyter AI**
  - Rating: -
  - Strengths:
    - Tool (in theory) supports multiple agents through ACP and custom personas.
  - Weaknesses:
    - User cannot exchange agents due to restricted server environment.
