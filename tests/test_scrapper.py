from src.scraper import scrape_books
from src.config import URL

def test_scrape_books():
    books = scrape_books(URL, 1)

    assert len(books) > 0

    for book in books:
        assert book["title"]
        assert book["price"]
        assert book["rating"]
        assert book["link"]
