# Meeting with EuXFEL Managers to Discuss Prototype Version Two

Date: 2027-04-14

Who: first author, EuXFEL managers (second and third authors)

## Topics

- Present results of tool research
- Show and discuss current system
- Discuss system requirements
- Discuss further steps

## Tool Research

Present purpose and features of:

- Kilo Code
- OpenCode
- goose
- Roo Code
- DeepAgents (by LangChain)
- Others: Continue, Lemma Code, etc.

## Current System

- User interaction with OpenCode vs. Kilo Code
- Working on a remote Jupyter Lab
- Jupyter MCP:
  - List available notebooks
  - Connect to a notebook
  - Summarize notebook content
  - Add cells with EXtra-data content
- VS Code: Working on local notebook with remote kernel from HPC cluster
- Send report to Zulip
- Currently missing components:
  - GitHub MCP
  - GitLab MCP
  - nono
- Current problem: Jupyter MCP Server not working anymore.
  - VS Code: Access to remote kernels possible, but not executing notebooks a remote kernel.
  - Jupyter MCP: Can connect to notebook, but cannot access notebook content (read and write).
  - Possible cause: flaws in the server configuration

## Requirements

- Question: Are important requirements missing?
- Answer: Sufficient for this MVP. Would have to add further requirements for production-ready system.

## Further Steps

**User study:**

- Participants:
  - 2-5 DA members
  - 2-5 instrument scientists
- Duration: 60 min
- Focus: qualitative insights
- Setup:
  - We provide a computer with the configured agentic AI system (for simplicity and time reasons)
  - Alternative: Fresh install on participants' machines using Docker files.

**Further optimization options:**

- Ingesting and retrieving entire templates of Jupyter notebooks possible with a specific MCP tool?
- Ingesting Alfresco wiki with Grounded Docs possible?
- Is it possible optimizing the agent to conduct test-driven development for notebooks?
