# Participant 05

## Demographics

What is your job position?

- Software engineer (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- Claude
- Claude Code
- GitHub Copilot
- ChatGPT
- Mistral

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- Every day
- Multiple days per week
- Once per week
- **Less than once per week**
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- Getting started with a run + do simple computation + make it scalable (and scientifically reproducible).

## RAG Interaction (via Grounded Docs UI)

- Q (European XFEL user docs): What Python version is used in the DA environment of 2024?
- A: Found the right information in the first chunk.
- Q (Maxwell docs): List specific maxwell hardware.
- A: Could not find the page as it is located on a page not accessible outside the internal network.
- Participant updated the Maxwell docs to include the internal pages.

## Code Generation/Explanation/Improvement (via AI agent)

- Q: Add a publication-worthy caption to the plot in the `extra.ipynb`.
- A: Good
- Q: How to show distribution of photon fluxes across multiple runs (not just one)?
- A: Good. One note was strange: "You should process one run at a time" (but Maxwell is designed for parallel processing).
- Q: Write code to calculate this.
- A: Code was somewhat correct. But extremely verbose. Problem was that it created another Python helper file, which could not be instantly executed via the Jupyter kernel. Manual work was necessary to make this work.

Further observations:

- Apparently, GPT-5.3-Codex ignored the AGENTS.md again (for Git commit).

## Reporting

Impression of the feature and report structure:

- Conversation summary can be useful.
- Summary might be also suited as extended session memory.

## Verdict

Positive:

- It was performing quite well for retrieval tasks.

Negative:

- Produced code was too verbose. Must use existing libraries instead of writing everything itself.

What was unexpected:

- Nothing

What features do you miss:

- Enforce actions from the AGENTS.md with agent hooks (if available for Kilo Code).
- More LSP-focused MCP servers, e.g., Pylance MCP.
- More specific agent workflow for the use case could be beneficial.
  - E.g., an orchestrator that splits big tasks into multiple sub-agents.
  - Check if Kilo Code and OpenCode also supports a Chat Debug feature like Copilot those. Update: None of both provide such a feature.

## Internal

### Implemented Improvements Before Starting the Session

- Kilo Code read permissions: Previous user auto-permitted many read actions. We kept them.
- AGENTS.md:
  - Capitalized "ALWAYS" in the initial instruction that it should always follow the subsequent instructions.
  - Edit to "Work with up-to-date information":
  
    ```bash
    [...]
    6. Use your internal knowledge.
    - If you use your internal knowledge, use `webfetch` to retrieve related sources that you can cite in your response.
    ```

### Technical Details

- Timestamp: 2026-04-24-14:00
- Setup:
  - VS Code + Jupyter Lab API + Kilo Code
  - Agent instructions: AGENTS.md + skills directory
  - Note: Agent could not execute code itself as it missed instructions on how to use remote Jupyter kernel.
- LLMs: GPT-5.3-Codex

### Improvement Notes

- Add further LSPs via MCP servers, e.g., Pylance, to improve the quality of the generated code (even without needing to execute it to test its correctness).
- Research if Kilo Code provides hooks that enable a customization of the agent behavior and that the agent adheres stricter to than AGENTS.md.
  - Kilo Code's Markdown-based [rules](https://kilo.ai/docs/customize/custom-rules) seem to be the only option.
  - OpenCode supports code-based [plugins](https://opencode.ai/docs/plugins/) (not compatible with Kilo Code).
- Be aware that indexing the complete Maxwell docs requires an internal network connection as some pages (e.g., for [hardware specs](https://docs.desy.de/maxwell/infrastructure/compute/hw_allcpu/)) are not available publicly.
