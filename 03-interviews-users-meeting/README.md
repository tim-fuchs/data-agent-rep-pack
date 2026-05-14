# Interviews with Facility Users and Members

## Summary of Interview Results

### Overview

- Date: 2026-01-27
- Event: Annual *Users' Meeting* of European XFEL and DESY
- Participants:
  - Three users
  - Five staff members (four scientists, one manager)
- Resources:
  - [Poster](01-users-meeting-poster.pdf)
  - [Interview results](02-users-meeting-results.md)

### Problem Identification and Motivation

- Data Analysis group provides very helpful support to users.
- Users do not want to read documentation.

### Definition of Objectives of a Solution

- Answer technical questions (e.g., about how to use a library)
- Plot data
- Improve user code
- Access all relevant information from myMDC and DAMNIT
- Use Slurm for batch processing
- Can adapt its code style to the user's style
- Provide a daily summary of myLog chat messages
- Must be private by design

## Debriefing Session

### Overview

- Date: 2026-02-12
- Participants:
  - 1 host
  - 13 members of EuXFEL Data Analysis group
- Objectives:
  - Review interview results  
  - Define next steps

### Review of Interview Results

- Low number of interviewees:
  - Not sufficient as the sole basis for tool planning.
  - Nevertheless, responses align with insights from previous interviews and focus group.
- Several proposed tool features seem valuable, e.g.,:
  - Plotting XGM vs. train ID
  - Documentation retrieval
- Clarification on the "summarize myLog messages" requirement:
  - Could help identify failures and critical events from the data
  - Might also summarize Redmine tickets and link them to myLog content.
- Risk:
  - An AI agent may inadvertently increase support requests if users report issues with generated code.

### Next Steps

1. Collect data sources for the knowledge base:
   - EXtra and EXtra-data libraries as foundational components  
   - FXE technique-oriented documentation, including Jupyter notebook examples
   - Eventually, AGIPD detector documentation
2. Begin implementation of the RAG system

### Further Information

- [FrevaGPT](https://indico.desy.de/event/50983/contributions/195463/):
  - AI agent developed by DKRZ  
  - Uses the Jupyter AI extension to generate code directly in Jupyter Notebooks
- [Context7](www.context7.com):
  - MCP server providing documentation for open-source projects, including Python packages such as EXtra-data  
  - Chatbot on Context7 website can generate plausible code for EXtra-data but mislabels the train index variable as *train ID* and occasionally hallucinates within code snippets.
