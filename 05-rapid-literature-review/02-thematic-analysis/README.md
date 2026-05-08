# Thematic Analysis of Relevant Articles

## Purpose

This folder contains:

- Summary of the thematic analysis (see below)
- Scripts:
  - Analyze the relevance of articles for the research question of the literature review
  - Extract requirements from the articles
  - Synthesize requirements into themes
  - Notes: The scripts use LLMs to conduct the analysis automatically.

## Usage

1. Read the summary of the thematic analysis below.
2. Optionally, repeat the thematic analysis:
   - Follow the installation process below.
   - Create the folder `data/articles`.
   - Copy the files from the `markdown_cleaned` (or `markdown`) folder of the previous inclusion process. Paste them into the `articles` folder.
   - Run `python scripts/analyze_relevance.py` to analyze the relevance of the articles in `data/articles`:
     - Exports one CSV per enabled analyzer: `data/relevance_openai.csv` and/or `data/relevance_nebius.csv`.
     - For each article, the analyzers run in parallel.
   - Run `python scripts/analyze_requirements.py` to extract requirements from the same articles:
     - Exports one CSV per enabled analyzer: `data/requirements_openai.csv` and/or `data/requirements_nebius.csv`.
     - For each article, the analyzers run in parallel.
   - Run `python scripts/combine_relevance.py` to combine the relevance scores of multiple analyzers:
     - Discovers `data/results/relevance_*.csv` files dynamically and builds provider columns such as `relevance_score_openai`.
     - Writes `data/results/relevance_combined.csv` with columns `article_ID`, dynamic provider score columns, `mean`, and `std`.
   - Run `python scripts/combine_requirements.py` to merge requirement rows from multiple analyzers:
     - Discovers `data/results/requirements_*.csv` files dynamically.
     - Writes `data/results/requirements_combined.csv`.
   - Run `python scripts/synthesize_thematically.py` to perform a two-pass thematic analysis:
     - Process:
       - Reads `data/results/requirements_combined.csv`.
       - Assigns an `initial_theme` per requirement.
       - Consolidates initial themes to `final_theme` labels, which should not overlap with each other.
       - Detects (near-)duplicate requirements per article and assigns the same thematic label to them.
       - Writes `data/results/synthesis_thematically_initial.csv` and `data/results/synthesis_thematically_final.csv`.
     - Note:
       - The creation of final themes might take a while and the result could contain flaws, depending on the choice of LLM.
       - If you already created the `synthesis_thematically_initial.csv` file and only want to repeat the final theme consolidation, use the `--skip-initial-themes` option: `python scripts/synthesize_thematically.py --skip-initial-themes`
   - Run `python scripts/synthesize_summary.py` to create a summary of the literature review.
     - Reads `data/results/synthesis_thematically.csv` and `data/results/relevance_combined.csv`.
     - Writes `data/results/synthesis_summary.md` by listing all themes, each with a prose summary of the theme, and a table of the corresponding requirements and the IDs and relevance scores of the articles they appear in.
   - Manually analyze the `synthesis_summary.md` file and extract themes and requirements that appear truly relevant to the research question of the literature review.

## Install

1. Create a `.env` file that contains the content of the `.env.example` file.
2. Configure `ANALYZERS` in `.env`:
   - `openai,nebius` runs the analysis of article relevance and requirements with two LLMs in parallel, one from the model provider OpenAI and one from Nebius Token Factory.
   - `openai` runs one LLM provided by OpenAI.
   - `nebius` runs one LLM provided by Nebius Token Factory.
3. Add provider credentials and model settings in `.env`:
   - Generate API key from OpenAI and/or Nebius Token Factory to access their models.
   - The `OPENAI_*` and `NEBIUS_*` entries are for the relevance and requirement analyses. Configure the entries for the providers you selected as analyzers.
   - The `SYNTHESIS_*` entries are for synthesizing the extracted requirements into themes.
4. Create a virtual environment, activate it, upgrade pip, and install the required packages: `python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt`.

## Summary of Thematic Analysis

### Overview

- Automatic process:
  - Analysis of 224 articles
  - Extraction of 5365 requirements (with near-duplicates)
    - 3062 from GPT-5.4-mini
    - 2303 from Minimax-M2.5
  - Synthesis of 26 themes, each representing a requirement
- Manual rework resulting in 18 themes

### Final Themes

**Agentic AI system shall ...**

**Access the HPC cluster**

- [c-q2-01] It is implemented in a non-intrusive way, that is, not interfering with the users’ original notebook and allowing interaction with the AI assistant through a side panel
- [c-q2-01] we conduct our study in a computational notebook (Jupyter) environment, given its popularity among data scientists
- [c-q5-12] The wizard acted as the backend of an AI assistant, carefully crafting and timing suggestions to analysts working through a data analysis task in a customized JupyterLab notebook.
- [c-q2-06] The design space encompasses interface locations ranging from ambient text-based suggestions to targeted cell-based or side-panel approaches, reflecting different trade-offs between discoverability, obtrusiveness, and user control. [...] It is implemented in a non-intrusive way, that is, not interfering with the users’ original notebook

**Interact with notebook content**

- [c-q2-01] The user can interact with the code recommendation using the following actions: *accept* the recommendation, *reject* the recommendation, *edit* the recommendation, and *save* the recommendation for later use.
- [c-q2-01] they can insert it into the cell with a click of a button

**Generate code optimized for high-performance computing**

- [s-q2-p1-09] LLM-based code generation agents can generate unit tests, integration tests, and security test cases based on requirements, code, and related documentation, as well as execute automated testing processes
- [s-q2-p1-09] The reflection component allows agents to examine, evaluate, and correct their own generated content or existing data, thereby improving past action decisions and correcting previous errors for continuous improvement
- [s-q2-p1-08] the agent is capable of producing optimized versions of the code while preserving its intended functionality.
- [s-q2-p1-08] It generates recommendations for refining algorithms, reducing redundancy, improving computational efficiency, and restructuring code where beneficial.

**Test code for correctness and safety risks**

- [s-q3-p1-08] Verification mechanisms constitute the quality control layer of LLM-based scientific agents, implementing critical safeguards against hallucination, logical inconsistencies, factual inaccuracies, and procedural errors
- [s-q3-p1-08] until the Verifier confirms that the output meets standards of validity and reproducibility
- [s-q2-p1-01] The AI programming assistant queries the underlying LLM to generate a pool of candidate code and test suggestions using the natural language prompt provided by the user in step 1.

**Request user feedback to guide and improve solutions**

- [s-q2-p3-10] Notably, the talk command enables sending natural language messages (not interpreted as commands for repository actions), the ask command is used to request user feedback, and the stop command interrupts the process, indicating goal achievement or the inability of the agents to proceed further.
- [s-q2-p3-10] AutoDev enables users to define complex software engineering objectives, which are assigned to AutoDev’s autonomous AI Agents to achieve.
- [g-q1-p3-08] Users engage interactively with the explanation, raising critiques, clarifications, or alternative perspectives.  

**Adapt code style and explanations to the user's expectations**

- [c-q4-08] and be capable of following user-speciﬁed coding style guidelines.
- [c-q4-08] AI-supported code completion tools should be able to identify the coding style followed and adapt its code suggestions.
- [c-q4-11] AI-based code assistants should ideally generate code that readily fits into the target project.

**Generate code documentation on project- and code-level**

- [s-q3-p3-03] With Comprehension, we give a measure on how hard or easy the code is to comprehend. Here, we focus on the quality of comments and documentation the tool generated.
- [s-q2-p1-10] It can also fluently generate comments, messages, and documentation.
- [a-05] The predefined prompt tool consistently provided concise Docstrings that participants perceived as more readable and contained less non-informative content compared to the output of the ad-hoc prompt tool.

**Request human approval for sensitive actions**

- [g-q3-p3-02] we advocate restricting autonomous operations to well-characterized, lower-risk scenarios where safety parameters and operational boundaries have been thoroughly validated through empirical testing and expert review.
- [s-q2-p3-10] These files define the available commands (actions) that AI agents can perform. Users can leverage default settings or fine-grained permissions by enabling/disabling specific commands, tailoring AutoDev to their specific needs.
- [s-q1-p3-10] providing regular updates on plans, progress, and potential issues to ensure robust oversight and enable informed intervention when necessary.

**Access relevant context information within a project**

- [g-q3-p1-07] Long-term memory stores essential and factual knowledge that underpins agent behavior and understanding of the world, ensuring this information persists beyond task completion. [...] Short-term memory allows agents to temporarily acquire skills, such as tool usage, store information about recent states of a biological system, and keep track of outcomes from earlier reasoning efforts.
- [c-q4-14] integrates retrieved content, user interaction history, and contextual information to generate effective prompts

**Decompose a request into verifiable goals**

- [c-q5-12] Planning assistance helps analysts reason about the analysis decisions. This can occur as analysts are explicitly planning their decisions (B) or even during execution when analysts are unaware of plausible alternatives (C).
- [s-q2-p3-10] Following the rules and actions configuration, the user specifies the software engineering task or process to be accomplished by AutoDev. [...] Planning and multi-step reasoning form the foundation of an LLM agent's ability to tackle complex tasks effectively which enables agents to decompose problems into smaller, more manageable subtasks and create strategic execution paths toward solutions
- [c-q2-01] an AI-based coding assistant that provides explicit alternatives as recommendations throughout the data science workflow.
- [c-q2-10] the Stepwise system decomposes the task into separate steps (visually similar to a computational notebook), displaying editable assumptions and their corresponding code one step at a time until the task is complete. [...] the Phasewise system decomposes the problem into three editable, logical phases: structured input/output assumptions, execution plan, and code.

**Work with up-to-date information**

- [c-q4-14] Our proposed testing methodology integrates a context- based RAG mechanism that interacts dynamically with local coding envi - ronments and retrieves contextual information as an enhancement to the LLMs prompts.
- [c-q3-16] The search engine facilitates three depths of inquiry: (1) broad academic database searches via the APIs for Semantic Scholar, OpenAlex, and PubMed, (2) within-text multi-article d-RAG queries (akin to 'PaperQA-2'), and (3) paper-specific question-answering  

**Close tasks with narrative summaries and recommended next steps**

- [c-q2-20] Narrative summaries: Using Natural Language Generation (NLG), Copilot produces Smart narrative text blocks that summarize the data in clear, everyday language.
- [c-q2-16] Meeting Summaries Automatically generates concise summaries of Teams meetings with key points, decisions, and action items.

**Provide citations, confidence levels, and verification steps**

- [c-q1-18] Transparent explanations, uncertainty indicators, and clearly communicated limitations
- [c-q1-18] Tools that integrate deep contextual awareness and provide transparency in the reasoning behind code suggestions are particularly valued for reducing uncertainty and fostering appropriate trust
- [c-q3-08] generating hypotheses and estimating their uncertainty to suggest relevant experiments

**Report conversations between user and agent to EuXFEL staff**

- [s-q2-p3-10] The Conversation Manager, responsible for initializing the conversation history, plays a pivotal role in overseeing the high-level management of the ongoing conversation.
- [s-q1-p3-09] These logs include content, context, and nuances of interactions, enabling the AI to construct and retrieve a rich, conversational history.
- [s-q1-p3-09] This conversational data is subsequently processed and stored within a dedicated database.

**Assist in drafting scientific manuscripts**

- [s-q3-p1-03] We demonstrated that the AI scientist v2 is capable of autonomously generating manuscripts that successfully pass peer review at a workshop of a major machine learning conference.
- [c-q3-15] assisting in the generation of text and the organization of manuscripts with speed and fluency.

**Recommend using a version control system**

- [c-q2-10] once an edit is submitted, our system introduces a new branch to preserve the original, unedited version, while incorporating the edited version in the “main” branch.

**Optimize latency**

- **[s-q3-p1-03]** An LLM is used to generate the plan and experiment code for each new child node, after which all new nodes are executed concurrently in parallel, significantly accelerating the exploration process.
- **[s-q3-p1-03]** For each selected idea, the system autonomously executed the full experimental pipeline using the parallelized agentic tree search (§3.2.2) multiple times, each initiated with a different random seed.
- **[s-q3-p2-07]** Although the parallelized mode accelerates improvements in wall-clock time, it introduces trade-offs between speed and computational efficiency.
- **[s-q3-p2-07]** We introduce a parallelized mode for AgentRxiv, allowing multiple agentic systems to run simultaneously and share findings.
- **[s-q1-p2-03]** Orchestrator (policy engine): A stateless, horizontally scalable service that evaluates routing decisions on every dialog turn.
- **[s-q1-p2-03]** The orchestrator must route between autonomous LLM responses, tool augmented generation (RAG, KB search, workflow APIs), and human collaboration (agent assist, supervised approval, or escalation) using signals such as intent class, risk score, user tier, coverage of cited evidence, live latency, token/$ budgets, and agent availability.

**Not share user data with third parties**

- [c-q2-13] Ethical concerns—including data privacy, bias, and transparency—also influenced user trust and adoption levels
- [c-q2-13] we’re using our own instance of CoPilot. There’s nothing that’s leaving the organisation.
