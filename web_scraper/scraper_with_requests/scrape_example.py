import requests
from bs4 import BeautifulSoup


def scrape_site(url):
    # Send an HTTP request to the URL of the webpage you want to access
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the title and description of the webpage
    title = soup.title.string
    description = ""

    description_meta_tag = soup.find("meta", attrs={"name": "description"})
    if description_meta_tag:
        description = description_meta_tag["content"]

    return title, description


if __name__ == "__main__":
    url = "https://example.com"
    title, description = scrape_site(url)
    print(f"Title: {title}. Description: {description}")
