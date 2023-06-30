# Python 3.11

import argparse
import csv

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"


def scrape_url(url):
    print(f"Scrape url {url}")
    response = requests.get(url)

    if response.status_code != 200:
        breakpoint()

    soup = BeautifulSoup(response.text, "html.parser")
    quote_divs = soup.select(".quote")

    quotes = []
    for quote_div in quote_divs:
        text = quote_div.select_one(".text").get_text()
        if '"' in text:
            text = text.replace('"', "")
        if "“" in text:
            text = text.replace("“", "")
        if "”" in text:
            text = text.replace("”", "")
        author = quote_div.select_one(".author").get_text()
        quote = {"text": text, "author": author}
        quotes.append(quote)

    print(f"Found #{len(quotes)} quotes")

    next_url = None
    if soup.select_one(".next > a"):
        next_link = soup.select_one(".next > a")["href"]
        next_url = f"{BASE_URL}{next_link}"

    return next_url, quotes


def write_to_file(file_name, quotes):
    field_names = ["author", "text"]
    with open(file_name, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(quotes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape quotes")
    parser.add_argument("-f", "--file_name")
    args = parser.parse_args()

    file_name = "quotes.csv"
    if args.file_name:
        file_name = args.file_name

    print("Start scraping")
    next_url = "https://quotes.toscrape.com/"
    quotes = []
    while next_url:
        next_url, new_quotes = scrape_url(next_url)
        quotes.extend(new_quotes)
    print(f"Total found #{len(quotes)}")
    write_to_file(file_name, quotes)
