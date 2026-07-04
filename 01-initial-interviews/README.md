# Initial Interviews with Managers

## Summaries of Individual Interviews

- [Interview 1](01-interview-manager-da.md)
- [Interview 2](02-interview-manager-da.md)
- [Interview 3](03-interview-manager-ctrl.md)
- [Interview 4](04-interview-manager-ctrl.md)
- [Interview 5](05-interview-manager-da.md)

## Summary of All Interviews

### Problem Identification and Motivation

- Users often contact European XFEL members of the scientific instruments and Data Analysis groups for support during:
  - Start-up phase of experiments, often with questions about hardware calibration and configuration
  - Offline data analysis
- Definition of offline data analysis:
  - It begins after the experiment at the beamline has finished.
  - The Data Analysis group calibrates the experimental data and then provides the raw and calibrated datasets to the user.
  - Datasets are often up to multiple petabytes large and distributed across many HDF5 files.
  - Datasets contain multiple experiment runs, and runs contain data from various hardware devices such as detectors and motors.
  - Users analyze the datasets together with metadata collected during the experiment to synthesize publishable scientific findings.
  - Users most often conduct offline data analysis via a JupyterHub server running on the HPC cluster called Maxwell.
- Typical user questions during offline data analysis:
  - How to measure photon counts of pump-probe experiments?
  - Detector geometry and layout
  - Pixel masking
  - Pixel calibration, which is largely resolved now but was previously a major topic
- Support resources:
  - Existing support resources for users and scientists include instrument-specific manuals.
  - However, these manuals are often very extensive.
- Current actions to counter documentation retrieval problems:
  - Transitioning from tool-centric documentation to experiment-centric documentation focused on experimental techniques and analysis methods.
  - The Data Analysis group started with documentation for instruments FXE and SQS.

### Definition of Objectives of a Solution

- Focus on AI support for offline data analysis:
  - Vision: an AI system provides first-level user support, particularly outside working hours of European XFEL staff.
    - In principle, staff should no longer support users during the offline data analysis phase. In practice, they will still support them to a limited extent.
    - If user-AI interaction is logged, a staff member can later review and correct the chatbot’s responses if necessary.
  - Possible solution features:
    - Provide tailored notebook templates
    - Navigate complex data entries of multiple hardware devices
    - Create and interpret complex plots
    - Optimize the user’s analysis code for HPC
    - Detect and report insufficient documentation to European XFEL staff based on user prompts and insufficient system responses
  - Key question: who is the targeted user group?
    - Beginners need templates and extensive guidance
    - Advanced users mainly need library-specific help, for example auto-completion
    - Both?
- Considerations for a first prototype:
  - Consider existing AI systems developed by a small team at European XFEL:
    - There is a system based on the FastMCP framework that exposes RAG functionality.
    - There are initial scripts for ingesting documentation from multiple sources into a RAG system.
    - Current work on the user interface via Zulip messenger.
    - There is a PhD project on predictive maintenance support for the Data Operation Center via RAG. No prototype available yet.
  - RAG component:
    - Besides the technique-oriented docs, a RAG system could help make the content for a specific problem more accessible.
    - Focus on the AGIPD detector, as it is the largest data source at European XFEL, has extensive existing documentation, and is related to many publications.
  - User interface options:
    - Jupyter AI: a good option because authentication for JupyterHub is already handled, as users log in with their DESY/European XFEL accounts.
    - Zulip messenger: the chatbot could join a relevant MyLog stream, for example Data Analysis.
    - European XFEL’s internal LLM frontend called RAY: not suitable, as only staff and long-term guests have access, not regular users.
  - System constraints:
    - The system should always cite the sources it used to generate a response to the user prompt.
    - The system should support MCP to be compatible with the existing system.
    - The user should decide which AI interactions are reported to European XFEL staff.

### Next Steps

- Further problem investigation:
  - Attend a meeting of the Data Analysis group to present and discuss ideas and the focus of the initial prototype with the experts.
  - Attend the poster session at the upcoming annual Users’ Meeting at European XFEL as an opportunity to interview users as well as European XFEL staff.
- Possibilities for tool evaluation:
  - Ideally, the solution should be tested with real users.
  - However, access to them is restricted to protect facility reputation.
  - As proxies for real users, European XFEL members who are in close contact with the users could be used.
    - Experts in data acquisition from the Controls group could test typical offline analysis workflows using the prototype; this could be considered training for them.
    - The Data Operation Center could use the tool to reconstruct and troubleshoot past user issues.
