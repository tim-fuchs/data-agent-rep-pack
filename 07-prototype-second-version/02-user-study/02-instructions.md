# User Study: Preparation and Instructions During Session

## Preparation

1. Check that Docker containers with MCP servers run.
2. Update template project with notes from previous session (e.g., `kilo.jsonc` and `AGENTS.md`).
3. Duplicate agent project.
4. Edit name, e.g., `project-06` (to not display Kilo Code history of previous sessions).
5. Open the duplicate in VS Code.
6. If active, deactivate `jupyter-mcp` server in Kilo Code.
7. In a terminal session, start SSH connection to Maxwell, load European XFEL Python module, start Jupyter Lab:

   ```bash
    ssh -L 8888:localhost:45123 max-exfl-display.desy.de
    module load exfel exfel-python/202601
    jupyter lab --no-browser --ip 0.0.0.0 --port 45123 --IdentityProvider.token="your-secure-jlab-token"
   ```

8. Open `extra.ipynb`.
9. (Do this once) Click the kernel selection button, add a remote Jupyter kernel:
   - Name: `HPC`
   - URL: `http://localhost:8888/lab?token=your-secure-jlab-token`
10. If prompted by VS Code, enter the Jupyter Lab token (`your-secure-jlab-token`).
11. Select remote Jupyter kernel.

## Intro

1. Purpose
   - Explore an agentic AI system
   - You should act like a user during offline data analysis today.
   - Goals:
     - What works good
     - What must be improved
     - Your opinion about the entire agentic concept for offline data analysis
     - This will help to improve the tool iteratively
     - Not: rating your performance

## Demographics

- Ask demographic questions

## System Overview

1. System overview
   - Remote Jupyter Lab + local agent
   - Remote Jupyter kernel + local VS Code (+ local notebook + local agent)
   - -> Today, focus on option 2

2. Repo overview
   - Have you brought your own notebook or use case?
   - Explain agent features (modes Ask/Plan/Code, new sessions)
   - AGENTS.md (purpose)
   - Skills (purpose)

## Focus of This Session

- Explain your own notebook or use case.

## Knowledge Sources

1. RAG
   - Open Grounded Docs UI (<http://localhost:6280>)
   - Go to Extra-data library.
   - Ask a question (e.g., how to open a run).
   - What documentation does the agent require to understand your regular use case (papers, websites, software docs, etc.)?
     - Evtl. find and index the document (if website).
   - Now, go to VS Code and use the Ask/Plan mode of the agent to ask the question.

2. GitLab:
   - Ask the agent a question about a repo you can find internally on GitLab (not a private repo).

3. GitHub:
   - Ask the agent a question about a public GitHub repo, e.g. by European XFEL.

## Code Generation/Explanation/Improvement

- What would you like to create with the agent?
- Based on what you researched, use the Plan mode of the agent to create a new notebook.
- (Check if you can install further packages)

## Reporting

- Use the skill /report-conversation to send a report to the European XFEL staff
- Which content would you have expected in the report?

## Verdict

- What do you like about the system?
- What should be improved?
- What was unexpected?
- What features do you miss?
