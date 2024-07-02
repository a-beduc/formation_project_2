import requests
from bs4 import BeautifulSoup


def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def get_next_page_url(url):
    # get the url linked to the button next and return it, if there is none, return None
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


def get_product_pages_urls(url):
    urls = []
    while True:
        url_page = get_list_product_page_url(url)
        urls.extend(url_page)
        url = get_next_page_url(url)
        if url is None:
            break
    return urls


def main():
    url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    # url_3 = "https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html"

    test = get_product_pages_urls(url)
    print(test)


if __name__ == "__main__":
    main()
