# Evaluation of Candidates for Integrating Retrieval-Augmented Generation (RAG) Functionality

## Candidates

- [Grounded Docs](https://grounded.tools)
  - Version: 2.2.1
  - What: Open-source, ready-to-use RAG service with main focus on MCP connectivity

- [OpenRAG](https://www.openr.ag)
  - Version: 0.4.1
  - What: open-source, ready-to-use RAG service with additional [MCP connecitivity](https://github.com/langflow-ai/openrag/tree/main/sdks/mcp)

- **Irrelevant candidates**
  - [Context7](https://context7.com)
    - What: Ready-to-use RAG service with docsumentation of various open-source projects and CLI and MCP connectivity
    - Requires user account
    - Freemium service
  - [LlamaIndex](https://developers.llamaindex.ai/python/cloud/llamacloud/getting_started/)
    - What: Ready-to-use RAG service
    - Requires user account
    - Freemium service
  - [MCP Scientific RAG](https://github.com/davinson-pezo/mcp-scientific-rag)
    - What: open-source, free, ready-to-use RAG service with MCP connectivity
    - Just a hobby project with no active maintainer community
  - [RAG MCP Server](https://github.com/tungetti/rag-mcp-server)
    - What: open-source, free, ready-to-use RAG service with MCP connectivity
    - Just a hobby project with no active maintainer community

## Requirements Analysis

### Work With Up-to-Date Information

- **Grounded Docs**
  - Rating: ++
  - Strengths:
    - User can ingest websites and local documents.
    - User can update the ingested docs via a refresh button and the API.
    - User can use the API to plan cron jobs that update the ingested docs.
    - Tools supports versioning of docs and version-specific queries, so results match the exact library version in use.
    - User can chat with the indexed docs. Tool retrieves and returns relevant document chunks.
    - MCP server delivers relevant chunks. LLM of AI agent can then synthesize the chunks into a response that fits to the instructions of the agent.
  - Weaknesses:
    - User must index the relevant source first.
    - Tool does not synthesize the retrieved chunks into a response.

- **OpenRAG**
  - Rating: +
  - Strengths:
    - User can ingest websites and local documents.
    - User can ingest documents stored on external storage sources (e.g., Google Drive).
    - User can chat with the indexed docs. Tool retrieves relevant document chunks and synthesizes them into a response.
    - MCP server delivers a ready-to-print response that the LLM of OpenRAG synthesized from the retrieved chunks.
  - Weaknesses:
    - User must index the relevant source first.
    - User must remove and renew documents, e.g., when a website was updated. OpenRAG does not provide a refresh feature.

### Latency Optimization

- **Grounded Docs**
  - Rating: ++
  - Strengths:
    - MCP service is quick as it just returns chunks.
  - Weaknesses:
    - None

- **OpenRAG**
  - Rating: +
  - Strengths:
    - MCP service returns a ready-to-print response.
  - Weaknesses:
    - Response of MCP server takes a while due to response creation.
    - Response of MCP server might have to be reworked by agent to fit the agent instructions.
    - The stack is heavy: backend, frontend, Langflow, OpenSearch, and Docling. More components could mean more latency than a single service.

### Not Share User Data

- **Grounded Docs**
  - Rating: +
  - Strengths:
    - User can deactivate telemetry.
  - Weaknesses:
    - None.

- **OpenRAG**
  - Rating: ++
  - Strengths:
    - No telemetry, as far as we know
  - Weaknesses:
    - None

### Implementation Effort

- **Grounded Docs**
  - Rating: ++
  - Strengths:
    - Tool is a ready-to-use RAG service with CLI and GUI interactivity, as well as built-in MCP server.
    - User can start the tool with a single `npx` command (or with a Docker container).
    - User can simply add a remote MCP client to their agentic tool to connect to Grounded Docs.
    - Tool is very lightweight.
  - Weaknesses:
    - User must config model provider initially.

- **OpenRAG**
  - Rating: ++
  - Strengths:
    - Tool is a ready-to-use RAG service with GUI interactivity that exposes an API for MCP connectivity.
    - Tool is containerized by design. User can start container with a `uvx` command.
    - User can simply add a local MCP client to their agentic tool to connect to Grounded Docs. Alternatively, the [OpenRAG MCP server](https://github.com/langflow-ai/openrag/tree/main/sdks/mcp) can also be containerized and added as remote MCP client to the agent.
  - Weaknesses:
    - User must install a quite heavy Docker container containing OpenSearch, Langflow, Docling, etc.
    - User must config model provider and app password initially.

### Component Replacement Effort

- **Grounded Docs**
  - Rating: ++
  - Strengths:
    - MCP connectivity makes it simple to switch to other MCP-supporting RAG services.
    - Tool provides [CLI commands](https://github.com/arabold/docs-mcp-server/blob/main/docs/guides/basic-usage.md) that enable regular document ingestion runs.
  - Weaknesses:
    - None

- **OpenRAG**
  - Rating: ++
  - Strengths:
    - MCP connectivity makes it simple to switch to other MCP-supporting RAG services.
    - Tool provides [Python SDK](https://github.com/langflow-ai/openrag/tree/cb5acc0497928f580cc46f3ed67d58cfd7ef28b7/sdks/python) that enables regular document ingestion runs.
  - Weaknesses:
    - None
