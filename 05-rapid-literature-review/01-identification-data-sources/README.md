# Scrape Content from Google, Google Scholar, and Consensus

## Purpose

This folder contains the raw HTML and CSV files exported from Google, Google Scholar, and Consensus, the Python scripts to scrape the entries from these files, as well as the CSV file containing the scraped data.

## Install

1. Open the command-line interface from this directory.
2. Create a virtual environment, activate it, upgrade pip, and install the required packages: `python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt`.

## Usage

- Run `python scripts/scrape.py` to process the raw files from Google, Google Scholar, and Consensus, and export the processed entries with ID, title, and URL to `data/sources.csv`.
- The `sources.csv` file will be used for the next step of the literature review, which is to scrape the content of the articles.
