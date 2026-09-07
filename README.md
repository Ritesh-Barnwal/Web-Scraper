# Web Scraper

## Project Goal

Build a Python-based web scraper that can automatically collect
useful information from webpages and organize the extracted data.

## Requirements

- Python
- Requests
- BeautifulSoup
- HTML parsing
- Data extraction
- Data storage

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Ritesh-Barnwal/Web-Scraper.git

2. Navigate to the project directory:
  cd Web-Scrapper

3. Create and activate a virtual environment:
  python3 -m venv .venv
  source .venv/bin/activate

4. Install the required dependencies:
  pip install -r requirements.txt

5. Run the Scraper:
  python -m src.scraper

# Data Source

This project uses Books to Scrape as
the data source for practicing web scraping.

# \Scraping Targets

The scraper collects the following information from each book:

Book title
Price
Rating
Book link

## Data Source

This project uses [Books to Scrape](https://books.toscrape.com/) as
the data source for practicing web scraping.

## Scraping Targets

The scraper collects the following information from each book:

- Book title
- Price
- Rating

# Week 1 Progress

## Progress

During Week 1, I built the basic structure of a Python web scraper using
Requests and BeautifulSoup.

Completed work:
- Set up the Python development environment.
- Learned the basics of BeautifulSoup and HTML parsing.
- Created a scraper to extract book information.
- Extracted book title, price, rating, and link.
- Added error handling for failed requests.
- Added handling for missing data.
- Added pagination to scrape multiple webpages.
- Tested the scraper with valid and invalid URLs.
- Added basic automated tests using pytest.
- Improved repeated requests using requests.Session().
- Updated the README with project setup and usage instructions.

## Challenges

# 1. Import Error

Initially, the project had an import error because the project structure
was not being recognized correctly.

**Solution:** Used `src` as a Python package and ran the scraper with:

<!-- ```bash
python -m src.scraper -->

# 2. Pagination URL Error

The scraper initially created an incorrect URL containing catalogue
twice when moving to the next page.

Solution: Used urljoin() to correctly construct the next-page URL.

# 3. Missing Data

Some webpage elements could potentially be missing.

Solution: Added checks before extracting the required information and
skip the book if required data is missing.

# 4. Request Errors

Web requests can fail because of invalid URLs or network problems.

Solution: Added exception handling using requests.RequestException.

### Week 1 Outcome

By the end of Week 1, the scraper can automatically navigate through
multiple pages of Books to Scrape and collect structured book information.

