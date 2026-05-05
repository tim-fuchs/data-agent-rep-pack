# Preprocess Articles Included in the Thematic Analysis

## Purpose

This folder contains:

- Summary of the article preprocessing during the screening process (see below)
- Python script to convert HTML and PDF files to Markdown files.
- Python script to count the number of characters in the Markdown files.
- Folder with the articles in Markdown format
  - Only available after conducting the conversion process
  - We excluded the folder in the replication package to avoid license violations.

## Usage

1. Read the summary of the article preprocessing below.
2. Optionally, repeat the preprocessing process:
   - Follow the installation process below.
   - Create the new folder `data` within this folder.
   - Copy the `html_pdf` folder from the previous screening process into `data`.
   - Run `scripts/convert_to_markdown.py` to convert the HTML and PDF files in `data/html_pdf` to Markdown format and save the Markdown files in the `/data/markdown` directory.
   - Run `scripts/count_characters.py` to count the number of characters in each Markdown file and save the results in the `/data/character_count.csv` file.

## Install

1. Open the command-line interface from this directory.
2. Create a virtual environment, activate it, upgrade pip, and install the required packages: `python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt`.

## Summary of Article Preprocessing

**Process:**

1. Use script to convert the HTML/PDF files of the 224 articles to Markdown.
2. Manually clean irrelevant content from Markdown files:
   - The HTML and PDF files include extraneous content as prefixes or suffixes of the main article text.
     - Prefix content may consist of webpage headers (e.g., recommended papers) or overview pages commonly found in PDFs (e.g., ACM).
     - Suffix content typically includes acknowledgments, references, and appendices.
   - This irrelevant content is also carried over into the Markdown files and could negatively affect LLM performance during data analysis.
   - Therefore, we manually removed irrelevant sections from each Markdown file to ensure high-quality input data.
   - We stored the cleaned Markdown files in the `/data/markdown_cleaned` directory, which is also considered by the `count_characters.py` script for character counting.
   - _Note:_ While automated approaches may be possible, we chose manual cleaning to ensure that only truly irrelevant content was removed.
3. Use script to count number of characters per article.

**Average number of characters per article:**

- Before cleaning: 93,029
- After cleaning: 57,433
