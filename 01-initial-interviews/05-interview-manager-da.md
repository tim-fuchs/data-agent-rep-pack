# Interview with Manager of the EuXFEL Data Analysis Group

Date: 2025-12-12

## Current Process

- Typical tools for offline data analysis:
  - Mostly **JupyterHub** on HPC cluster (Maxwell)
- Additional tools and information sources:
  - **MyMDC**
    - Receives input from DAQ
    - Aggregates experiment-related information
  - **MyLog**
    - Based on Zulip messenger
    - A new Zulip channel is created for each experiment proposal.
    - Each channel contains multiple streams (e.g., Alignment, Data Analysis, Beam Status).
    - Streams include important text and images documenting experiment details.
    - MyLog data is forwarded to MyMDC.
    - The PI of the proposal decides whether to make this data public.
  - **DAMNIT** (metadata tool for offline analysis)
    - Executes a “context file,” a workflow that converts processed datasets into a large summary table.
    - The resulting table lists all experiment runs as rows, including key information for each run.

## Planned Tool

- Note: **RAG-generated answers should always cite to the underlying source material.**
- Additional tool idea:
  - **The chatbot could join a relevant MyLog stream** (e.g., Data Analysis) and provide first-level assistance to users (including outside working hours).
  - A DA team member can later review and correct the chatbot’s responses if needed.
  - Advantage: Transparent user interaction with the chatbot.
  - Alternative: **Chatbot interaction in Jupter AI. User decides which messages should be reported in MyLog.**

## Planned Study

- EuXFEL Users' Meeting, 2026-01-23 -30: usefulness for connecting with users?
  - Yes.
  - The DA manager will host a satellite meeting.
  - Register a poster and include a QR code linking to the survey.
  - Expected attendance:
    - ~1000 participants for the full EuXFEL/DESY Users' Meeting.
    - ~100 participants for the DA satellite meeting.
      - 01-23, 10:00–17:00: online meeting
      - 01-27, 16:00–19:00: poster session at EuXFEL
- Discuss ideas with DA group:
  - 01-15, 14:00–15:00: DA group meeting — opportunity to present ideas and initial prototypes (Zulip, Jupyter, or a combination).
