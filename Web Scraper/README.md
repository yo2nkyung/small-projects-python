# Simple Web Scraper

A simple Python web scraper that fetches HTML content from a specified URL, extracts titles and links from anchor tags (`<a>`), and saves the extracted data to a CSV file.

## Project Overview

This project demonstrates a basic web scraping tool using Python. The scraper fetches HTML content from a given URL, parses the content to extract specific information (titles and links), and stores the extracted data in a CSV file for further use or analysis.

### Key Features

- Fetch HTML content from a specified URL
- Parse HTML content to extract titles and links from anchor tags
- Save extracted data to a CSV file

## Installation

### Prerequisites

- Python 3.x

### Installation Steps

1. Required packages:
   - beautifulsoup4
   - requests

## Usage

1. Update the URL in the script to the website you want to scrape:

   ```python
   url = 'https://example.com'  # Replace with the actual URL
   ```

2. Run the script:

   ```python
   python web_scraper.py
   ```

3. The extracted data will be saved to extracted_data.csv.