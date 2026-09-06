import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from src.config import (
    URL,
    BOOK_SELECTOR,
    TITLE_SELECTOR,
    PRICE_SELECTOR,
    RATING_SELECTOR,
    LINK_SELECTOR
)

def scrape_books(url):
    scraped_data = []
    page_number = 1

    while url:
        print(f"Scraping page {page_number}...")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as error:
            print(f"Error fetching webpage: {error}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

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

        next_button = soup.select_one("li.next a")

        if next_button:
            next_page = next_button["href"]
            url = urljoin(url, next_page)
        else:
            url = None    

        page_number += 1
        
    return scraped_data

if __name__ == "__main__":
    books = scrape_books(URL)

    for book in books:
        print(book)
