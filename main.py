import src.load_csv
import src.urls_scraper
import src.bookclass


def main():
    csv_input = input(
        "\nYou are about to extract datas about every product from the website books.toscrape.com.\n"
        " Proceed (Y/N) ? ")
    # Small UI using the console
    while True:
        if csv_input == "N" or csv_input == "n":
            print("\n########################################"
                  "\n############# GOODBYE ##################"
                  "\n########################################")
            exit()

        elif csv_input == "Y" or csv_input == "y":
            print("\n########################################"
                  "\n##### I WILL DOWNLOAD .CSV FILE(S) #####"
                  "\n########################################")
            break

        else:
            print("\n\ninvalid input, try again\n")
            csv_input = input(
                "Do you want to extract information about every product from the website books.toscrape.com. (Y/N) ? ")

    img_input = input("\nDo you also want to download images from the website (Y/N) ? ")
    while True:
        if img_input == "Y" or img_input == "y":
            print("\n########################################"
                  "\n##### I WILL DOWNLOAD .JPG FILE(S) #####"
                  "\n########################################")
            break

        elif img_input == "N" or img_input == "n":
            print("\n########################################"
                  "\n#### I WON'T DOWNLOAD .JPG FILE(S) #####"
                  "\n########################################")
            break

        else:
            print("\ninvalid input, try again")
            img_input = input("Do you want to download images from the website : books.toscrape.com ? (Y/N)")

    print("\n\n########################################"
          "\n######### DOWNLOAD IN PROGRESS #########"
          "\n############# DO NOT EXIT ##############"
          "\n########################################\n", flush=True)

    url = "https://books.toscrape.com/index.html"
    # url can also work with : "https://books.toscrape.com/catalogue/category/books_1/index.html" but it may break if
    # it starts with another url.
    list_of_category_url = src.urls_scraper.get_list_category_page_url(url)
    # create a list of links for every category
    for url_category in list_of_category_url:
        # for every category, create a list of links for every product, then create object Book for every product.
        # then transform Book object in dictionaries and load them in a CSV.
        # if the users asked for images, it uses the attribute "image_url" of Books to download the images.
        list_of_url = src.urls_scraper.get_product_pages_urls(url_category)
        list_of_books = src.load_csv.book_creator(list_of_url)
        src.load_csv.csv_loader(list_of_books)
        if img_input == "Y" or img_input == "y":
            for book in list_of_books[0]:
                book.get_img()

    print("\n########################################"
          "\n############# GOODBYE ##################"
          "\n########################################")


if __name__ == "__main__":
    main()
