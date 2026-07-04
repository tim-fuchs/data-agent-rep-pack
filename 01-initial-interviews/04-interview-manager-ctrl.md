# Interview with Manager of the European XFEL Controls Group

Date: 2025-12-10

## Current Process

- Typical tools for offline data analysis:
  - **Mostly JupyterHub** on HPC cluster (Maxwell)
- Most useful forms of user support during offline data analysis:
  - Provide **tailored notebook templates**
  - **Improve code** to optimize performance with European XFEL hardware and software
  - Key question: Should the tool **target beginners** (who need templates and extensive guidance) or **advanced users** who mainly need library-specific help (e.g., auto‑completion)?

## Planned Tool

- Preferred interface for users (and for European XFEL in the long term):
  - Likely **Jupyter AI**. Authentication for JupyterHub on HPC cluster is partially handled already because users log in with their DESY/European XFEL accounts.
  - European XFEL's internal LLM system (RAY) is not suitable; only staff and long-term guests have access, not regular users.
- Current status of the European XFEL RAG project (documentation unclear so far):
  - A DA team member has created an initial ingestion script for adding DA documentation.
  - The CTRL group manager is developing MyLog support (in Zulip) for users.
  - A CTRL group PhD student is working on predictive maintenance support for the Data Operation Center via RAG; no prototype yet.

## Planned Study

- Feasibility of running the study in January–February:
  - User operation begins only on 15.04.2026. **Access to users is restricted to protect facility reputation, so direct user intervention is not feasible.**
  - More realistic forms of process intervention:
    - **Experts in data acquisition of the CTRL group** could test typical offline analysis workflows using the prototype; this could double as training.
    - The **Data Operation Center** could use the tool to reconstruct and troubleshoot past user issues.
- European XFEL Users' Meeting, 2026-01-23 -30: usefulness for connecting with users?
  - Yes.
  - The DA manager will host a satellite meeting. Consider registering a poster and adding a QR code linking to a survey.
