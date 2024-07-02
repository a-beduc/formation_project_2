import sys

sys.path.insert(0, 'src')
#temporary solution to allow the importation of some modules. Resolve it later

from src.load_csv import csv_loader
from src.urls_scraper import get_product_pages_urls


def main():
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    csv_loader(url, "testunique")

    url2 = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    get_url2 = get_product_pages_urls(url2)
    csv_loader(get_url2, "testmultiple")


if __name__ == "__main__":
    main()
