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
- Copilot
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

- Question: What version of python is used in the DA environments for 2024.
- Response: Found the right information in the first chunk.
- Question to maxwell docs: maxwell hardware
- Response: Could not find it (located in a table apparently not accessible outside the internal network)
- Participant updated the Maxwell docs to include the internal pages.

## Code Generation/Explanation/Improvement (via AI agent)

- **Question:** Add a publication-worthy caption to the plot in the `extra.ipynb`.
- **Response:** Good
- **Question:** How to show distribution of photon fluxes across multiple run (not just one)?
- **Response:** Good. One note was off: You should process one run at a time (but Maxwell can do parallel processing).
- **Question:** Write code to calculate this.
- **Response:** Code was somewhat correct. But extremely verbose. Problem was that it created another Python helper file, which could not be instantly executed via the Jupyter kernel. Manual work was necessariry to make this work.

Further observations:

- Apparently, 5.3-Codex ignored the AGENTS.md again (for Git commit).

## Reporting

Impression of the feature and report structure:

- Conversation summary can be useful.
- Summary might be also suited as extended session memory.

## Drafting Manuscript

Impression of the feature:

-

## Verdict

Positive:

- It was performing quite well for retrieval tasks.

Negative:

- Produced code was too verbose. Must use existing libraries instead of writing everything itself.

What was unexpected:

-

What features do you miss:

- Enforce actions from the AGENTS.md with Agent Hooks (if available for Kilo Code). It is available for Copilot.
- More LSP-focused MCP server, e.g., Pylance MCP.
- More specific agent workflow for the use case might be good. One that splits big task into multiple sub-agents.
  - Check if Kilo Code and OpenCode also support a Chat Debug feature (like Copilot).

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

- Timestamp: 2026-MM-DD-TT:00
- Setup:
  - VS Code + remote kernel via SSH to Maxwell Jupyter Lab + Kilo Code
  - Note: Agent could not execute code itself as it is outside the SSH environment and did not have access to the kernel.
- LLMs: GPT-5.3-Codex

### Improvement Notes

- Add further LSPs via MCP servers, e.g., Pylance, to improve the quality of the generated code (even without needing to execute it to test its correctness).
- Research if Kilo Code provides hooks that enable a customizization of the agent behavior and that are stricter adhered to than AGENTS.md.
  - Kilo Code's Markdown-based [rules](https://kilo.ai/docs/customize/custom-rules) seem to be the only option.
  - OpenCode supports code-based [plugins](https://opencode.ai/docs/plugins/).
