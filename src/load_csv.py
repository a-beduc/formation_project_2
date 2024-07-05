import csv
from .bookclass import Book
from datetime import datetime
import os


def create_csv_directory():
    # create a directory named "csv" if it doesn't exist
    category_dir = os.path.join("csv")
    os.makedirs(category_dir, exist_ok=True)


def create_csv_file_name(category):
    # create a file in the directory csv with the name of the category and the date/min
    now = str(datetime.now())
    reformated_now = now[0:10] + "_" + now[11:13] + "-" + now[14:16]
    csv_file = category + "_" + reformated_now + ".csv"
    return csv_file


def book_creator(tuple_list_of_url_category):
    # create instances of book from product_url, and return a tuple containing ([list of object book], category)
    if not isinstance(tuple_list_of_url_category, tuple):
        tuple_list_of_url_category = ([tuple_list_of_url_category], "no_category")
    list_of_books = []
    for url in tuple_list_of_url_category[0]:
        books_of_url = Book.from_url(url)
        list_of_books.append(books_of_url)
    return list_of_books, tuple_list_of_url_category[1]


def csv_loader(tuple_list_of_books_category, batch_size=20):
    # create csv file in a csv directory with content extracted from a tuple ([list of object book], category)
    create_csv_directory()
    csv_file_name = create_csv_file_name(tuple_list_of_books_category[1])
    csv_path = os.path.join("csv", csv_file_name)
    headers = vars(tuple_list_of_books_category[0][0])

    with open(csv_path, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers.keys())
        writer.writeheader()

        current_batch = []

        for book in tuple_list_of_books_category[0]:
            dictionary_of_book = vars(book)
            current_batch.append(dictionary_of_book)
            if len(current_batch) == batch_size:
                writer.writerows(current_batch)
                current_batch = []

        if current_batch:
            writer.writerows(current_batch)
