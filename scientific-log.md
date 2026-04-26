# Scientific Log

## 2024-11: Initial Plans

### Research Questions

- What knowledge patterns are present in the documentation of large scientific datasets?
- How can tool support assist data scientists in creating high-quality dataset documentation?

### Methodology

- Likely approach: action research:
  - Identify knowledge patterns through:
    - Interviews with data scientists
    - Content analysis of dataset documentation
  - Investigate tool support by:
    - Interviewing data scientists
    - Proposing and evaluating a documentation tool or solution
- Key considerations:
  - Integrate approaches from SE research (e.g., Treude, Maalej, Puhlfürß, Google’s Data Cards) with practices from the FAIR and RSE community.
  - Examine differences between data documentation in RSE and traditional software documentation.

## 2025-06-02: Interview with EuXFEL Data Analysis Group Leader

- Discuss current activities and challenges related to knowledge exchange
- Propose ideas for a study

## 2025-06-03: Internal Brainstorming

### **Study Context**

- User needs vary from basic API usage to in-depth understanding of dataset structure and analysis techniques.
- EuXFEL Data Analysis group provides:
  - Alias look-up files for easier navigation in HDF5 datasets
  - Technical documentation:
    - Existing resources include Data Management Plans (DMPs) and comprehensive instrument manuals.
    - New initiative: more high-level, user-friendly documentation

### **Study Objective**

- Personalized, on-demand documentation of complex scientific datasets for users
- Move from static documentation to an interactive, queryable knowledge base
  - RAG knowledge base aggregates manuals, DMPs, dataset documents, and more.
  - Enables personalized, adaptive responses to user prompts (simpler or more complex explanations).

## 2025-06-05: Doctoral Camp

Talk by Michael (DA group)

### **EuXFEL Data Policy and Derived Documents**

- Data Management Plans (DMPs) include service agreements (e.g., to define data size reductions)
- EuXFEL Data Format Specification (EXDF): structures HDF5 datasets

### **EXDF Tools**

- Support data reduction
- Example: graph neural network that predicts file relevance for users

### **DAMNIT Tool**

- Allows annotation of data points (e.g., marking importance).
- Provides data pipelines, compute jobs, and result caching.

## 2025-06-24: Interview with EuXFEL Data Analysis Group Leader

- Discuss focus of the study, focus of potential tool, and typical user questions

## 2025-07-16: RSE Day at DESY

- Connected with members of the Language Technology group at Uni Hamburg
  - Develop a pipeline-designed package for RAG system configuration:
    <https://github.com/uhh-hcds/encourage>
  - Potentially valuable for the project

## 2025-07-28: Internal Brainstorming

- Observation: RAGs and their configurations are well-researched.
- Proposed focus of our study:
  - Case study on RAG requirements engineering at EuXFEL
  - Focus on input/output specifications and integration with existing tools

## 2025-09-24: Internal Brainstorming

- Emphasize data documentation as the core project focus.
- A RAG tool focused on detector documentation could be suitable.
- Consider a follow-up meeting with EuXFEL DA group leader, Walid, and Tim to define the project topic.

## 2025-11-04: Project Focus Refinement

- Rather than building just a RAG for detector documentation, consider developing a tool that identifies data points with insufficient documentation.

## 2025-11-11: Interview with EuXFEL Control Group Manager

- Discuss user needs, potential tool features, any further technical information at EuXFEL (e.g., existing source code for RAG system)

## 2025-11-20: Begin of Intensive Research

### Forming First RQs

- RQ1: What knowledge-related challenges do users encounter when analyzing EuXFEL datasets and working with the available documentation?
- RQ2: How can a data-focused AI agent effectively address the challenges?

### Begin of Domain Research

- Structure and functionality of EuXFEL accelerator, instruments, and detectors
- EuXFEL Data Analysis group:
  - Responsibilities and activities
  - Publications (papers and posters)
  - Tools and documentation
- Tools
  - RAG systems
  - Model Context Protocol

## 2025-12-10: Interview with EuXFEL Controls Group Manager

- Exploration of current offline data analysis process, proposed tool, and planned study

## 2025-11-11: Meeting with UHH Supervisor

- Focus on scientific novelty important
- The current focus is too vague. Sounds rather like a consulting project.
- Eventually, focus on FAIR principles or other knowledge-related aspects.
- Methodology considerations: Action research might not be the best fit (as its focus is on the process, not the artifact).

## 2025-12-12: Interview with EuXFEL Data Analysis Group Manager

- Exploration of current offline data analysis process, proposed tool, and planned study

## 2025-12-16 Registration for EuXFEL User Meeting

- Registration of poster “AI Agent Support for Data Analysis” (T. Fuchs and L. Gelisio and S. Hauf and W. Maalej)

## 2026-01-07 Preparation of Focus Group 1 with DA Group

Activities:

- Restructuring RQs to align them with design science research:
- Literature review of guidelines, especially:
  - Kontio et al. (2004, 2008) about focus groups
  - Luke et al. (2014) about mind mapping
  - Davis et al. (2023)
  - Tong et al., (2007)
  - O’Brien et al. (2014)
- Structuring the first focus group session and collecting the questions for participants

## 2026-01-15 Execution of Focus Group 1

- 30 minutes execution
- 16 participants (13 in person, 3 via video conference) + 1 session host

## 2026-01-19 Meeting with DA group leader

- Debriefing of focus group 1 (discussed questions about certain statements during the session)
- Discussed the Users’ Meeting poster and questionnaire
- Outlined the next focus group
- Further recommendations:
  - Conduct interviews with instrument groups (but eventually do this already during Users’ Meeting)
  - Check EuXFEL’s Alfresco platform for company-internal documentation by instrument groups and others.

## 2026-01-22 and -26 EuXFEL’s Users’ Meeting

- Data workshop on the 22nd:
  - Presentations by the DA group provided further information, news, and resources regarding the data analysis processes (especially from the user perspective).
  - Link to event and further resources: <https://indico.desy.de/event/51446/overview>
- Poster session on the 26th:
  - Discussion with users, instrument scientists, and data scientists

## 2026-02-12 Meeting with DA group

- Objectives:
  - Discuss results of Users’ Meeting
  - Define next steps

## 2026-02-23 Research on Available EuXFEL Documentation

- Objective: Collect available documentation of EuXFEL that will be the basis of the RAG knowledge base
- Intermediate findings:
  - There are many resources that could be added to the knowledge base of our tool, especially public webpages of European XFEL. However, many of these webpages might already be included in the modern foundation model, such as GPT 5.
  - It makes more sense to focus the knowledge base on coding-specific resources of European XFEL, as recent breaking changes in their software will not be included in the foundation models.
  - For the first prototype, we will focus on available documentation for the `EXtra-data` library and any software specific to the scientific instrument `FXE` because the Data Analysis group recently published detailed documentation for this instrument.

## 2026-03-04 Prototyping for Version 1 of the Tool

- Objective: Create a prototype consisting of an RAG-based backend server and a Jupyter Lab + Jupyter AI frontend server. The RAG knowledge base should be focused on EXtra-data and any specific software of the FXE instrument.
- Intermediate findings:
  - We extended the `karabo-rag` project by EuXFEL. We implemented a more complex RAG pipeline for Sphinx-based documentation (for the EXtra-data library) and configured a Jupyter Lab server with a Jupyter AI extension that can query the RAG backend.
  - We presented the prototype during a meeting with the EuXFEL data scientists to receive feedback for improving the prototype.

## 2026-03-13 Rapid, Multivocal Literature Review

- Objective: to integrate lessons learned from similar studies into our requirements analysis by extracting requirements for our tool from these studies
- Activities: Review scientific and non-scientific literature with a rapid, AI-assisted literature review
- Intermediate findings:
  - We created multiple Python scripts to establish a pipeline consisting of (1) identification of papers, (2) screening of papers, (3) processing eligible papers, and (4) conducting a thematic analysis to extract requirements.
  - The thematic analysis was supported by LLMs (the proprietary model GPT-5.4-mini and the open-source model Minimax-M2.5):
    - From the 250 unique papers identified, 224 were relevant for analysis. From these papers, GPT 5.4 mini extracted 3062 requirements, while Minimax-M2.5 extracted 2303 requirements.
    - The subsequent thematic analysis with GPT-5.4-mini resulted in 26 themes.
  - We manually reviewed the quality of extracted requirements and synthesized themes. We found that the quality of requirements extracted by the LLMs was generally good, while many themes were overlapping.
  - We reworked the themes by extracting 16 requirements from them that were most relevant for our tool. 10 of these requirements were already stated by EuXFEL staff and users, while the other 6 requirements have a more general-purpose focus and will support the implementation of the tool.

## 2026-03-29 Comparison of Candidates for the Components of the Agentic AI System

- Objective:
- Intermediate findings:

## 2026-04-14 Presentation of Intermediate Results for Candidates and Agentic AI System

- To whom: both EuXFEL managers
- How: 60-minute meeting
- What? See [meeting procotol](/08-prototype-second-version/evaluation/01-meeting-euxfel-managers.md).

## 2026-04-20 Presentation of Second Prototype to Data Analsis Group

- How: 30-minute meeting
- Objective: Invite group members (and interested scientists) to a user study

## 2026-04-22 Start of User Study

- Overall, 12 participants
  - 8 people with profession in data science or software engineering
  - 4 instrument scientists
