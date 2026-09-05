import requests
from bs4 import BeautifulSoup

from config import (
    URL,
    BOOK_SELECTOR,
    TITLE_SELECTOR,
    PRICE_SELECTOR,
    RATING_SELECTOR
)

def scrape_books(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Error fetching webpage: {error}")
        return []

# or just use this below one line
    # response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select(BOOK_SELECTOR)

    scraped_data = []

    for book in books:
        title = book.select_one(TITLE_SELECTOR).get_text(strip=True)
        price = book.select_one(PRICE_SELECTOR).get_text(strip=True)
        rating = book.select_one(RATING_SELECTOR)["class"][-1]

        scraped_data.append({
            "title": title,
            "price": price,
            "rating": rating
        })

    return scraped_data


if __name__ == "__main__":
    books = scrape_books(URL)

    for book in books:
        print(book)

