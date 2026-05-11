# Participant 02

## Demographics

What is your job position?

- Data scientist (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- Every day
- Multiple days per week
- Once per week
- **Less than once per week**
- Never

With what AI assistants have you worked before?

- RAY (just trying)

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- Yes, two use cases:
  - SQS: calibrating data
  - SCS: estimating resolution of a detector

## RAG Interaction (via Grounded Docs UI)

- Participant added [SQS technique-oriented docs](https://dataanalysis.pages.xfel.eu/techniques-docs/sqs/).
- Question to SQS docs: **How can I calibrate data from the eTOF in SQS?**
- System did not find the correct doc, but a near-duplicate, which provides slightly different (and the wrong) code.

## Code Generation/Explanation/Improvement (via AI agent)

GPT-5.4-mini:

- Question: **How can I calibrate data from the eTOF in SQS?**
- Answer was conceptually correct, but implemented many lines of code, representing what the EuXFEL library can do with a few lines.
- After re-prompting, the agent spend a lot of time by calling many MCP tools. It reused a GitHub repo from DESY FLASH (instead of EuXFEL). Answer seemed to be conceptually correct, but was not the EuXFEL version described in the SQS docs.
- Participant pointed the model towards the SQS docs available via the RAG mcp server. Produced code was correct but just used numpy and not the expected EuXFEL library.

Qwen3-Next-80B-A3B-Thinking:

- Question: **How could I read data from the MaranaX detector in SCS and optimize its resolution in an HRIXS experiment at European XFEL?**
- Agent mixed up SCS with SQS. Overall, there was at lot of misunderstood points in the response.

GPT-5.3-Codex:

- Same SCS question again
- Solution seemed to be conceptually correct, but lacked code for some steps. Eventually, as the user prompt was not explicitly focused on code.
- After re-prompting to produce code for the steps, the response contained a lot of code but not from the relevant SCS Toolbox repo from GitLab.
- After re-prompting to steer the agent towards the SCS toolbox, the response was a good solution using the library. BUT it actually used a fork of the repo, not the original repo from SCS.

Further observations:

- When participant switched the model from OpenAI (5.4-mini) to Nebius Token Factory (Qwen3), the conversation window was filled with empty spaces indefinitely. We had to stop the session and start a new one.
- At some point, GPT-5.4-mini ran into rate limitation error. Probably because we reached to maximum tokens per minutes allowed by OpenAI. This is why we switched the LLM.

## Reporting

Impression of the feature and report structure:

- Interesting. But participant does not have a plan (yet) on how they would react to the report. It is a bit overwhelming.
- Report should be focused on reporting problems.

## Verdict

Positive:

- Agent described each step of the solution, even if it could not find the optimal solution.
- Agent provided citations of original docs.

Negative:

- Agent did not always provide full-code solutions.
- Agent did not always found the correct source (docs, repository).

What was unexpected:

- Many agent modes (Ask, Plan, Code) - a bit confusing

What features do you miss:

- None

## Internal

### Implemented Improvements Before Starting the Session

- Added EXtra library to RAG system
- Update AGENTS.md: Agent should **always** request to git-commit after completing an edit.
- Kilo Code read permissions: Previous user auto-permitted many read actions. We kept them.

### Technical Details

- Timestamp: 2026-04-22-14:00
- Setup:
  - VS Code + remote kernel via SSH to Maxwell Jupyter Lab + Kilo Code
  - Agent instructions: AGENTS.md + skills directory
  - Note: Agent could not execute code itself as it is outside the SSH environment and did not have access to the kernel.
- LLMs: GPT-5.4-mini, Qwen3-Next-80B-A3B-Thinking, GPT-5.3-Codex

### Improvement Notes

- Work on a solution that enables agent to execute code via the remote kernel.
- Use GPT-5.3-Codex instead of GPT-5.4-mini to improve latency and quality of results.
- Add [SQS technique-oriented docs](https://dataanalysis.pages.xfel.eu/techniques-docs/sqs/) to RAG ingestion script.
- Update AGENTS.md:
  - Steer agent towards using important GitLab and GitHub repositories (e.g., SCS Toolbox on GitLab). But it should only use originals, not forks.
  - Clarify that the agent should always provide code as a solution (as long as not explicitly prompted differently).
- Add skill report-problem: a problem-focused version of report-conversation, which is only executed when a problem occurred in the conversation.
- Be aware of Kilo Code UX bug: Switching from OpenAI to Nebius models might cause the tool to add infinite free spaces in the session. Ultimately, you have to stop the session and start a new one.
