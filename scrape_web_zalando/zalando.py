import inspect
import json
from pathlib import Path
import time

from playwright.sync_api import sync_playwright

LIST_URL = [
    "https://www.zalando.co.uk/under-armour-tech-tee-sports-shirt-un242d0cl-q11.html",
    "https://www.zalando.co.uk/under-armour-tech-tee-sports-shirt-un242d0cl-k11.html",
    "https://www.zalando.co.uk/under-armour-tech-tee-sports-shirt-un242d0cl-a11.html",
    "https://www.zalando.co.uk/nike-sportswear-club-tracksuit-bottoms-ni122e05h-q11.html",
    "https://www.zalando.co.uk/calvin-klein-underwear-low-rise-trunk-3-pack-pants-black-c1152k00m-802.html",
    "https://www.zalando.co.uk/pier-one-tracksuit-bottoms-mottled-light-grey-pi922e03i-c11.html",
    "https://www.zalando.co.uk/nike-sportswear-club-tracksuit-bottoms-dark-grey-heathermatte-silverwhite-ni122e05i-c11.html",
    "https://www.zalando.co.uk/under-armour-tracksuit-bottoms-halo-grayblack-un242e0so-c11.html",
    "https://www.zalando.co.uk/under-armour-graphic-shorts-sports-shorts-pitch-gray-black-un242e0n1-c11.html",
    "https://www.zalando.co.uk/yourturn-sweatshirt-blue-yo12100w6-k12.html",
]

class ZalandoProductsScraper:
    def __init__(self, **kwargs):
        self.browser = None
        self.page = None
        self._default_page_width = 1200
        self._default_page_height = 800

    def create_new_page(self):
        page = self.browser.new_page()
        page.set_viewport_size(
            {
                "width": self._default_page_width,
                "height": self._default_page_height,
            }
        )
        return page

    def initialize_browser(self, playwright):
        firefox = playwright.firefox
        self.browser = firefox.launch(
            headless=True,
        )
        self.firefox = firefox
        return self.browser

    def process(self):
        products = []
        for url in LIST_URL:
            time.sleep(1)
            self.page.goto(url, wait_until="domcontentloaded")
            data = self.page.query_selector('script[type="application/ld+json"]')
            if data:
                data = json.loads(data.text_content())
            else:
                return
            title = f'{data.get("manufacturer")} {data.get("name")}'
            description = data.get("description")
            listing_url = f'https://www.zalando.co.uk/{data.get("url")}'
            price = data.get("offers", [])[0].get("price")
            product = {
                "listing_url": listing_url,
                "title": title,
                "description": description,
                "price": price
            }
            products.append(product)
        return products
    
    def run(self):
        with sync_playwright() as playwright:
            self.initialize_browser(playwright)
            self.page = self.create_new_page()
            products = self.process()
            file_path = (
                Path(inspect.getfile(self.__class__))
                .resolve()
                .parent
            ) / "results.json"
            if products:
                with open(file_path, "w", encoding="utf-8") as fp:
                    try:
                        json.dump(
                            products,
                            fp,
                            indent=4,
                            ensure_ascii=False,
                        )
                    except Exception as ex:
                        print(f"Error while writing JSON: {ex}")
            self.browser.close()


if __name__ == "__main__":
    scraper = ZalandoProductsScraper()
    scraper.run()
