import requests
import time

url = "https://eazypc.in/product-category/refurbished-laptops-under-30k/?wpf_min_price=23499&wpf_max_price=34000&wpf_fbv=1"
url1 = "https://eazypc.in/product-category/corporate-laptops-eazypc-delhi-ncr/page/3/"

session = requests.Session()


# for no in range(1,8):
#     r = session.get(f"https://eazypc.in/product-category/corporate-laptops-eazypc-delhi-ncr/page/{no}/")
    
#     with open(rf"F:\Trainee_TUVOC\Beautiful_Soup\{no}.html", "w", encoding="utf-8") as f:
#         f.write(r.text)

r = session.get("https://eazypc.in/product-category/corporate-laptops-eazypc-delhi-ncr/page/3/")

with open(r"F:/Trainee_TUVOC/Beautiful_Soup/3.html", "w", encoding="utf-8") as f:
    f.write(r.text)

r = session.get("https://eazypc.in/product-category/corporate-laptops-eazypc-delhi-ncr/page/6/")

with open(r"F:/Trainee_TUVOC/Beautiful_Soup/6.html", "w", encoding="utf-8") as f:
    f.write(r.text)