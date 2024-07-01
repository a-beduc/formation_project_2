# ceci est un commentaire test pour m'entraîner sur GitHub
import requests
from bs4 import BeautifulSoup
import re


def main():
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    # url = "https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    """example : <div class="col-sm-6 product_main"> <h1> TITRE </h1>"""
    """search for a <h1> in a <div> that contains the class : "col-sm-6 product_main" 
     and get rid of the <x> and get rid of excess spaces"""

    category = soup.find(name="ul", class_="breadcrumb").li.find_next_sibling("li").find_next_sibling("li").text.strip()

    title = soup.find("div", class_="col-sm-6 product_main").find("h1").text.strip()

    price = soup.find(name="p", class_="price_color").text.strip()
    price = float(str(price[1:]))

    stock = soup.find(name="p", class_="instock availability").text.strip()
    stock = int((re.findall(r'\d+', stock))[0])

    star_rating = 0
    str_star_rating = str(soup.find_all("p"))
    index_star_notation = str_star_rating.find("star-rating")
    cas = ""

    for i in range(index_star_notation + 12, index_star_notation + 15):
        print(str_star_rating[i])
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

    description = soup.find(name="div", class_="sub-header").find_next("p").text.strip()

    table_product_information = soup.find(name="table", class_="table table-striped").find_all("td")
    list_table = []
    for i in table_product_information:
        list_table.append(i.text.strip())

    upc = list_table[0]
    product_type = list_table[1]
    price_without_tax = float((re.findall(r'\d+.\d+', list_table[2]))[0])
    price_with_tax = float((re.findall(r'\d+.\d+', list_table[3]))[0])
    tax = float((re.findall(r'\d+.\d+', list_table[4]))[0])
    availability = int((re.findall(r'\d+', list_table[5]))[0])
    number_of_review = list_table[6]

    print(f"Category : {category}")
    print("--------")
    print(f"Le titre de ce livre est \"{title}\".")
    print("--------")
    print(f"{title} coûte : {price} en livres sterlings")
    print("--------")
    print(f"Il y a {stock} exemplaires de {title} en stock")
    print("--------")
    print(f"Le livre a un score de {star_rating} étoile(s).")
    print("--------")
    print(f"Resume de l'oeuvre : {description}")
    print("--------")
    print(f"Code UPC : {upc}")
    print("--------")
    print(f"Type de produit : {product_type}")
    print("--------")
    print(f"Prix sans taxe : {price_without_tax} en livres sterlings")
    print("--------")
    print(f"Prix avec taxe : {price_with_tax} en livres sterlings")
    print("--------")
    print(f"Montant de la taxe : {tax} en livres sterlings")
    print("--------")
    print(f"Il reste {availability} exemplaires en stock")
    print("--------")
    print(f"Resume de l'oeuvre : {number_of_review}")
    print("--------")


if __name__ == "__main__":
    main()
