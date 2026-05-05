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

### Overview of Automatic Process

- 224 articles analyzed
- 5365 requirements extracted (with near-duplicates)
  - 3062 from GPT-5.4-mini
  - 2303 from Minimax-M2.5
- 26 themes

### Themes and Requirements After Manual Rework

**01 Information Retrieval: Agent shall retrieve up-to-date code-related information from public and private resources.**

- **[c-q4-14]** Our proposed testing methodology integrates a context- based RAG mechanism that interacts dynamically with local coding envi - ronments and retrieves contextual information as an enhancement to the LLMs prompts.
- **[c-q3-16]** The search engine facilitates three depths of inquiry: (1) broad academic database searches via the APIs for Semantic Scholar, OpenAlex, and PubMed, (2) within-text multi-article d-RAG queries (akin to 'PaperQA-2'), and (3) paper-specific question-answering  
- [s-q3-p1-08] External knowledge bases expand the agent's informational scope by integrating up-to-date and domain-specific data, allowing for retrieval, synthesis, and contextualization of complex scientific concepts.
- [g-q3-p1-01] Agentic AI involves using a large language model (LLM) to carry out multi-step tasks, by connecting it to external tools such as Internet browsers or coding suites.
- [s-q3-p3-10] The ability of LLMs to interact with external tools through function calling is fundamental for building intelligent agents capable of delivering real-time, contextually accurate responses
- [s-q2-p1-09] The tool usage module greatly enhances their action space by granting agents permission to invoke external functions or APIs.
- [s-q2-p2-03] LLM-based agents have emerged [9, 10], combining the strengths of LLMs with external tools and resources to enable more dynamic and autonomous operations.

**02 Tool Integration: The agent shall integrate into existing environment (Jupyter Lab on HPC cluster), not disrupt user workflows, and not require copy-paste interactions.**

- **[c-q2-06]** The design space encompasses interface locations ranging from ambient text-based suggestions to targeted cell-based or side-panel approaches, reflecting different trade-offs between discoverability, obtrusiveness, and user control. [...] It is implemented in a non-intrusive way, that is, not interfering with the users’ original notebook
- **[c-q2-06]** All participants believed it is valuable to adapt code assistants to notebooks.
- [c-q1-20] Using CoPilot as a pair programmer to ask questions and get help with functions and syntax in the IDE without switching to external sources like API specs, Google or Stack Overflow, etc.
- [c-q4-11] Copilot works within the IDE by analyzing the context of the code being written, including variables, functions, and surrounding code, to provide code suggestions.
- [g-q2-p1-06] GitHub Copilot Chat is not just a chat window. It recognizes what code a developer has typed, what error messages are shown, and it's deeply embedded into the IDE.
- [c-q2-11] AI copilots must be intuitive, non-intrusive, and context-aware, allowing users to interact seamlessly across platforms.
- [c-q1-05] their integration with the development environment is fundamental as well.
- [c-q1-05] developers sometimes perceive the automatic suggestions as intrusive.
- [c-q5-19] Copilot can be integrated with more IDEs
- [g-q2-p2-04] easy integration options with other developer tools
- [c-q2-09] AI insights surface within familiar interfaces —Excel spreadsheets display predictive analytics, Word documents incorporate automated summaries, and Teams meetings feature real-time transcription.
- [c-q2-06] successful notebook-based code assistants require careful adaptation to this specific computing environment. [...] It is worth mentioning that the corporation achieved true interoperability across its ecosystem. Data flows between services without format conversions or manual transfers.
- [s-q2-p2-05] Challenges with AI integration and usability in development environments (raised in 3% of all responses) and Workflow disruption (raised in 2.1% of responses) should be addressed by companies who provide AI assistants for the market
- [c-q2-05] the general lack of tool integration meant that there was a substantial amount of copy-paste to move text and code between different windows.
- **[c-q2-01]** we conduct our study in a computational notebook (Jupyter) environment, given its popularity among data scientists
- **[c-q2-01]** It is implemented in a non-intrusive way, that is, not interfering with the users’ original notebook and allowing interaction with the AI assistant through a side panel
- [c-q1-18] systems integrated into Jupyter notebooks... that assist data scientists by suggesting analytical next steps, facilitating iterative development, and reducing cognitive load during complex data-analysis tasks

**03 Code Generation and Validation: The agent shall generate, format, and execute code, test for correctness, iteratively improve solutions, and avoid hallucinations and security vulnerabilities.**

- [a-07] Participants also spoke about a need to verify generative AI responses for correctness, quality, and hallucinations.
- [s-q3-p3-03] Factual correctness is of utmost importance, and writing that does not adhere to the rigorous standards of scientific integrity should not be considered part of the body of scientific knowledge
- [g-q3-p3-04] Hallucination and factuality: LLMs routinely generate plausible but incorrect content ("hallucination") and suffer from outdated or inconsistent knowledge bases
- [g-q2-p2-03] AI tools like Claude Code that generate correct code on the first pass and fit naturally into existing workflows earn praise; whereas tools that require constant correction quickly lose favor
- [s-q2-p2-03] Hallucination is another main concern, where the model generates code that appears plausible but is actually incorrect or nonsensical
- [s-q2-p2-05] AI-generated output is inaccurate was highlighted by 17.7% of responses.
- [s-q3-p1-08] until the Verifier confirms that the output meets standards of validity and reproducibility
- [c-q5-05] human reviewers were often unable to identify hallucinations in unfamiliar domains without explicit verification steps, emphasizing the need for structured review processes for AI -generated code
- [s-q1-p3-03] effective quality control mechanisms, such as automated verification, static analysis, and model-aware debugging tools, are emphasized as critical to responsible adoption
- [s-q3-p1-01] On examination, we found that the in-text citations were incorrect and the references in the list were fabricated by the application
- [c-q6-10] The findings suggest that AI tools can greatly enhance academic work when used with proper verification and structured commands
- [s-q2-p3-09] we carefully designed prompts to ensure responses (ii) are technically correct
- [s-q2-p3-07] Measure of how well the technique performs in generating correct and functional code
- [c-q2-20] Accuracy of output - the correctness and completeness of the response relative to the expected insight.
- [c-q5-10] Quality of Output as the alignment of generated solutions with expected outcomes, particularly for visualization tasks
- [g-q3-p2-09] As the system spends more time reasoning and improving, the self-rated quality of results improve and surpass models and unassisted human experts.
- [g-q3-p2-09] These agents use automated feedback to iteratively generate, evaluate, and refine hypotheses, resulting in a self-improving cycle of increasingly high-quality and novel outputs.
- [s-q2-p3-10] This category also encompasses validation tools such as linters and bug-finding utilities.
- [c-q3-05] Any errors detected during the validation are iteratively corrected by the LLM, achieving a syntax validation success rate of ∼97% within three iterations in a benchmark data set of 66 examples for inorganic synthesis.
- [c-q4-15] It's worth considering the integration of automated security testing tools (if not already implemented), such as Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST), into the development workflow when utilizing GitHub Copilot.
- [s-q2-p1-05] we also assess additional properties such as the time cost (detecting DoS vulnerability), the memory access validity (detecting various memory-related vulnerabilities in low-level languages like C), and the side-effect or integrity of data (detecting SQL injection vulnerability).

**04 Controlled Autonomy: The agent shall operate under explicit permissions and require human approval for sensitive actions, such as file deletion and code execution on the HPC cluster.**

- **[g-q3-p3-02]** we advocate restricting autonomous operations to well-characterized, lower-risk scenarios where safety parameters and operational boundaries have been thoroughly validated through empirical testing and expert review.
- [g-q2-p3-06] Tools with agentic workflows that execute multiple tasks autonomously without any human oversight were excluded.
- **[s-q2-p3-10]** These files define the available commands (actions) that AI agents can perform. Users can leverage default settings or fine-grained permissions by enabling/disabling specific commands, tailoring AutoDev to their specific needs.
- [g-q1-p2-07] Both data sources show that human input was essential to clarify technical details, ensure contextual accuracy, and validate prioritization results.
- **[s-q1-p3-10]** providing regular updates on plans, progress, and potential issues to ensure robust oversight and enable informed intervention when necessary.
- [c-q3-16] installation confined to isolated virtual environments to minimise potential global environment contamination.
- [g-q3-p1-01] Another way to protect against agents going awry is keep them in 'containers' that limit the actions they can take or information they can access — for example, making them unable to delete files
- [a-03] JELAI is deployed using docker-compose, simplifying setup and ensuring user isolation for scalability and privacy.

**05 Privacy: The agent shall be private by design (e.g., local model, disabled telemetry, pseudonymized identifiers).**

- **[c-q2-13]** Ethical concerns—including data privacy, bias, and transparency—also influenced user trust and adoption levels
- **[c-q2-13]** we’re using our own instance of CoPilot. There’s nothing that’s leaving the organisation.
- [g-q2-p2-03] developers frequently ask whether a tool trains on their code, stores telemetry, or sends sensitive snippets to the cloud
- [s-q2-p3-01] Future systems should be aware of these needs and provide mechanisms to ensure that users have the ability to control any form of recording and sharing.
- [g-q1-p3-05] Allow users to control, erase, or refresh their records at all times.

**06 Domain-Specific Adaptivity: The agent shall align with domain-specific requirements for high-performance computing (code optimization and execution on HPC cluster).**

- **[s-q3-p1-08]** Verification mechanisms constitute the quality control layer of LLM-based scientific agents, implementing critical safeguards against hallucination, logical inconsistencies, factual inaccuracies, and procedural errors
- **[s-q3-p1-08]** until the Verifier confirms that the output meets standards of validity and reproducibility
- [c-q2-17] it is important for the AI to adjust its output (e.g., by providing explanations at the right level of detail)
- [a-07] This points to the need for tailoring responses according to user expertise
- [s-q2-p2-02] well-designed AI programming assistants may adapt to differences in expertise levels
- [g-q2-p2-08] I have a CLAUDE.md file that I update periodically, which contains process rules and preferences for Claude to follow. [...] Another powerful technique is providing in-line examples of the output format or approach you want.
- [c-q4-05] The extent to which the behavior of Copilot can adapt well to user coding habits is a vital factor in their decision to use Copilot. Therefore, providing flexible and user-friendly customization options is highly beneficial.

**07 User Communication: The agent shall explain steps, results, and recommendations with narrative summaries and supporting citations.**

- [s-q3-p1-02] Ongoing efforts also focus on improving the explainability and safety of AI agents, ensuring their actions and decisions can be understood and scrutinized by humans.
- [c-q3-01] Creating explainable AI models that offer clear reasoning for their hypotheses, experimental recommendations and conclusions is essential for preserving scientific integrity
- [c-q2-11] Users need to understand not only what the AI suggests but also why. This has led to increased focus on explainability, fairness, and auditability in AI system design
- **[s-q1-p2-02]** Explainability is essential for creating AI systems that are not perceived as "black boxes"; AI must articulate the reasoning behind its decisions in a way humans can understand, fostering trust and enabling informed decision-making
- [c-q6-18] Transparency and comprehensibility are crucial for AI systems to gain public trust.
- [c-q3-16] Progress is documented, providing transparent analytical decision paths.
- **[c-q5-17]** All hand -offs must maintain comprehensive audit trails documenting both AI recommendations and human decisions.
- [g-q1-p1-06] the user can further query the system about why a decision or prediction was made and whether it can be trusted.
- [c-q2-20] Narrative summaries: Using Natural Language Generation (NLG), Copilot produces Smart narrative text blocks that summarize the data in clear, everyday language.
- [c-q2-15] The platform systematically documents outputs, the underlying data sources, the assumptions made by the agents, and the rationale behind proposed model components or parameters.
- [s-q2-p3-06] Particularly the lack of sources or references was seen as a challenge
- [s-q3-p3-09] Proper and accurate source crediting
- [c-q2-15] QSP-Copilot maintains provenance metadata, linking extracted information directly to its references, thereby ensuring traceability.
- [g-q3-p3-04] Trust is impeded by black-box methods, especially with generative AI, prompting calls for explainable, provenance-traceable model outputs
- [c-q2-13] Several users highlighted that Copilot provides clear citations, helping them verify information

**08 Reporting: The agent shall report metrics for task performance and output confidence (to EuXFEL users and staff).**

- **[c-q1-18]** Transparent explanations, uncertainty indicators, and clearly communicated limitations
- **[c-q1-18]** Tools that integrate deep contextual awareness and provide transparency in the reasoning behind code suggestions are particularly valued for reducing uncertainty and fostering appropriate trust
- **[c-q3-08]** generating hypotheses and estimating their uncertainty to suggest relevant experiments
- [c-q2-01] performance of the recommendation, measured by the score assigned to the tasks. The score is determined using an answer key and a scoring mechanism that evaluates the correctness of the final solutions submitted for each task.
- [s-q3-p3-03] With Efficiency, we report on run time performance.
- [s-q2-p3-07] The efficiency of the generated code is evaluated based on performance metrics such as execution time, memory usage, and computational complexity
- [s-q3-p1-10] Wherever possible, reporting of system performance should be granular, with breakdowns across features of the problem space
- [s-q1-p2-03] Latency budgets: 200/500 ms; measure P50/P95 and deadline miss rate.
- [s-q2-p2-04] we felt it was important that the assistant convey a sense of uncertainty to encourage users to not accept its results uncritically
- [g-q3-p2-01] Uncertainty quantification techniques can help flag model predictions with low confidence, prompting further scrutiny.
- [a-04] Any result should also include its confidence or statistical relevancy.
- [c-q1-16] we recommend that systems like Copilot should help users see a little bit into the black box, such as what it is using as input, a confidence value (or visualization), and its own estimation of the skill level of the user.
- [g-q1-p2-07] Participants stressed the need for visible reasoning to sustain confidence in outputs and suggested adding intermediate calculations, manual adjustment options, and rationale logs to improve traceability and trust.
- [g-q3-p2-07] What is needed for taking safe decisions is epistemic humility: the AI must know the limits of its own knowledge, so that in case of doubt it avoids actions that could yield major harm according to some of the theories from the Bayesian posterior over theories.

**09 User-Specific Adaptivity: The agent shall adapt its code style and explanations to the user’s expectations.**

- **[c-q4-08]** and be capable of following user-speciﬁed coding style guidelines.
- **[c-q4-08]** AI-supported code completion tools should be able to identify the coding style followed and adapt its code suggestions.
- **[c-q4-11]** AI-based code assistants should ideally generate code that readily fits into the target project.
- [c-q1-03] The generated code's style doesn't match my project's.
- [g-q1-p2-04] Contextual design: When human-AI systems are intentionally structured to align with domain-specific requirements and goals.

**10 Scientific Writing Support: The agent shall assist in drafting scientific manuscripts.**

- [c-q3-16] drafting of a complete manuscript incorporating visualisations and validated citations
- **[s-q3-p1-03]** We demonstrated thatTh e A I Sc i e n t i s t - v 2 is capable of autonomously generating manuscripts that successfully pass peer review at a workshop of a major machine learning conference.
- **[c-q3-15]** assisting in the generation of text and the organization of manuscripts with speed and fluency.
- [c-q2-12] AI tools such as ChatGPT can also aid in drafting manuscripts, offering valuable suggestions for structuring and enhancing the content.

**11 Task Planning and Execution: The agent shall decompose tasks into verifiable steps within an executable plan, execute tasks iteratively using user-controlled feedback loops, provide alternative solutions where applicable, and recommend next steps based on intermediate results.**

- **[c-q5-12]** Planning assistance helps analysts reason about the analysis decisions. This can occur as analysts are explicitly planning their decisions (B) or even during execution when analysts are unaware of plausible alternatives (C).
- **[s-q2-p3-10]** Following the rules and actions configuration, the user specifies the software engineering task or process to be accomplished by AutoDev. [...] Planning and multi-step reasoning form the foundation of an LLM agent's ability to tackle complex tasks effectively which enables agents to decompose problems into smaller, more manageable subtasks and create strategic execution paths toward solutions
- **[c-q2-01]** an AI-based coding assistant that provides explicit alternatives as recommendations throughout the data science workflow.
- [s-q1-p1-10] Once clicked, users are given five sentence candidates, analogous to that of keyword-based recommendation.
- **[c-q2-10]** the Stepwise system decomposes the task into separate steps (visually similar to a computational notebook), displaying editable assumptions and their corresponding code one step at a time until the task is complete. [...] the Phasewise system decomposes the problem into three editable, logical phases: structured input/output assumptions, execution plan, and code.
- [s-q2-p2-01] These agents operate at the task level—reading codebases, planning changes, executing tools, refactoring code, running tests, and submitting pull requests.
- [c-q3-16] parameterisation of logical reasoning steps, conceptually aligned with 'least-to-most' prompting identifies constituent task components. This improves the tractability and transparency of multi-stage scientific workflows and enables verification and refinement of each component to maintain step-level precision
- [g-q3-p1-09] To improve the overall quality of the generated paper, we incorporated multiple reflection processes into our workflow. We repeat these reflections three times.
- [g-q3-p3-04] Code is generated, executed, and reviewed using program-and-review cycles overseen by code reviewer subagents
- [c-q1-08] The development model in SE 3.0 is inherently iterative and cyclic, where humans react to the prototyped software in every code cycle.
- [c-q2-06] Users often accept these imperfect solutions and then engage in an accept-validate-repair sequence [4] as a way to read, internalize, and adapt the generated code to the local interface.
- [c-q5-09] Participants emphasized on the importance of thoroughly validating every operation performed using LLM-generated code.
- [c-q1-11] These agents accept high-level tasks from developers and follow plan–execute–validate–revise loops until a stopping condition is met.
- [s-q1-p1-09] AI agents can be taught or give feedback by the human participants through direct, iterative interactions.
- [c-q1-13] These AI partners engage in iterative, conversation-driven development processes
- [g-q2-p2-08] For a new project, I’ll describe the idea and ask the LLM to iteratively ask me questions until we’ve fleshed out requirements and edge cases.
- [c-q2-14] the task of developing a model usually consists of a dialogue with ChatGPT, rather than a single request–response interaction.
- [s-q1-p1-05] effective and iterative communication with ChatGPT is essential for ensuring accurate and relevant responses, as it operates on the principle of "garbage in, garbage out".
- [g-q1-p2-07] Participants noted that iterative feedback improved completeness and feasibility, often within two feedback rounds.
- [s-q1-p3-08] The iterative exchange continues until the AI's instruction requirements are satisfied, and is followed by the presentation of the AI's predicted outcome for the decision-making task.
- [g-q1-p3-02] The humans were giving instructions, evaluating ideas, and debating choices. Meanwhile AI was offering ideas, illustrating concepts, responding to our feedback.
- [c-q2-10] Any variables and dataframes created during execution are displayed as intermediary variables that the user may inspect.
- [s-q3-p1-06] We hope Agent Laboratory enables researchers to allocate more effort toward creative ideation rather than low-level coding and writing, ultimately accelerating scientific discovery.
- [g-q3-p3-02] the emphasis should shift from output safety to behavioral safety, which signifies a comprehensive approach that evaluates not only the accuracy of the agent’s output but also the actions and decisions it takes.
- [g-q3-p1-07] Hence, it is necessary to verify the agent action plan before execution.

**12 Context Awareness: The agent shall maintain relevant context across conversation turns, and files and sessions within a project.**

- [c-q1-10] The system incorporates a specialized language processing pipeline optimized for code comprehension that maintains contextual understanding across multiple files within the same solution.
- [s-q2-p2-03] The model can handle multiple interactions and maintain contextual understanding
- **[g-q3-p1-07]** Long-term memory stores essential and factual knowledge that underpins agent behavior and understanding of the world, ensuring this information persists beyond task completion. [...] Short-term memory allows agents to temporarily acquire skills, such as tool usage, store information about recent states of a biological system, and keep track of outcomes from earlier reasoning efforts.
- [s-q3-p1-04] In order to enable iterative computation and scientific reasoning over long time horizons, the co-scientist uses a persistent context memory to store and retrieve states of the agents and the system during the course of the computation.
- [c-q2-06] They generally preferred not to manually specify context, trusting the system to consider all available information.
- **[c-q4-14]** integrates retrieved content, user interaction history, and contextual information to generate effective prompts
- [g-q2-p2-03] The underlying requirement is straightforward: tools must reliably maintain, retrieve, and update relevant project context as work progresses
- [c-q1-18] Tools should reduce cognitive load through seamless integration into existing workflows and by providing context-aware suggestions
- [s-q2-p3-06] we observed that the presence or absence of project-specific information, referred to as contextual information or simply context, had a more significant influence on participants’ overall experiences.

**13 Documentation: The agent shall generate comprehensive documentation, including project-level (e.g., README files) and code-level documentation (e.g., inline comments).**

- [s-q2-p1-10] It can also fluently generate comments, messages, and documentation.
- [a-05] The predefined prompt tool consistently provided concise Docstrings that participants perceived as more readable and contained less non-informative content compared to the output of the ad-hoc prompt tool.
- [s-q3-p3-03] With Comprehension, we give a measure on how hard or easy the code is to comprehend. Here, we focus on the quality of comments and documentation the tool generated.
- [c-q4-06] The tool not only produces code but is also capable of generating comprehensive comments that elucidate the purpose and functionality of the code, given the current context within the development environment.

**14 Version Control: The agent shall enforce the use of version control systems to ensure code availability and reproducibility of results.**

- **[c-q2-10]** once an edit is submitted, our system introduces a new branch to preserve the original, unedited version, while incorporating the edited version in the “main” branch.
- [g-q3-p3-01] Versioning is critical; when comparing different experiments, you must ensure they are benchmarked against the same data.

**15 Performance: The agent shall optimize latency using, e.g., parallel execution of sub-agents, adjusting reasoning depth to task complexity, and caching.**

- [g-q3-p3-08] Downstream developers don’t care about the number of active parameters when they’re using an API. They simply care about the dollar cost relative to accuracy.
- [s-q3-p3-10] Future evaluation frameworks should integrate cost efficiency as a core metric, tracking factors such as token usage, API expenses, inference time, and overall resource consumption.
- **[s-q3-p1-03]** An LLM is used to generate the plan and experiment code for each new child node, after which all new nodes are executed concurrently in parallel, significantly accelerating the exploration process.
- **[s-q3-p1-03]** For each selected idea, the system autonomously executed the full experimental pipeline using the parallelized agentic tree search (§3.2.2) multiple times, each initiated with a different random seed.
- **[s-q3-p2-07]** Although the parallelized mode accelerates improvements in wall-clock time, it introduces trade-offs between speed and computational efficiency.
- **[s-q3-p2-07]** We introduce a parallelized mode for AgentRxiv, allowing multiple agentic systems to run simultaneously and share findings.
- [c-q2-02] Data-Copilot plans workflows—multiple interfaces in specific order forming chain, parallel, or loop structures.
- [c-q3-16] delegating implementation to two further orchestrators in parallel – a figures agent and a tables agent – each responsible for their respective visual elements.
- [g-q3-p2-09] This design enables the system to flexibly scale compute and to iteratively improve its scientific reasoning towards the specified research goal.
- [g-q1-p2-10] The modularity and distributed nature of multiagent systems enable agents to scale effectively, accommodating growth and evolving challenges without compromising performance or efficiency.
- [s-q1-p1-09] The internal reasoning produced by the ChatCollab AI agents when making decisions is made public to a human admin in the system’s user interface.
- [c-q1-15] Communicating genAI’s reasoning process and derivation of its outputs in the context of the current task.
- **[s-q1-p2-03]** Orchestrator (policy engine): A stateless, horizontally scalable service that evaluates routing decisions on every dialog turn.
- **[s-q1-p2-03]** The orchestrator must route between autonomous LLM responses, tool augmented generation (RAG, KB search, workflow APIs), and human collaboration (agent assist, supervised approval, or escalation) using signals such as intent class, risk score, user tier, coverage of cited evidence, live latency, token/$ budgets, and agent availability.
- [s-q1-p1-01] Workflow Automation Effectiveness (WAE) has produced M = 3.84, SD = 0.69, reflecting perceived reductions in manual steps, improved routing smoothness, and faster completion of routi ne requests.
- [c-q1-08] To ensure AI teammates are effective for daily use, they must offer low-latency responses and be cost-effective.  
- [g-q2-p1-07] To make sure the user experience is smooth, we define a latency SLA for context fetching

**- 16 Scalability: The agent shall support multiple concurrent users efficiently.**

- **[a-03]** Support multiple concurrent users efficiently while ensuring data isolation and privacy, particularly when using local LLMs.
- **[c-q3-16]** Additional safeguards include API rate limiting to prevent service overload, logging of all system activities for auditability
