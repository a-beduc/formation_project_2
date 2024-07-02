from book import Book


def create_dictionary(product_url):
    book = Book.from_url(product_url)
    book = vars(book)
    return book
