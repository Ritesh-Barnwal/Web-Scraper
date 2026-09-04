Web Scraping Notes

1. What is Web Scraping?

Web scraping is the process of automatically collecting useful
information from webpages using a program.

2. What is HTML Parsing?

HTML parsing means converting HTML into a structure that a program
can understand and navigate.

3. Requests

Requests is used to send an HTTP request to a website and retrieve
the webpage's HTML.

Example:
response = requests.get(url)

4. BeautifulSoup

BeautifulSoup is used to parse HTML and search through its structure
to find the information we need.

import requests
from bs4 import BeautifulSoup
web = requests.get("https://www.geeksforgeeks.org/")

5. Finding Elements

BeautifulSoup provides methods such as find() and find_all().

find()

Finds the first matching element.

soup.find("h1")
find_all()

Finds all matching elements.

soup.find_all("h2")
6. Finding by Class

We can search for elements using their CSS class.

soup.find("div", class_="product")
7. Extracting Text

After finding an element, we can extract its text.

element.get_text(strip=True)
8. Extracting Attributes

HTML elements can contain attributes such as href and src.

Example:

link["href"]