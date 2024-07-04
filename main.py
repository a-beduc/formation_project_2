import sys

sys.path.insert(0, 'src')
# # temporary solution to allow the importation of some modules. Resolve it later

from src.load_csv import csv_loader
from src.urls_scraper import get_product_pages_urls, get_list_category_page_url


def main():
    csv_input = input(
        "You are about to extract information about every product from the website books.toscrape.com.\n\n "
        "Proceed (Y/N) ? ")
    while True:
        if csv_input == "N" or csv_input == "n":
            print("\nThanks you for using our script.\n\nGoodbye.\n")
            exit()

        elif csv_input == "Y" or csv_input == "y":
            print("\n##### .CSV FILE(S) DOWNLOADED #####\n")
            break

        else:
            print("\n\ninvalid input, try again\n")
            csv_input = input(
                "Do you want to extract information about every product from the website books.toscrape.com. (Y/N)")

    # test avec une page produit
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    csv_loader(url)
    #
    # test avec une page catégorie (placé page 1)
    # url2 = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    # get_url2 = get_product_pages_urls(url2)
    # csv_loader(get_url2)
    #
    # url = "https://books.toscrape.com/index.html"
    # list_category = get_list_category_page_url(url)
    # for category in list_category:
    #     get_url = get_product_pages_urls(category)
    #     csv_loader(get_url)

    img_input = input("Do you want to download images from the website : books.toscrape.com ? (Y/N)")
    while True:
        if img_input == "N" or img_input == "n":
            print("\nThanks you for using our script.\n\nGoodbye.\n")
            exit()

        elif img_input == "Y" or img_input == "y":
            print("\n##### .JPG FILE(S) DOWNLOADED #####\n")
            print("\nThanks you for using our script.\n\nGoodbye.\n")
            exit()

        else:
            print("\ninvalid input, try again")
            img_input = input("Do you want to download images from the website : books.toscrape.com ? (Y/N)")


if __name__ == "__main__":
    main()
