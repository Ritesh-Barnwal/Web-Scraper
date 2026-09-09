from concurrent.futures import ThreadPoolExecutor
import argparse
import csv
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from src.config import (
    BOOK_SELECTOR,
    TITLE_SELECTOR,
    PRICE_SELECTOR,
    RATING_SELECTOR,
    LINK_SELECTOR
)


def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["title", "price", "rating", "link"]
        )

        writer.writeheader()
        writer.writerows(data)

def fetch_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def fetch_pages(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        pages = list(executor.map(fetch_page, urls))
    return pages

def scrape_books(url, pages):
    scraped_data = []
    page_number = 1
    session = requests.Session()

    while url and page_number <= pages:
        print(f"Scraping page {page_number}...")

        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()

        except requests.RequestException as error:
            print(f"Error fetching webpage: {error}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        if "captcha" in response.text.lower():
            print("CAPTCHA detected. Scraping stopped.")
            break

        books = soup.select(BOOK_SELECTOR)

        if not books:
                print("No books found on the webpage.")
                break

        for book in books:
            title_element = book.select_one(TITLE_SELECTOR)
            price_element = book.select_one(PRICE_SELECTOR)
            rating_element = book.select_one(RATING_SELECTOR)
            link_element = book.select_one(LINK_SELECTOR)

            if (
                not title_element
                or not price_element
                or not rating_element
                or not link_element
            ):
                print("Skipping book because some data is missing.")
                continue

            title = title_element.get_text(strip=True)
            price = price_element.get_text(strip=True)
            rating = rating_element["class"][-1]
            link = link_element["href"]

            scraped_data.append({
                "title": title,
                "price": price,
                "rating": rating,
                "link": link
            })

        next_button = soup.select_one("li.next a")

        if next_button:
            next_page = next_button["href"]
            url = urljoin(url, next_page)
        else:
            url = None

        page_number += 1

    return scraped_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Web Scraper CLI"
    )

    parser.add_argument(
        "--url",
        required=True,
        help="URL to scrape"
    )

    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of pages to scrape"
    )

    args = parser.parse_args()

    url = args.url
    pages = args.pages

    if pages < 1:
        print("Error: pages must be at least 1.")
        exit()

    start_time = time.time()

    books = scrape_books(url, pages)

    print("Scraping completed successfully!")
    print(f"Books scraped: {len(books)}")
    print("Data saved to: books.csv")

    save_to_csv(books, "books.csv")

    end_time = time.time()

    print(
        f"Total execution time: "
        f"{end_time - start_time:.2f} seconds"
    )