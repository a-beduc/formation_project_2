import csv
import bookclass
from urls_scraper import get_product_pages_urls
from datetime import datetime


def create_dictionary(product_url):
    books = bookclass.Book.from_url(product_url)
    books = vars(books)
    return books


def csv_loader(list_of_url, batch_size=20):
    if not isinstance(list_of_url, tuple):
        list_of_url = ([list_of_url], "no_category")

    list_of_urls = list_of_url[0]
    now = str(datetime.now())
    reformated_now = now[0:10] + "_" + now[11:13] + "-" + now[14:16]
    csv_file = reformated_now + "_" + list_of_url[1] + ".csv"
    header = create_dictionary(list_of_urls[0])

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

    return print("\n\ntravaille termine\n\n")


def main():
    url_2 = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    csv_loader(url_2)

    url2 = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    get_url2 = get_product_pages_urls(url2)
    csv_loader(get_url2)


if __name__ == "__main__":
    main()
