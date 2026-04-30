# Participant 09

## Demographics

What is your job position?

- instrument scientist (physics background)

How often do you use generative AI (e.g., ChatGPT, Claude Code)?

- **Every day**
- Multiple days per week
- Once per week
- Less than once per week
- Never

With what AI assistants have you worked before?

- ChatGPT
- Gemini
- Brave AI Assistant

How often do you analyze data via Jupyter notebooks, Python, Julia, R, etc.?

- Every day
- **Multiple days per week**
- Once per week
- Less than once per week
- Never

## Focus of This Session

Have you brought your own use case or Jupyter notebook?

- How to execute Slurm batch job to execute code in parallel

## RAG Interaction (via Grounded Docs UI)

- EuXFEL user docs: Can you find the documentation for how to use the Slurm
  - Could not find the result
- Maxwell: How to use Slurm
  - Could not find it

## Code Generation/Explanation/Improvement (via AI agent)

- Q (Ask): How to use Slurm? I have a Python file. I want to submit this as a job.
- R: Reasonable answer. Provided citation to Maxwell docs.
- Q: I have a for loop in my code, which has 500 iterations. Each one is independently computable. I want to use Slurm to run multiple loops simultaneously. How to do that? Explain with example.
- R: Reasonable answer. A bit unncessary extras (common commands).
- Q (Code): Can you check using my Juptyter kernel how many nodes I have available for use and depending on that tell me how long my array can be.
- R: Agent first responded that it could not access sinfo via its internal terminal. Participant had to steer it to use the available Jupyter notebook to check this information. Via some back and worth we made it work.

Further observations:

- Agent provided outdated URL to Maxwell Job Documentation

## Reporting

Impression of the feature and report structure:

- Not tested

## Verdict

Positive:

- Access Jupyter notebook to try to execute the commands

Negative:

- RAG system could not find relevant information

What was unexpected:

- Nothing

What features do you miss:

- Agent should be able to write code and execute it (this problem was caused by connection errors)

## Internal

### Implemented Improvements Before Starting the Session

- AGENTS.md:
  - Agent should create atomic notebook cells instead of big cells.
  - We made the Git instructions more explicit (git init + git commit in one step).
  - We added an instruction that the agent should recommend the user to close and re-open an edited Jupyter file to make the edits by the agent visible to the user.
- RAG: We added the [SCS Toolbox](https://scs.pages.xfel.eu/toolbox/).

### Technical Details

- Timestamp: 2026-04-30-11:00
- Setup:
  - VS Code + remote kernel via SSH to Maxwell Jupyter Lab + Kilo Code
  - Agent instructions: AGENTS.md + skills directory
- LLMs: GPT-5.4

### Improvement Notes

- Renew Maxwell documentation (only focused on Infrastructure webpages at the moment)
- Add official [Slurm docs](https://slurm.schedmd.com)
