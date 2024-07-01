from module_book.book import Book


def main():
    url = "https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html"
    # url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    book = Book.from_url(url)
    print(book.category)
    print(book.title)
    print(book.price)
    print(book.stock)
    print(book.star_rating)
    print(book.description)
    print(book.upc)
    print(book.product_type)
    print(book.price_without_tax)
    print(book.price_with_tax)
    print(book.tax)
    print(book.availability)
    print(book.number_of_review)


if __name__ == "__main__":
    main()
