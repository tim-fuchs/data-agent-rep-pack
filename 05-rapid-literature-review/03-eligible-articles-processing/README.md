# Process Eligible Articles

## Purpose

This folder contains:

- The Python script to convert HTML and PDF to Markdown.
- The Python script to count the number of characters in the Markdown files.

## Install

1. Open the command-line interface from this directory.
2. Create a virtual environment, activate it, upgrade pip, and install the required packages: `python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt`.

## Usage

- Run `scripts/convert_to_markdown.py` to convert the HTML and PDF files in the `/data/html_pdf` directory to Markdown format and save them in the `/data/markdown` directory.
- Run `scripts/count_characters.py` to count the number of characters in each Markdown file and save the results in the `/data/character_count.csv` directory.

The Markdown files will be used for the next step of the literature review, which is to extract the key information from them.

## Notes on Additional Markdown Cleaning

- The HTML and PDF files include extraneous content before and after the main article text.
  - Prefix content may consist of webpage headers (e.g., recommended papers) or overview pages commonly found in PDFs (e.g., ACM).
  - Suffix content typically includes acknowledgments, references, and appendices.
- This non-essential material is also carried over into the Markdown files and can negatively affect LLM performance during data analysis.
- To address this, we manually removed irrelevant sections from each Markdown file to ensure high-quality input data. We stored the cleaned Markdown files in the `/data/markdown_cleaned` directory, which is also considered by the `count_characters.py` script for character counting.
- Across the 224 Markdown files used for data analysis, this process reduced the average file size **from 93,029 to 57,433 characters**.
- _Note:_ While automated approaches may be possible, we chose manual cleaning to ensure that only truly irrelevant content was removed.
