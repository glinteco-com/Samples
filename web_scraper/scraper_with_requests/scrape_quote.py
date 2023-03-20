import json

import requests
from bs4 import BeautifulSoup


def scrape_site(url):
    # Send an HTTP request to the URL of the webpage you want to access
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    quote_divs = soup.find_all("div", attrs={"class": "quote"})
    quotes = []
    for quote_div in quote_divs:
        quote_content = quote_div.find("span", attrs={"class": "text"}).string[
            1:-1
        ]
        tag_divs = quote_div.find_all("a", attrs={"class": "tag"})
        quote_tags = [
            tag_div.string
            for tag_div in quote_div.find_all("a", attrs={"class": "tag"})
        ]
        quotes.append({"content": quote_content, "tags": quote_tags})

    return quotes


if __name__ == "__main__":
    url = "http://quotes.toscrape.com/page/1/"
    quotes = scrape_site(url)
    print(json.dumps(quotes, indent=4))
