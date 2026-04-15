# Notes of Focus Group 1 with EuXFEL Data Scientists

Date: 2026-01-15

## Participants

- 1 interviewer
- 13 data scientists in-person
- 3 data scientists via Zoom

## Intro

- PhD project in informatics at uni HH, EuXFEL/DASH
- Knowledge exchange, focus groups
- problem-focused: questionnaire about challenges in knowledge exchange
- solution-focused: AI-powered VS Code extension to generate documentation comments in code
- solution-focused: AI-powered knowledge base to accelerate information retrieval from issue trackers and documents
- solution-focused: AI-powered tool to support users during offline data analysis

- 3 research questions:
  - What knowledge-related challenges in offline data analysis?
  - Which requirements are there for an AI agent?
  - What design recommendations can be derived in practice?

- Today focus on problem identification
- Artifact: mind maps

- Side note: AI round table at DESY, someone in HH is doing exactly this, resulting in a chat tool with Jupyter notebook extension

## Interactive/discussion part with live mind-map editing

### Tools

What tools do users use?

- Notebooks (Max-Jhub), EXtra, DAMNIT, (myMdC, Zulip/myLog - proposal DA-related communication, and results)
- Wrappers around community tools
- Also, instrument-specific tools, build upon our libraries, e.g., SCS toolbox
- Own tools by users - problem support and documentation by different actors

### Current process

- How does it start and end?
  - Different between instruments and also sometimes within instrument
  - "Starts with data, ends with plot"
  - Hard to standardize; sometimes it start with migration to Maxwell, but not always
  - Usually, data collection is the 1st step
  - Often: open Jupyter notebook with EXtra. DA framework is the most stable thing to start with.
  - This is a process of optimization, getting the best signal out of the data
  - It is 2-goal-oriented: data collection, and getting information out of the logs, e.g., on which runs are needed - different runs required for detector calibration purposes vs. data analysis
  - The choice of interface differs also between techniques, SFX users often don't use notebooks
- Whom do external users contact on the different steps?
  - Beamline staff, sometimes it's us
  - Communication on myLog
- If they are using notebooks, how do they work?
  - Experienced users insist on using their notebooks
  - Others need help and appreciate template notebooks
  - Templates and custom notebooks can be provided
  - Before the experiments, it is sorted out what we have and what they need, preparation of things missing
  - Users rarely start from scratch, but often they need to build things on top

### Documentation

- Interviewer looked at our existing docs resources, listed them, and asks if something was missing.
- More specific:
  - Instrument-specific docs
  - technique-oriented documentation
- Calibration docs are not written for users and thus likely not interesting from them (but public, and maybe worthwhile to be harvested by AI)
- Relevant artifacts: publications (e.g., Xwiz paper contains tutorial section)

### Challenges

What are typical support use cases during offline analysis?

- How to access/read the data
- Not familiar with infrastructure complexity
- Sometimes users are even unsure about what quantities to compute from the data
- Special cases when conducting non-established experiments
- Challenge of data scale. Anecdotical reference: "they cannot even calculate a mean"  
- Mismatch of what we vs. users expect from opening the data
- Reading data vs. interpreting data

What are challenges for the DA members?

- Single functionalities are well documented, but putting them together in a user-centric practical workflow is a challenge
- It is also a question of familiarity, experience, and learning over years
  - But good documentation facilitates and accelerates this process
- Textbook vs. cookbook information
- Understanding what the users want is a challenge
- Is support availability a problem?
  - We have our tools to solve this problem.
  - We cannot debug 1000 lines of user code, but we can support with the obvious things. We have to find middle ground.

Are there other stakeholders?

- Instrument scientists
- The data analysis support by instrument staff varies a lot.
  - Sometimes, single scientists have invested more time than the users themselves.
- The variety and range of user experience and requirements is much larger than in other domains, e.g., experiments at radio telescopes are more structured.
