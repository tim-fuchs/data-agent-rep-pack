# Instructions

## Preparation

1. Duplicate template project.
2. Open new version in VS Code.
3. Deactivate jupyter-mcp servers.
4. Connect to Maxwell Jupyter Lab

## Intro

1. Purpose
   - Explore an AI system
   - You should act like a user during offline data analysis today.
   - Goals:
     - What works good
     - What must be improved
     - Your opinion about the entire agentic concept for offline data analysis
     - This will help to improve the tool iteratively

## Demographics

- Ask demographic questions

## System Overview

1. System overview
   - Remote Jupyter Lab + local agent
   - Remote Jupyter kernel + local VS Code (+ local notebook + local agent)
   - -> Today, focus on option 2

2. Repo overview
   - Have 
   - Notebook
   - Explain agent features (modes Ask/Plan/Code, new sessions)
   - AGENTS.md (purpose)
   - Skills (purpose)
   - What is a bit limiting:
     - Only open notebook in read mode, not write mode (otherwise, close notebook to see edits from the agent).

## Knowledge Sources

1. RAG
   - Open Grounded Docs (<http://localhost:6280>)
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

## Drafting Manuscript

- Use the skill /draft-manuscript to create a first manuscript draft
- What would you have expected from this feature?

## Reporting

- Use the skill /report-conversation to send a report to the EuXFEL staff
- Which content would you have expected in the report?

## Verdict

- What do you like about the system?
- What should be improved?
- What was unexpected?
- What features do you miss?
