from module_book.book import Book
import csv

'''I'd like to add a way to create a list of 
dictionaries each representing every attributes of a book object
and when the list is big enough (100 book?) load them all in a csv as a batch
but i will need to create a function to get url(s) from the site booktoscrap
first. Below is a placeholder code to create a csv'''

def main():
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    url_2 = "https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html"
    book = Book.from_url(url)
    book_2 = Book.from_url(url_2)

    dictionary_book = vars(book)
    dictionary_book_2 = vars(book_2)

    csv_variable_name = "automated_name_later"+".csv"

    with open(csv_variable_name, "w", newline="") as myfile:
        wro = csv.DictWriter(myfile, fieldnames=dictionary_book.keys())
        wro.writeheader()
        wro.writerow(dictionary_book)
        wro.writerow(dictionary_book_2)



if __name__ == "__main__":
    main()
