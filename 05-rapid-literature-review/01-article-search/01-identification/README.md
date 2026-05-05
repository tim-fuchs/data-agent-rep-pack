# Identify Articles

## Purpose

This folder contains:

- Summary of the identification process (see below)
- HTML and CSV files containing the search results from the data sources (Google, Google Scholar, Consensus, additional papers)
- Python script to scrape the title and URL of the file entries
- CSV file containing the scraped information

## Usage

1. Read the summary of the article identification process below.
2. Optionally, repeat the identification process:
   - Follow the installation process below.
   - Run `python scripts/scrape.py` to export the ID, title, and URL of the articles to `data/sources.csv`.

## Install

1. Open the command-line interface from this directory.
2. Create a virtual environment, activate it, upgrade pip, and install the required packages: `python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt`.

## Summary of Identification Process

### Information Sources

- Sources:
  - Google Scholar
  - Google
  - Consensus AI
  - Additionally: publications we were already aware of
- Filter:
  - Publication date between 2023-01-01 and 2026-03-13 (to focus on requirements for LLM-based AI agents)
  - Result types:
    - Scientific publications
    - Grey literature (preprints, blog posts, technical reports, etc.)

### Search Queries

- Note: List of search queries is based on the following ChatGPT search query and multiple interactions afterward (2026-03-13):
  `"I want to conduct a rapid multi-vocal literature review via Google, Google Scholar, and Consensus AI to review lessons learned from studies about human-ai interaction in the fields of software engineering and science. List good search terms."`

- Search queries for Google and Google Scholar:
  - Human-AI collaboration:
    `("human AI" OR "human LLM" OR "human copilot" OR "human AI agent") (collaboration OR team OR "assisted work" OR "augmented work") ("lessons learned" OR recommendation OR experience OR evaluation)`
  - Developer experience:
    `("AI" OR "LLM" OR "copilot" OR "AI agent") ("developer" OR "coding assistant" OR "pair programming" OR "code generation" OR "software engineering") ("lessons learned" OR recommendation OR experience OR evaluation)`
  - AI for science:
   `("AI" OR "LLM" OR "copilot" OR "AI agent") (scientists OR researchers OR "scientific research" OR "scientific workflow") ("lessons learned" OR recommendation OR experience OR evaluation)`

- Search queries for Consensus AI:
  - `how do AI copilots affect developers?`
  - `how do AI copilots affect data scientists?`
  - `how do AI copilots affect science?`
  - `lessons learned copilots for developers`
  - `lessons learned copilots for data scientists`
  - `lessons learned copilots for science`

### Data Collection Process

- Date of data collection: 2026-03-13
- Browser settings:
  - General:
    - Safari on macOS
    - English language
  - For Google and Google Scholar:
    - New private browser per query
    - Cookies rejected
  - Consensus:
    - Login with user account required
- Data export:
  - Google and Google Scholar:
    - Per query, first three pages downloaded as HTML files.
    - Data extracted via Python script
  - Consensus:
    - Per query, used the built-in feature to export the list of references as CSV file
- Data processing:
  - Create and run a Python script to scrape title and link of each entry from the exported files and store the entries together with generated IDs in one CSV file.

### Identified Articles

**Overview:**

| Source        | 1. Search results | 2. Unique | 3. Full text available |
| ------------- | ----------------- | --------- | ---------------------- |
| Google        | 88                | 71        | 70                     |
| Scholar       | 90                | 85        | 85                     |
| Consensus     | 119               | 87        | 86                     |
| Additional    | 7                 | 7         | 7                      |
|               |                   |           |                        |
| Sum           | 304               | 250       | 248                    |
|               |                   |           |                        |
| Peer Reviewed |                   | 148       | 148                    |
| Preprint      |                   | 48        | 48                     |
| Blog          |                   | 48        | 46                     |
| Forum         |                   | 3         | 3                      |
| Report        |                   | 1         | 1                      |
| Video         |                   | 1         | 1                      |
| Code          |                   | 1         | 1                      |

**Process:**

1. Only keep unique articles by comparing article titles with each other.
2. Open the article to check:
   - If full text is available
     - Full text was unavailable for two articles.
     - Webpage of one article was unavailable. Other article was behind a paywall.
   - Type of article
3. For all non-peer-reviewed articles, check if a peer-reviewed version exists
   - Example: arXiv preprint vs. ACM version of an article
   - Among the non-peer-reviewed articles, we could find 14 peer-reviewed versions.
