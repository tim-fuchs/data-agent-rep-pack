# Focus Group with Data Analysis Group of EuXFEL

Date: 2026-01-15

## Participants

- 1 interviewer
- 13 data scientists in-person
- 3 data scientists via Zoom

## Intro

- Study: AI-powered tool to support users during offline data analysis
- Research questions:
  - What knowledge-related challenges in offline data analysis?
  - What requirements must an AI agent meet to address challenges?
  - What design recommendations can be derived?
- Today: focus on problem identification
- Process: interactive discussion with live editing of a mind map

## Tools

- What tools do users use during offline data analysis?
  - JupyterHub on Maxwell HPC cluster
  - EXtra Python libraries
  - DAMNIT
  - myMdC
  - myLog
    - Customized Zulip messenger with streams (proposals) and channels (Data Analysis, etc.)
    - Used for any proposal-related communication and metadata taken during the experiment
    - myLog content is also presented on myMDC.
  - Instrument-specific tools built upon EuXFEL libraries, e.g., SCS toolbox
  - Community tools, e.g., CrystFEL
  - Other tools by users (self-developed or from other facilities)

## Current Process

- Interview questions:
  - How does offline data analysis start and end?
  - Whom do users contact during the different steps?
  - If users use Jupyter notebooks, what content do notebooks typically have?

- Process is hard to standardize.
  - Exact processes differ between instrument groups and even experiments within one instruments group.
  - E.g., users of the SFX instrument do not use Jupyter notebooks.
  - Common denominator: "It starts with data and ends with plots."

- Common process:
  1. Collect data during DAQ (data acquisition)
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
     - Software config:
       - Template options:
         - Users rarely start from scratch. Usually, they use templates.
           - Data Analysis can provide templates and custom notebooks.
           - Experienced users insist on using own notebook templates.
           - Others need help and appreciate our template notebooks.
         - Template options:
           - None
           - From Data Analysis group, specific to one type of experiment at EuXFEL
           - User's own template
       - Libraries and environments:
         - Python libraries and environment by Data Analysis group
         - User's own libraries and environment
     - Hardware options:
       - Maxwell HPC cluster
       - User's own computation environment
  6. Analyze the data

- If users use Jupyter notebooks, what content do notebooks typically have?
  - Before the experiments, it is sorted out what the users require and what the facility can offer.
  

## Documentation

- Interviewer looked at our existing docs resources, listed them, and asks if something was missing.
- More specific:
  - Instrument-specific docs
  - technique-oriented documentation
- Calibration docs are not written for users and thus likely not interesting from them (but public, and maybe worthwhile to be harvested by AI)
- Relevant artifacts: publications (e.g., Xwiz paper contains tutorial section)

## Challenges

- What are typical support use cases during offline analysis?
  - How to access/read the data
  - Not familiar with infrastructure complexity
  - Sometimes users are even unsure about what quantities to compute from the data
  - Special cases when conducting non-established experiments
  - Challenge of data scale. Anecdotical reference: "they cannot even calculate a mean"  
  - Mismatch of what we vs. users expect from opening the data
  - Reading data vs. interpreting data

- What are challenges for the DA members?
  - Single functionalities are well documented, but putting them together in a user-centric practical workflow is a challenge
  - It is also a question of familiarity, experience, and learning over years
    - But good documentation facilitates and accelerates this process
  - Textbook vs. cookbook information
  - Understanding what the users want is a challenge
  - Is support availability a problem?
    - We have our tools to solve this problem.
    - We cannot debug 1000 lines of user code, but we can support with the obvious things. We have to find middle ground.

- Are there other stakeholders?
  - Instrument scientists
  - The data analysis support by instrument staff varies a lot.
    - Sometimes, single scientists have invested more time than the users themselves.
  - The variety and range of user experience and requirements is much larger than in other domains, e.g., experiments at radio telescopes are more structured.

## Further Information

- Recently, AI round table at DESY: DKRZ is working on a similar project (including a Jupyter notebook extension).
