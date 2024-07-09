import re
from src.urls_scraper import get_soup
import os
import requests


class Book:
    def __init__(self, product_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                 number_available, product_description, category, review_rating, image_url):
        # Initialization of attributes
        self.product_url = product_url
        self.universal_product_code = universal_product_code
        self.title = title
        self.price_including_tax = price_including_tax
        self.price_excluding_tax = price_excluding_tax
        self.number_available = number_available
        self.product_description = product_description
        self.category = category
        self.review_rating = review_rating
        self.image_url = image_url

    @staticmethod
    def clean_number_float(number):
        # transform a string into a float
        float_number = float((re.findall(r'\d+.\d+', number))[0])
        return float_number

    @staticmethod
    def clean_number_int(number):
        # transform a string into an int
        int_number = int((re.findall(r'\d+', number))[0])
        return int_number

    @staticmethod
    def extract_category_from_soup(soup):
        # extract the category from the navigation bar
        category = soup.find(name="ul", class_="breadcrumb")
        category = category.li.find_next_sibling("li").find_next_sibling("li").text.strip()
        return category.lower()

    @staticmethod
    def extract_title_from_soup(soup):
        # extract the title ; could have been using only find("h1") since there is only one <h1></h1>
        title = soup.find("div", class_="col-sm-6 product_main").find("h1").text.strip()
        return title

    @staticmethod
    def extract_star_rating_from_soup(soup):
        # extract the number of stars attributed to a book from 1 to 5
        review_rating = 0
        str_star_rating = str(soup.find_all("p"))
        index_star_notation = str_star_rating.find("star-rating")
        cas = ""
        # create a string of 3 characters from the classes star-rating One / Two / Three / Four / Five and match it
        for i in range(index_star_notation + 12, index_star_notation + 15):
            cas = cas + str_star_rating[i]
        match cas:
            case 'One':
                review_rating = 1
            case 'Two':
                review_rating = 2
            case 'Thr':
                review_rating = 3
            case 'Fou':
                review_rating = 4
            case 'Fiv':
                review_rating = 5
        return review_rating

    @staticmethod
    def extract_description_from_soup(soup):
        product_description = soup.find(name="div", class_="sub-header").find_next("p").text.strip()
        return product_description

    @staticmethod
    def extract_table_product_information(soup):
        # extract the whole table containing information on the product ; return the values as a list
        table_product_information = soup.find(name="table", class_="table table-striped").find_all("td")
        list_table = []
        for i in table_product_information:
            list_table.append(i.text.strip())
        return list_table

    @staticmethod
    def extract_img_url_from_soup(soup):
        img_link = soup.find("div", class_="item active").img.get("src")
        image_url = "https://books.toscrape.com" + img_link[4:]
        return image_url

    @classmethod
    def from_url(cls, url):
        """ initiate the values of the attributes of the class from an url and return an object.
        the datas contained within the list extracted from the table are initiated using their index.
        The whole process might break if a product has a different html structure
        """
        soup = get_soup(url)

        product_url = url
        universal_product_code = cls.extract_table_product_information(soup)[0]
        title = cls.extract_title_from_soup(soup)
        price_including_tax = cls.clean_number_float(cls.extract_table_product_information(soup)[3])
        price_excluding_tax = cls.clean_number_float(cls.extract_table_product_information(soup)[2])
        number_available = cls.clean_number_int(cls.extract_table_product_information(soup)[5])
        product_description = cls.extract_description_from_soup(soup)
        category = cls.extract_category_from_soup(soup)
        review_rating = cls.extract_star_rating_from_soup(soup)
        image_url = cls.extract_img_url_from_soup(soup)

        return cls(product_url=product_url, universal_product_code=universal_product_code, title=title,
                   price_including_tax=price_including_tax, price_excluding_tax=price_excluding_tax,
                   number_available=number_available, product_description=product_description, category=category,
                   review_rating=review_rating, image_url=image_url)

    def get_img(self):
        # download image from the link stored in the attribute image_url
        # name it and store it in appropriate directory
        category_dir = os.path.join("img", self.category)
        os.makedirs(category_dir, exist_ok=True)
        string_title = self.product_url
        index_of_last_slash = string_title.rfind("/")
        string_title_without_last_part = string_title[:index_of_last_slash]
        index_of_second_last_slash = string_title_without_last_part.rfind("/")
        index_of_underscore = string_title.rfind("_")
        string_title = string_title[index_of_second_last_slash + 1:index_of_underscore]
        extension = self.image_url.split(".")[-1]
        file_path_name = "img/" + self.category + '/' + string_title + "." + extension
        data = requests.get(self.image_url).content
        with open(file_path_name, 'wb') as img:
            img.write(data)