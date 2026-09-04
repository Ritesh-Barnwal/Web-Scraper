import requests
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>My Products</h1>

        <div class="product">
            <h2>iPhone</h2>
            <p class="price">₹70,000</p>
        </div>

        <div class="product">
            <h2>Samsung</h2>
            <p class="price">₹60,000</p>
        </div>

        <div class="product">
            <h2>Pixel</h2>
            <p class="price">₹50,000</p>
        </div>
    </body>
</html>
"""


soup = BeautifulSoup(html, "html.parser")

products = soup.find_all("div", class_="product")

for product in products:
    name = product.find("h2").get_text(strip=True)
    price = product.find("p", class_="price").get_text(strip=True)

    print("Product:", name)
    print("Price:", price)
