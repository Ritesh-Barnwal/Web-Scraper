import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse # For CLI (W2 D3)

from src.config import (
    URL,
    BOOK_SELECTOR,
    TITLE_SELECTOR,
    PRICE_SELECTOR,
    RATING_SELECTOR,
    LINK_SELECTOR
)

import csv

def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["title", "price", "rating", "link"]
        )

        writer.writeheader()
        writer.writerows(data)

def scrape_books(url, pages):
    scraped_data = []
    page_number = 1

    while url and page_number <= pages:
        print(f"Scraping page {page_number}...")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as error:
            print(f"Error fetching webpage: {error}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        
        if "captcha" in response.text.lower():
            print("CAPTCHA detected. Scraping stopped.")
            break

        books = soup.select(BOOK_SELECTOR)

        for book in books:
            title_element = book.select_one(TITLE_SELECTOR)
            price_element = book.select_one(PRICE_SELECTOR)
            rating_element = book.select_one(RATING_SELECTOR)
            link_element = book.select_one(LINK_SELECTOR)

            if not title_element or not price_element or not rating_element or not link_element:
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
    parser = argparse.ArgumentParser(description="Web Scraper CLI")
    parser.add_argument("--url", required=True, help="URL to scrape")
    parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape")

    args = parser.parse_args()
    url = args.url
    pages = args.pages
    
    # url = input("Enter webpage URL: ")
    # pages = int(input("Enter number of pages: "))

    books = scrape_books(url, pages)

    save_to_csv(books, "books.csv")

    for book in books:
        print(book)
