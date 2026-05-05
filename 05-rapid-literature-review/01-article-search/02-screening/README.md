# Screen Articles

## Purpose

This folder contains:

- Summary of the screening process (see below)
- CSV file from the previous identification process
- Python script that downloads the HTML websites of the identified articles
- CSV file logging the download process (timestamp and success status per article)
- Folder with the the articles in HTML format
  - Only available after conducting the download process
  - We excluded the folder in the replication package to avoid license violations.

## Usage

1. Read the summary of the article screening process below.
2. Optionally, repeat the screening process:
   - Follow the installation process below.
   - Copy the `sources.csv` file from the previous identification process. Paste it to the `02-screening/data` folder.
   - Make sure to have access to the full text of the articles you want to download. For scientific publications behind a paywall, you need to connect to a university VPN.
   - Run `python scripts/export_html.py` to download the HTML versions of the articles listed in `data/sources.csv` to the `data/html_pdf` directory.
   - Read the `data/log.csv` file to check which files could be downloaded and which not.
   - Manually check the downloaded files to identify files that do not contain the full text of an article (might just contain the title and abstract).
   - Manually download the full text of the articles that could not be downloaded automatically (ideally as HTML file, not PDF).
   - Skim the articles to check their relevance.

## Install

1. Open the command-line interface from this directory.
2. Create a virtual environment, activate it, upgrade pip, and install the required packages: `python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt`.

## Summary of Screening Process

**Overview:**

| Source        | 1. Full text available | 2. Relevant |
| ------------- | ---------------------- | ----------- |
| Google        | 70                     | 55          |
| Scholar       | 85                     | 81          |
| Consensus     | 86                     | 81          |
| Additional    | 7                      | 7           |
|               |                        |             |
| Sum           | 248                    | 224         |
|               |                        |             |
| Peer Reviewed | 148                    | 141         |
| Preprint      | 48                     | 46          |
| Blog          | 46                     | 36          |
| Forum         | 3                      | 0           |
| Report        | 1                      | 1           |
| Video         | 1                      | 0           |
| Code          | 1                      | 0           |

**Process:**

1. Download the articles:
   - Out of the 248 unique articles with available full text, the full-text HTML could be automatically exported for 100 articles only.
   - For the remaining articles, we had to download the full text (HTML or PDF) manually due to the following reasons:
     - Bot detection mechanisms (e.g., ACM Digital Library, Taylor and Francis Online)
     - Dynamically rendered content that is visible in the browser but not captured during export (e.g., IEEE Xplore, ScienceDirect)
     - Full text not directly available on the website (e.g., arXiv preprints without HTML version)
2. Skim articles to check their relevance regarding the research question of the literature review.

**Reasons for excluding articles:**

- It is about enabling better AI benchmarks.
- It is about how to report AI usage in publications.
- It is about how to use AI for literature reviews.
- It is about performance of LLMs for literature reviews.
- It is about the AI job market.
- It is an advertisement for a tool. (2x)
- It is a forum thread with general RAG instructions.
- It is a landing page for a tool.
- It is a short report without any empirical insights.
- It is a superficial social media discussion. (2x)
- It is a short replication study.
- It describes a dataset.
- It introduces a new benchmark. (3x)
- It is an introduction of a new tool feature.
- It is an overview of AI tools.
- It is an overview of a training course. (2x)
- It is not in English.
- It compares performance of LLMs on exam questions.
- It lists articles about using AI for science. Would just be relevant if we would conduct snowballing additionally.
