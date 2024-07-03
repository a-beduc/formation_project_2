import csv
import bookclass
from urls_scraper import get_product_pages_urls
from datetime import datetime


def create_dictionary(product_url):
    # create a dictionary where key = attribute of a class and value the value of the object
    books = bookclass.Book.from_url(product_url)
    books = vars(books)
    return books


def csv_loader(list_of_url, batch_size=20):
    # create csv file with content extracted from a list of urls and name it based on url
    # if its not a tuple, convert entry to tuple ([list], category)
    if not isinstance(list_of_url, tuple):
        list_of_url = ([list_of_url], "no_category")

    # create a name for the file
    now = str(datetime.now())
    reformated_now = now[0:10] + "_" + now[11:13] + "-" + now[14:16]
    csv_file = list_of_url[1] + "_" + reformated_now + ".csv"

    # create the header
    list_of_urls = list_of_url[0]
    header = create_dictionary(list_of_urls[0])

    # add content to a csv, create it if necessary, add rows as batches
    with open(csv_file, 'a', newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header.keys())
        writer.writeheader()

        current_batch = []

        for url in list_of_urls:
            books = create_dictionary(url)
            current_batch.append(books)
            if len(current_batch) == batch_size:
                writer.writerows(current_batch)
                current_batch = []

        if current_batch:
            writer.writerows(current_batch)


def main():
    # to test the code : expected create files csv
    url_2 = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    csv_loader(url_2)

    url2 = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    get_url2 = get_product_pages_urls(url2)
    csv_loader(get_url2)


if __name__ == "__main__":
    main()
