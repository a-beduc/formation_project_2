import requests
from bs4 import BeautifulSoup


def get_soup(url):
    # get html content
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def get_list_category_page_url(url):
    # get the urls that link to categories and put them in a list
    list_of_link = []
    soup = get_soup(url).find("ul", class_="nav nav-list").find_all("a")
    category_link_start = "https://books.toscrape.com/catalogue/category/books"
    for link in soup:
        category_link_end = link.get("href")
        j = category_link_end[:(category_link_end.rfind("/"))].rfind("/")
        list_of_link.append(category_link_start + category_link_end[j:])
    list_of_link.pop(0)
    return list_of_link


def get_next_page_url(url):
    # get the url linked to the button next and return it, if there is none, return None
    # not using .get("href") but possible if .find("a") added beforehand
    next_button = get_soup(url).find("li", class_="next")
    if next_button:
        next_button = next_button.find("a")["href"]
        i = url.rfind("/")
        next_url = url[:i + 1] + next_button
        return next_url
    else:
        return None


def get_list_product_page_url(url):
    # find every link to a product found in a page and add it to a list
    list_of_link = []
    all_h3 = get_soup(url).find_all("h3")
    for h3 in all_h3:
        x = h3.find("a")["href"]
        list_of_link.append("https://books.toscrape.com/catalogue" + x[8:])
    return list_of_link


def create_category_name(url):
    # get the category from the url based on ../category_number/whatever.html
    i = url.rindex("/", 0, url.rfind("/"))
    j = url.rfind("_")
    category_name = url[i + 1:j]
    return category_name


def get_product_pages_urls(url):
    # find every link to a product found in a category and add it to a list
    urls = []
    category = create_category_name(url)
    while True:
        url_page = get_list_product_page_url(url)
        urls.extend(url_page)
        url = get_next_page_url(url)
        if url is None:
            break
    return urls, category

