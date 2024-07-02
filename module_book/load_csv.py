from urls_scraper import get_product_pages_urls
from create_dictionnaries import create_dictionary
import csv


def main():
    url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    urls = get_product_pages_urls(url)

    batch = []
    for i in urls:
        book = create_dictionary(i)
        batch.append(book)

    csv_variable_name = "automated_name_later" + ".csv"

    with open(csv_variable_name, "w", newline="") as myfile:
        wro = csv.DictWriter(myfile, fieldnames=batch[0].keys())
        wro.writeheader()
        for i in batch:
            wro.writerow(i)

    print("CSV LOADED")


if __name__ == "__main__":
    main()
