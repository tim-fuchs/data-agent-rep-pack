# Analysis Article Data

## Purpose

This folder contains all scripts to analyze the relevance of and extract requirements from the articles in `data/articles`.
The analysis is performed with one or more LLMs as analyzers, which can be configured in the `.env` file.
Initial experiments with LLM user prompts are documented in the `prompt_versions` folder.

## Install

1. Copy `.env.example` to `.env`.
2. Configure `ANALYZERS` in `.env`:
   - `openai,nebius` runs the analysis of article relevance and requirementswith two LLMs in parallel, one from OpenAI and one from Nebius
   - `openai` runs only OpenAI
   - `nebius` runs only a model hosted by Nebius, e.g., MiniMax-M2.5
3. Add provider credentials and model settings in `.env`: use `OPENAI_*` and/or `NEBIUS_*` for the relevance and requirement analyses, and `SYNTHESIS_*` for the subsequent synthesis.
4. Create a virtual environment, activate it, upgrade pip, and install the required packages: `python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt`.

## Usage

- Run `python scripts/analyze_relevance.py` to analyze the relevance of the articles in `data/articles`.
  - Outputs one CSV per enabled analyzer: `data/relevance_openai.csv` and/or `data/relevance_nebius.csv`.
  - For each article, enabled analyzers run in parallel.
- Run `python scripts/analyze_requirements.py` to extract requirements from the same articles.
  - Outputs one CSV per enabled analyzer: `data/requirements_openai.csv` and/or `data/requirements_nebius.csv`.
  - For each article, enabled analyzers run in parallel.
- Run `python scripts/combine_relevance.py` to combine the relevance scores of multiple analyzers.
  - Discovers `data/results/relevance_*.csv` files dynamically and builds provider columns such as `relevance_score_openai`.
  - Writes `data/results/relevance_combined.csv` with columns `article_ID`, dynamic provider score columns, `mean`, and `std`.
- Run `python scripts/combine_requirements.py` to merge requirement rows from multiple analyzers.
  - Discovers `data/results/requirements_*.csv` files dynamically.
  - Writes `data/results/requirements_combined.csv`.
- Run `python scripts/synthesize_thematically.py` to perform two-pass thematic synthesis.
  - Reads `data/results/requirements_combined.csv`.
  - Assigns an `initial_theme` per requirement, then consolidates themes to low-overlap reusable `final_theme` labels.
  - Detects (near-)duplicates per article and assigns same thematic labels to them.
  - Writes `data/results/synthesis_thematically_initial.csv` and `data/results/synthesis_thematically_final.csv`.
  - To skip initial theme assignment and only perform final theme consolidation (using previously saved initial themes), add the `--skip-initial-themes` option: `python scripts/synthesize_thematically.py --skip-initial-themes`
  - When skipping, the script reads from `data/results/synthesis_thematically_initial.csv` and only performs the final theme consolidation step.
- Run `python scripts/synthesize_summary.py` to create a summary of the literature review.
  - Reads `data/results/synthesis_thematically.csv` and `data/results/relevance_combined.csv`.
  - Writes `data/results/synthesis_summary.md` by listing all themes, each with a prose summary of the theme, and a table of the corresponding requirements and the IDs and relevance scores of the articles they appear in.
