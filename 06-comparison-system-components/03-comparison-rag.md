# Comparison of Candidates for Integrating Retrieval-Augmented Generation (RAG) Functionality

## Candidates

- [Grounded Docs](https://grounded.tools)
  - What: Open-source, ready-to-use RAG service with main focus on MCP connectivity
  - Version: 2.2.1

- [OpenRAG](https://www.openr.ag)
  - What: open-source, ready-to-use RAG service with additional [MCP connecitivity](https://github.com/langflow-ai/openrag/tree/main/sdks/mcp)
  - Version: 0.4.1

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
  - Rating: +
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
  - Rating: -
  - Strengths:
    - User can ingest websites and local documents.
    - User can ingest documents stored on external storage sources (e.g., Google Drive).
    - User can chat with the indexed docs. Tool retrieves relevant document chunks and synthesizes them into a response.
    - MCP server delivers a ready-to-print response that the LLM of OpenRAG synthesized from the retrieved chunks.
  - Weaknesses:
    - User must index the relevant source first.
    - User must manually remove and renew documents, e.g., when a website was updated. OpenRAG does not provide a refresh feature.
    - Websites can only be ingested via chat interface, not via the knowledge interface.

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
  - Rating: +
  - Strengths:
    - Ready-to-use MCP server with CLI and web UI.
    - Can be started with a single `npx` command, and client wiring is straightforward.
  - Weaknesses:
    - Still requires configuring sources, indexing, and optionally embeddings.
    - Best results need some setup choices around source selection and version targeting.

- **OpenRAG**
  - Rating: --
  - Strengths:
    - Provides a complete, opinionated RAG platform instead of separate building blocks.
    - Quickstart and Docker flows exist for getting the stack running.
  - Weaknesses:
    - Requires coordinating several services and environment variables.
    - Initial setup includes model providers, passwords, OpenSearch, Langflow, and Docling concerns.

### Component Replacement Effort

- **Grounded Docs**
  - Rating: +
  - Strengths:
    - Good fit when the current component is a documentation lookup or search layer.
    - MCP-based integration makes it relatively easy to swap into an assistant toolchain.
  - Weaknesses:
    - Replacing a broader RAG platform still requires adapting ingestion and indexing workflows.

- **OpenRAG**
  - Rating: --
  - Strengths:
    - Can replace multiple pieces at once because it bundles ingestion, search, chat, and flow editing.
  - Weaknesses:
    - It is a full stack replacement, not a drop-in component swap.
    - Migration likely touches infra, data flow, and client configuration at the same time.
