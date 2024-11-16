import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL of the website
base_url = "https://thefirstedition.com"

# Headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def get_total_pages(category_url):
    response = requests.get(category_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the pagination element and extract the total number of pages
    pagination = soup.find("nav", class_="woocommerce-pagination")
    if pagination:
        pages = pagination.find_all("a")
        if pages:
            last_page = pages[-2].get_text()
            return int(last_page)
    return


def extract_book_details(book_url):
    response = requests.get(book_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    details = {}
    # Extract SKU
    sku = soup.find("span", class_="sku")
    details["SKU"] = sku.get_text(strip=True) if sku else None
    # Extract title
    title = soup.find("h1", class_="product_title")
    details["Title"] = title.get_text(strip=True) if title else None
    # Extract price
    price = soup.find("p", class_="price")
    details["Price"] = price.get_text(strip=True) if price else None
    # Extract description
    description = soup.find("div", class_="woocommerce-product-details__short-description")
    details["Description"] = description.get_text(strip=True) if description else None
    return details


def scrape_category(category_url):
    books = []
    total_pages = get_total_pages(category_url)
    for page in range(1, total_pages + 1):
        print(f"Scraping page {page} of {total_pages} in category {category_url}")
        page_url = f"{category_url}/page/{page}/"
        response = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        # Find all book links on the page
        book_links = soup.find_all("a", class_="woocommerce-LoopProduct-link")
        for link in book_links:
            book_url = link.get("href")
            print(f"Scraping book: {book_url}")
            book_details = extract_book_details(book_url)
            books.append(book_details)
            time.sleep(1)  # Delay to avoid overwhelming the server
    return books


# Choose a category to scrape
category_url = "https://thefirstedition.com/product-category/literature-classics/"

# Scrape the chosen category
books_data = scrape_category(category_url)

# Convert the list of books to a DataFrame
df = pd.DataFrame(books_data)

# Save to CSV
df.to_csv("the_first_edition_books.csv", index=False)
print("Scraping completed. Data saved to 'the_first_edition_books.csv'")
