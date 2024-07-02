from create_dictionnaries import create_dictionary
import csv


def csv_loader(list_of_url, csv_name, batch_size=20):
    if not isinstance(list_of_url, list):
        list_of_url = [list_of_url]

    csv_file = csv_name + ".csv"
    header = create_dictionary(list_of_url[0])

    with open(csv_file, 'a', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header.keys())
        writer.writeheader()

        current_batch = []

        for url in list_of_url:
            book = create_dictionary(url)
            current_batch.append(book)
            if len(current_batch) == batch_size:
                writer.writerows(current_batch)
                current_batch = []

        if current_batch:
            writer.writerows(current_batch)

    return print("\n\ntravaille termine\n\n")


def main():
    url_2 = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    csv_loader(url_2, "testunique")


if __name__ == "__main__":
    main()
