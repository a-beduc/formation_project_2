import requests
from bs4 import BeautifulSoup
import re


class Book:
    def __init__(self, category, title, price, stock, star_rating, description, upc, product_type, price_without_tax,
                 price_with_tax, tax, availability, number_of_review):
        self.category = category
        self.title = title
        self.price = price
        self.stock = stock
        self.star_rating = star_rating
        self.description = description
        self.upc = upc
        self.product_type = product_type
        self.price_without_tax = price_without_tax
        self.price_with_tax = price_with_tax
        self.tax = tax
        self.availability = availability
        self.number_of_review = number_of_review

    @staticmethod
    def clean_number_float(number):
        float_number = float((re.findall(r'\d+.\d+', number))[0])
        return float_number

    @staticmethod
    def clean_number_int(number):
        int_number = int((re.findall(r'\d+', number))[0])
        return int_number

    @staticmethod
    def extract_category_from_soup(soup):
        category = soup.find(name="ul", class_="breadcrumb")
        category = category.li.find_next_sibling("li").find_next_sibling("li").text.strip()
        return category

    @staticmethod
    def extract_title_from_soup(soup):
        title = soup.find("div", class_="col-sm-6 product_main").find("h1").text.strip()
        return title

    @staticmethod
    def extract_price_from_soup(soup):
        price = soup.find(name="p", class_="price_color").text.strip()
        price = float(str(price[1:]))
        return price

    @staticmethod
    def extract_stock_from_soup(soup):
        stock = soup.find(name="p", class_="instock availability").text.strip()
        stock = Book.clean_number_int(stock)
        return stock

    @staticmethod
    def extract_star_rating_from_soup(soup):
        star_rating = 0
        str_star_rating = str(soup.find_all("p"))
        index_star_notation = str_star_rating.find("star-rating")
        cas = ""
        for i in range(index_star_notation + 12, index_star_notation + 15):
            cas = cas + str_star_rating[i]
        match cas:
            case 'One':
                star_rating = 1
            case 'Two':
                star_rating = 2
            case 'Thr':
                star_rating = 3
            case 'Fou':
                star_rating = 4
            case 'Fiv':
                star_rating = 5
        return star_rating

    @staticmethod
    def extract_description_from_soup(soup):
        description = soup.find(name="div", class_="sub-header").find_next("p").text.strip()
        return description

    @staticmethod
    def extract_table_product_information(soup):
        table_product_information = soup.find(name="table", class_="table table-striped").find_all("td")
        list_table = []
        for i in table_product_information:
            list_table.append(i.text.strip())
        return list_table

    @classmethod
    def from_url(cls, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        category = cls.extract_category_from_soup(soup)
        title = cls.extract_title_from_soup(soup)
        price = cls.extract_price_from_soup(soup)
        stock = cls.extract_stock_from_soup(soup)
        star_rating = cls.extract_star_rating_from_soup(soup)
        description = cls.extract_description_from_soup(soup)
        upc = cls.extract_table_product_information(soup)[0]
        product_type = cls.extract_table_product_information(soup)[1]
        price_without_tax = cls.clean_number_float(cls.extract_table_product_information(soup)[2])
        price_with_tax = cls.clean_number_float(cls.extract_table_product_information(soup)[3])
        tax = cls.clean_number_float(cls.extract_table_product_information(soup)[4])
        availability = cls.clean_number_int(cls.extract_table_product_information(soup)[5])
        number_of_review = cls.extract_table_product_information(soup)[6]

        return cls(category=category, title=title, price=price, stock=stock, star_rating=star_rating,
                   description=description, upc=upc, product_type=product_type, price_without_tax=price_without_tax,
                   price_with_tax=price_with_tax, tax=tax, availability=availability, number_of_review=number_of_review)


def main():
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
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
