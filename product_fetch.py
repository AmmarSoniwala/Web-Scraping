import sys
sys.stdout.reconfigure(encoding="utf-8")

from bs4 import BeautifulSoup
import re
import json

with open(r"F:\Trainee_TUVOC\Beautiful_Soup\product.html", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

product_detail = {}
product_list = []

products = soup.find_all("div", "product-element-bottom")
print(len(products))

product_details = []
counter = 0

for i in range(0,189):
    if i == 62 or i == 143:
        continue
    else:
        product_details.append(products[i])
        counter = counter+1

for product in product_details:
    prod = product.select_one("h3 a")
    prod_name = prod.get_text()
    # print(prod_name)

    price = product.select_one("span span", class_="woocommerce-Price-amount amount")
    currency = price.select_one("span bdi span", class_="woocommerce-Price-currencySymbol").decompose()
    price_tag = price.get_text()
    # print(price_tag)
    
    stock = product.select_one("p", class_="wd-product-stock stock wd-style-default")
    stock_detail = ""
    if stock:
        stock_detail = stock.get_text()
    else:
        stock_detail = "Out of Stock"
    # print(stock_detail)
    product_detail={
        "name": prod_name,
        "price": price_tag,
        "availability": stock_detail
    }

    # print(product_detail)

    product_list.append(product_detail)
    
# print(product_list)

with open(r"F:\Trainee_TUVOC\Beautiful_Soup\product.json", "w") as output:
    json.dump(product_list, output, indent = 2)