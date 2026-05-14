# Design, Demonstration, and Evaluation of First Prototype

## Prototype Overview

- Note:
  - We cannot provide the source code for the first prototype, as it relies heavily on an internal system that is not (yet) intended for release.
  - We do not consider this a threat to the validy of our study. We consider the first prototype a "throwaway" from which we derived new design objectives for the second prototype. The second prototype is [available in this repository](/07-prototype-second-version/README.md).
- RAG backend: `karabo-rag`
  - Based on [EuXFEL Karabo RAG project](https://git.xfel.eu/llm/karabo-rag) (EuXFEL account required for access)
  - Vector database: Qdrant
  - Exposes an API handler that a frontend can consume and that supports multi-turn chat conversations
  - Exposes another API to manage document ingestions
  - Models:
    - Chat completions: GPT-5.4-mini (OpenAI)
    - Document embedding: text-embedding-large (OpenAI)
  - Knowledge base: [EXtra-data](https://extra-data.readthedocs.io/en/latest/index.html)
- Agent frontend: [Jupyter AI v2](https://jupyter-ai.readthedocs.io/en/v2/)
  - Extension that we installed via `pip` on the remote Jupyter Lab server hosted on the EuXFEL HPC cluster
  - Provides a pre-built *Jupyternaut* agent persona
  - Does not support multi-agent workflows, including an agent loop.
  - Is preconfigured to connect to the agent endpoint
  - Model for chat completions: GPT-5.4-mini (OpenAI)

## Evaluation with Data Analysis Group

- Date: 2025-03-19
- Setting: Meeting with 12 members of the EuXFEL Data Analysis group
- What are your first positive/negative thoughts on the demo? What would be important improvement potentials for the next prototype version?
- **Good:**
  - Jupyter AI interface is straightforward. Configure an EuXFEL persona and eventually add custom commands.
  - The LLM responses in the side panel are formatted correctly with Markdown and code cells.
- **Negative:**
  - The LLM responses of the cell magic should be executable code cells with inline code comments instead of plain text output.
  - The LLM response should embed clickable URLs directly in the main response body, not just in the reference section.
  - Generated code contains many hallucinations, such as non-existing methods or attributes.
    - We should ingest the entire AST of the code together with the corresponding documentation comments and unit tests, and restrict the LLM to focus on the available data only.
    - We should ingest existing notebooks, e.g., from the users (be aware of potential copyright problems) and from the DA group).
    - We should run the LLM in agent mode **(Gen AI assistant vs. agentic AI system)**.
      - Add linting (Pylance, MyPy).
      - Add validation loop (generate, test, fix, re-run).
      - After the meeting, one of the meeting participants generated a notebook that contains an overview of every EXtra-data feature. They created it with Claude Opus 4.6, a short prompt, and a link to the public EXtra-data documentation. This creates the question if a RAG component is even necessary for modern agents with access to the internet.
- **Unclear/confusing:**
  - Which additional context from the notebook is sent to the LLM together with the prompt? Does it differ for the side panel and the cell magic?
    - By default, just the last two prompts and responses.
    - This can be configured in the Jupyter AI settings.
    - The context should eventually include the entire notebook, other files, or the entire repository.
- **Further notes:**
  - Check out **Grounded Docs**, an open-source MCP server as alternative to Context7, which can provide information from various documents (text, PDFs, code, etc.) and executes semantic chunking.
  - If the agent should be deployed on the HPC cluster:
    - Make sure it is sandboxed in a restricted environment. This could be enabled by **nono**, which uses Landlock. However, Landlock is apparently deactivated on the EuXFEL HPC.
    - Make sure that any code execution is approved by a human. An autonomously acting agent could consume a lot of capacity while working on flawed solutions.
- **Takeaways:**
  - Ready-to-use agentic tools (like Claude Code) perform much better than our self-developed system. Many developers already use such tools on their computers. We should built on that.
  - The main challenge lies in integrating such agentic tools into the infrastructure at EuXFEL (particularly the HPC cluster) and adapting their behavior to the use case of offline data analysis at EuXFEL.
