import sys

sys.path.insert(0, 'src')
# # temporary solution to allow the importation of some modules. Resolve it later

from src.load_csv import csv_loader
from src.urls_scraper import get_product_pages_urls, get_list_category_page_url


def main():

    # test avec une page produit
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    csv_loader(url)
    #
    # test avec une page catégorie (placé page 1)
    url2 = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    get_url2 = get_product_pages_urls(url2)
    csv_loader(get_url2)



    # url = "https://books.toscrape.com/index.html"
    # list_category = get_list_category_page_url(url)
    # for category in list_category:
    #     get_url = get_product_pages_urls(category)
    #     csv_loader(get_url)


if __name__ == "__main__":
    main()
