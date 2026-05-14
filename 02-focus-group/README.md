# Focus Group with Data Analysis Group

Date: 2026-01-15

## Mind Maps

- [Initial version](01-focus-group-initial-mindmap.pdf)
- [Final version](02-focus-group-final-mindmap.pdf)

## Participants

- 1 interviewer
- 16 group members

## Intro

- Study: AI-powered tool to support users during offline data analysis
- Research questions:
  - What knowledge-related challenges in offline data analysis?
  - What requirements must an AI agent meet to address challenges?
  - What design recommendations can be derived?
- Today:
  - Focus on problem identification
  - Interactive discussion; results documented in a mind map

## Tools

- Tools that users use during offline data analysis:
  - [Jupyter Hub on Maxwell HPC cluster](https://doi.org/10.1007/s41781-021-00058-y)
  - Python libraries by Data Analysis, e.g., EXtra-data, [EXtra-xwiz](https://doi.org/10.3390/cryst13111533)
  - Instrument-specific tools, e.g., SCS toolbox
  - Community tools, e.g., CrystFEL
  - EuXFEL tools to collect and visualize experiment metadata:
    - [myMdC](https://doi.org/10.18429/JACOW-ICALEPCS2025-THCR005)
    - [myLog](https://doi.org/10.18429/JACOW-ICALEPCS2025-THMG013)
      - Customized Zulip messenger with streams (proposals) and channels (Data Analysis, etc.)
      - Used for any proposal-related communication and metadata taken during the experiment
      - myLog content is also presented on myMDC.
    - DAMNIT
  - Other tools by users (self-developed or from other facilities)

## Current Process

- Questions:
  - What are the typical process steps of users to accomplish offline data analysis?
  - How do users typically start their notebook with? Totally blank? Template from DA/instruments? Cookbook recipe?

- Process is hard to standardize.
  - Exact processes differ between instrument groups and even experiments within one instruments group.
  - E.g., users of the SFX instrument do not use Jupyter notebooks.
  - Common denominator: "It starts with data and ends with plots."

- Common process:
  1. Collect data during DAQ (data acquisition) process
     - Metadata is stored in myMDC.
  2. Migrate data from online to offline data analysis storage
  3. Analyze experiment logs
     - With myLog, myMDC, and DAMNIT
     - To classify the relevance of different experiment runs
     - Some runs are required for data calibration processes, others for actual data analysis.
  4. Exchange with staff from Data Analysis and instrument group on how to analyze the data
     - Exchange via:
       - In-person chat
       - myLog
       - Rare: ticket system (Redmine)
     - Support by instrument group:
       - Each group usually has at least one person with strong data analysis skills.
       - Often, they act as a proxy for the Data Analysis group.
     - Support by Data Analysis group:
       - Recommend a data analysis process
       - Especially for non-standard processes not contained in templates
  5. Set up analysis:
     - Most stable thing to start with: Jupyter notebook via JupyterHub on Maxwell cluster + software from Data Analysis group
     - Hardware options:
       - Maxwell HPC cluster
       - User's own computation environment
     - Software config:
       - Templates:
         - Users rarely start from scratch. Often, they use templates:
           - Data Analysis can provide templates and custom notebooks.
           - Experienced users insist on using own notebook templates.
           - Others need help and appreciate our template notebooks.
         - Template options:
           - None
           - From Data Analysis group, specific to one type of experiment at EuXFEL
           - User's own template
       - Libraries and environments:
         - Python libraries and environment by Data Analysis group
         - Instrument-specific tools, e.g., SCS toolbox
         - Community tools, e.g., CrystFEL
         - User's own libraries and environment
  6. Analyze the data. Examples:
     - Check if data is calibrated correctly
     - Optimize the analysis to receive best signal from the data
     - Produce data plots  

## Documentation

- Questions:
  - What documentation do users require when analyzing the data (e.g., DA documentation, instrument documentation)?
  - Where is this documentation located?
  - From whom do users receive the documentation?

- Documentation by Data Analysis group
  - General docs
    - [DA webpage of EuXFEL website](https://www.xfel.eu/organization/scientific_and_technical_groups/data_department/data_analysis/documentation_and_training_material/index_eng.html)
    - [User documentation](https://dataanalysis.pages.xfel.eu/user-documentation/)
    - Docs of software libraries, e.g.:
      - [EXtra](https://extra.readthedocs.io/en/latest/)
      - [EXtra-data](https://extra-data.readthedocs.io)
      - [EXtra-geom](https://extra-geom.readthedocs.io/en/latest/)
      - [DAMNIT](https://damnit.readthedocs.io/)
    - [GitLab](https://git.xfel.eu) and [GitHub](https://github.com/European-XFEL) repositories of EuXFEL
    - [Offline calibration website](https://calibration.pages.xfel.eu/pycalibration/)
      - Not written for users and thus likely not interesting from them
      - But public and eventually still relevant for AI system
  - Instance-specific docs
    - [Redmine tickets](https://redmine.xfel.eu/) (with problem and solution description)
    - DA recommendations added in experiment proposals
- Documentation by instrument groups
  - Instrument-specific docs, e.g., [SCS](https://scs.pages.xfel.eu/documentation/index.html) and [SCS Toolbox](https://scs.pages.xfel.eu/toolbox/index.html) (but docs of instruments vary in detail)
  - Technique-oriented documentation by DA (currently available for [FXE](https://dataanalysis.pages.xfel.eu/techniques-docs/fxe/) and [SQS](https://dataanalysis.pages.xfel.eu/techniques-docs/sqs/))
  - Technical reports on EuXFEL website, e.g, for [SPB/SFX](https://www.xfel.eu/facility/instruments/spb_sfx/documentation/index_eng.html)
- [Maxwell documentation](https://docs.desy.de/maxwell/documentation)
- Publications by Data Analysis and instrument groups
  - E.g. [EXtra-xwiz paper](https://doi.org/10.3390/cryst13111533) contains tutorial section

## Challenges

- Questions:
  - What are knowledge-related challenges during offline data analysis (e.g., documentation, communication and support, clarity of tool features, requirements of users):
    - For users?
    - For DA members?
    - For other EuXFEL members, e.g., instruments groups?
  - What are the biggest challenges at the moment?

- Challenges of users:
  - In general: The range of user experience and variety of requirements are much larger than in other domains.
    - E.g., experiments at telescopes are more structured.
  - Initially unclear objectives for data analysis
  - Contractual constrainsts: limited support by EuXFEL during offline data analysis phase
    - We cannot debug 1000 lines of user code.
    - But we can support with the obvious things.
  - Mismatched expectations regarding complexity of data analysis process
    - How to read and manipulate the data
    - How to interpret the data
  - Unfamiliarity with infrastructure complexity
  - Unfamiliarity with HPC
    - Especially regarding performance requirements of the code
    - "Some cannot even calculate a mean."
  - Unfamiliarity with complex, heterogeneous, somtimes novel analysis procedures of instruments and types of experiments
    - Especially when conducting non-established experiments
    - Good documentation facilitates and accelerates this process
  - Composing the scattered documentation for a specific analysis objective
    - Single functionalities are well documented, but putting them together in a user-centric practical workflow is a challenge.
    - But users rather need "cookbook recipes".

- Challenges of DA members:
  - Unfamiliarity with complex, heterogeneous, somtimes novel analysis procedures of instruments and types of experiments
    - Requires learning over years
  - Composing the scattered documentation for a specific analysis objective
  - Understand analysis objectives of users
  - Time effort for supporting users

- Challenges of instrument scientists:
  - Understand analysis objectives of users
  - Time effort for supporting users
    - The data analysis support by instrument staff varies a lot.
    - Sometimes, instrument scientists invest more time in the analysis than the users themselves.

## Further Information

- Recently, AI round table at DESY: DKRZ is working on a similar project (including a Jupyter notebook extension).
