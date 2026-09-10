# Web Scraper

A Python-based web scraper that extracts structured book information
from webpages and stores the collected data in CSV format.

## Project Goal

The goal of this project is to build a practical web scraper that can
automatically collect useful information from webpages, handle common
errors, support multiple pages, and organize the extracted data.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Selenium
- CSV
- Pytest
- ThreadPoolExecutor

## Features

- Scrapes book information from Books to Scrape.
- Extracts book title, price, rating, and link.
- Supports scraping multiple pages.
- Handles request and network errors.
- Handles missing webpage data.
- Detects CAPTCHA pages and stops scraping.
- Saves scraped data into a CSV file.
- Provides a command-line interface using argparse.
- Supports JavaScript-rendered webpages using Selenium.
- Uses logging to record scraping activity and errors.
- Uses multi-threading support for concurrent webpage requests.
- Includes basic automated testing using pytest.
- Measures total execution time.

## Data Source

This project uses
[Books to Scrape](https://books.toscrape.com/)
as the data source for practicing web scraping.

## Scraping Targets

The scraper collects the following information from each book:

- Book title
- Price
- Rating
- Book link

## Project Structure

```text
Web-Scrapper/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── scraper.py
│   └── javascript_scraper.py
├── tests/
│   └── test_scrapper.py
├── Notes/
│   └── web_scraping_notes.md
├── README.md
├── requirements.txt
├── books.csv
└── .gitignore 
```

## Installation


1. Clone the repository
```bash
git clone https://github.com/Ritesh-Barnwal/Web-Scraper.git 
```
2. Navigate to the project directory
cd Web-Scrapper
3. Create a virtual environment
python3 -m venv .venv
4. Activate the virtual environment
source .venv/bin/activate
5. Install dependencies
pip install -r requirements.txt


## Run the scraper using:

```bash
python -m src.scraper --url https://books.toscrape.com/ --pages 5
```

### Command-line arguments

### `--url`

The URL of the website to scrape.

Example:

```bash
--url https://books.toscrape.com/
```

### `--pages`

The number of pages to scrape.

Example:

```bash
--pages 5
```

The number of pages must be at least 1.

Output

The scraped data is stored in:

`books.csv`

### The CSV file contains:

- title
- rating
- price
- link
- Logging

The scraper records important activities and errors in:

`scraper.log`

### The log contains information such as:

- Request errors
- Pages being scraped
- CAPTCHA detection
- Missing book data
- Timestamps
- Logging levels
- JavaScript Pages

Some webpages load their content using JavaScript, which may not be available in the initial HTML response.

For such pages, Selenium is used to load the webpage in a browser and retrieve the rendered HTML.

The JavaScript scraper is located at:

`src/javascript_scraper.py`

## Testing

The project includes automated tests using pytest.

Run the tests with:

```bash
python -m pytest
```

## Performance

The project includes support for concurrent webpage requests using `Python's ThreadPoolExecutor.`

This allows multiple webpage requests to be handled concurrently when
using the multi-threaded fetching functionality.

## Deployment

The Web Scraper is deployed using GitHub Actions.

The workflow runs the scraper in a GitHub-hosted Ubuntu environment and
automatically:

- Checks out the project repository.
- Sets up Python 3.13.
- Installs project dependencies.
- Runs the scraper.
- Uploads the generated `books.csv` and `scraper.log` files as workflow artifacts.

The GitHub Actions workflow is located at:

`.github/workflows/scraper.yml`

The workflow can be manually triggered from the GitHub Actions tab.

## Error Handling

The scraper handles several common problems:

- Invalid URLs
- Network/request failures
- Missing webpage elements
- Invalid page numbers
- Empty scraping results
- CAPTCHA detection



## Project Progress

# Week 1
Set up the Python development environment.
Created the basic scraper.
Learned Requests and BeautifulSoup.
Extracted book title, price, rating, and link.
Added error handling.
Added missing-data handling.
Added pagination.
Added automated testing.
Added requests.Session() for repeated requests.

# Week 2
Added CSV data storage.
Added command-line arguments using argparse.
Added CAPTCHA detection.
Added automated testing.
Improved request performance.
Refactored the scraper for better readability.

# Week 3
Added Selenium support for JavaScript-rendered webpages.
Added multi-threaded webpage fetching support.
Conducted user testing and gathered feedback.
Improved error handling.
Improved command-line output.
Added logging for scraper activity and errors.
Updated project documentation and README.

# Week 4
Deployed the Web Scraper using GitHub Actions.
Configured scraper execution in a GitHub-hosted environment.
Verified successful scraper execution and artifact generation.

### Author

`Ritesh Kumar Barnwal`