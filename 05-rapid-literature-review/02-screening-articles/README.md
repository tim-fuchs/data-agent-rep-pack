# Scrape Articles (Scientific Publications, Blog Posts, etc.)

## Purpose

This folder contains:

- The CSV file with the scraped titles and URLs from Google, Google Scholar, and Consensus
- The Python script to export the HTML websites from the URLs

## Install

1. Open the command-line interface from this directory.
2. Create a virtual environment, activate it, upgrade pip, and install the required packages: `python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt`.

## Usage

- Make sure to have access to the full text of the articles you want to scrape. For scientific publications, you may need to have access through a university VPN.
- Run `python scripts/export_html.py` to export the HTML content of the articles listed in `data/sources.csv` and save them in the `data/html_pdf` directory. The process is documented in `data/log.csv`.

## Notes on Automatically Downloaded Articles

- Out of 250 unique articles, the full-text HTML could be automatically exported only for 102 articles.
- For the remaining articles, the full text (HTML or PDF) had to be downloaded manually due to the following reasons:

  - Bot detection mechanisms (e.g., ACM Digital Library, Taylor and Francis Online)
  - Dynamically rendered content that is visible in the browser but not captured during export (e.g., IEEE Xplore, ScienceDirect)
  - Full text not directly available on the website (e.g., arXiv preprints without HTML version)

- See `../literature_review_overview.xlsx` for the list of manually and automatically downloaded articles.
