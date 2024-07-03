import requests
from bs4 import BeautifulSoup


def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def get_next_page_url(url):
    # get the url linked to the button next and return it, if there is none, return None
    # not using .get("href") but possible if .find("a") added before
    next_button = get_soup(url).find("li", class_="next")
    if next_button:
        next_button = next_button.find("a")["href"]
        i = url.rfind("/")
        next_url = url[:i + 1] + next_button
        return next_url
    else:
        return None


def get_list_product_page_url(url):
    list_of_link = []
    all_h3 = get_soup(url).find_all("h3")
    for h3 in all_h3:
        x = h3.find("a")["href"]
        list_of_link.append("https://books.toscrape.com/catalogue" + x[8:])
    return list_of_link


def create_csv_name(url):
    i = url.rindex("/", 0, url.rfind("/"))
    j = url.rfind("_")
    category_name = url[i + 1:j]
    return category_name


def get_list_category_page_url(url):
    list_of_link = []
    soup = get_soup(url).find("ul", class_="nav nav-list").find_all("a")
    i = url.rfind("/")
    for link in soup:
        x = link.get("href")
        list_of_link.append(url[:i + 1] + x)
    list_of_link.pop(0)
    return list_of_link


def get_product_pages_urls(url):
    urls = []
    csv_name = create_csv_name(url)
    while True:
        url_page = get_list_product_page_url(url)
        urls.extend(url_page)
        url = get_next_page_url(url)
        if url is None:
            break
    return urls, csv_name


def main():
    url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    # url_3 = "https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html"

    test = get_product_pages_urls(url)
    print(test)


if __name__ == "__main__":
    main()
