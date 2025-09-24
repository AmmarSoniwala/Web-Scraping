import sys
sys.stdout.reconfigure(encoding="utf-8")

from bs4 import BeautifulSoup
import re
import time

# for i in range(1,8):
#     with open(rf"F:\Trainee_TUVOC\Beautiful_Soup\{i}.html", "r", encoding="utf-8") as f:
#         html_content = f.read()
        
#     soup = BeautifulSoup(html_content, 'html.parser')
    
#     product_detail = soup.find_all("div", "product-element-bottom")
#     print(len(product_detail))
    
#     with open(r"F:\Trainee_TUVOC\Beautiful_Soup\product.html", "a", encoding="utf-8") as f:
#         for prod in product_detail:
#             f.write("\n" + str(prod))

# for i in range(1,8):
#     with open(rf"F:\Trainee_TUVOC\Beautiful_Soup\c{i}.html", "r", encoding="utf-8") as f:
#         time.sleep(2)
#         html_content = f.read()
        
#     soup = BeautifulSoup(html_content, 'html.parser')
    
#     product_detail = soup.find_all("div", "product-element-bottom")
#     print(len(product_detail))
    
#     with open(r"F:\Trainee_TUVOC\Beautiful_Soup\product.html", "a", encoding="utf-8") as f:
#         for prod in product_detail:
#             f.write("\n" + str(prod))


# with open(r"F:\Trainee_TUVOC\Beautiful_Soup\s1.html", "r", encoding="utf-8") as f:
#     time.sleep(2)
#     html_content = f.read()
        
# soup = BeautifulSoup(html_content, 'html.parser')
    
# product_detail = soup.find_all("div", "product-element-bottom")
# print(len(product_detail))
    
# with open(r"F:\Trainee_TUVOC\Beautiful_Soup\product.html", "a", encoding="utf-8") as f:
#     for prod in product_detail:
#         f.write("\n" + str(prod))

for i in range(1,3):
    with open(rf"F:\Trainee_TUVOC\Beautiful_Soup\g{i}.html", "r", encoding="utf-8") as f:
        time.sleep(2)
        html_content = f.read()
        
    soup = BeautifulSoup(html_content, 'html.parser')
    
    product_detail = soup.find_all("div", "product-element-bottom")
    print(len(product_detail))
    
    with open(r"F:\Trainee_TUVOC\Beautiful_Soup\product.html", "a", encoding="utf-8") as f:
        for prod in product_detail:
            f.write("\n" + str(prod))