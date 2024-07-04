import sys
from time import sleep

sys.path.insert(0, 'src')
import src.load_csv
import src.urls_scraper
import src.bookclass


def main():
    csv_input = input(
        "You are about to extract datas about every product from the website books.toscrape.com.\n\n "
        "Proceed (Y/N) ? ")
    while True:
        if csv_input == "N" or csv_input == "n":
            print("\n########################################\n"
                  "\n############# GOODBYE ##################\n"
                  "\n########################################\n")
            exit()

        elif csv_input == "Y" or csv_input == "y":
            print("\n########################################\n"
                  "\n##### I WILL DOWNLOAD .CSV FILE(S) #####\n"
                  "\n########################################\n")
            break

        else:
            print("\n\ninvalid input, try again\n")
            csv_input = input(
                "Do you want to extract information about every product from the website books.toscrape.com. (Y/N)")

    img_input = input("Do you want to download images from the website : books.toscrape.com ? (Y/N)")
    while True:
        if img_input == "Y" or img_input == "y":
            print("\n########################################\n"
                  "\n##### I WILL DOWNLOAD .JPG FILE(S) #####\n"
                  "\n########################################\n")
            break

        elif img_input == "N" or img_input == "n":
            print("\n########################################\n"
                  "\n##### I WON'T DOWNLOAD .JPG FILE(S) #####\n"
                  "\n########################################\n")
            break

        else:
            print("\ninvalid input, try again")
            img_input = input("Do you want to download images from the website : books.toscrape.com ? (Y/N)")

    print("\n\n########################################\n"
          "\n######### DOWNLOAD IN PROGRESS #########\n"
          "\n############# DO NOT EXIT ##############\n"
          "\n########################################\n\n", flush=True)

    sleep(1)

    # # To test the program with one category.
    # url = "https://books.toscrape.com/catalogue/category/books/religion_12/index.html"
    # list_of_url = src.urls_scraper.get_product_pages_urls(url)
    # list_of_books = src.load_csv.book_creator(list_of_url)
    # src.load_csv.csv_loader(list_of_books)
    # if img_input == "Y" or img_input == "y":
    #     for book in list_of_books[0]:
    #         book.get_img()

    url = "https://books.toscrape.com/index.html"
    list_of_category_url = src.urls_scraper.get_list_category_page_url(url)
    for url_category in list_of_category_url:
        list_of_url = src.urls_scraper.get_product_pages_urls(url_category)
        list_of_books = src.load_csv.book_creator(list_of_url)
        src.load_csv.csv_loader(list_of_books)
        if img_input == "Y" or img_input =="y":
            for book in list_of_books[0]:
                book.get_img()


    print("\n########################################\n"
          "\n############# GOODBYE ##################\n"
          "\n########################################\n")

if __name__ == "__main__":
    main()
