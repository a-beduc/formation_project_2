import module_book.urls_scraper
from module_book.load_csv import csv_loader


def main():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    urls = module_book.urls_scraper.get_product_pages_urls(url)
    csv_loader(urls, "test")


if __name__ == "__main__":
    main()
