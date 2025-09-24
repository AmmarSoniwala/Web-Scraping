import requests
import time

url1 = "https://eazypc.in/product-category/coding-programming-laptops-delhi-ncr/page/1/"

session = requests.Session()


# for no in range(1,8):
#     time.sleep(2)
#     r = session.get(f"https://eazypc.in/product-category/coding-programming-laptops-delhi-ncr/page/{no}/")
    
#     with open(rf"F:\Trainee_TUVOC\Beautiful_Soup\c{no}.html", "w", encoding="utf-8") as f:
#         f.write(r.text)


# r = session.get("https://eazypc.in/product-category/student-laptops-eazypc-second-hand-laptop-store-in-delhi-ncr/")
    
# with open(r"F:\Trainee_TUVOC\Beautiful_Soup\s1.html", "w", encoding="utf-8") as f:
#     f.write(r.text)

for no in range(1,3):
    time.sleep(2)
    r = session.get(f"https://eazypc.in/product-category/gaming-laptops/page/{no}/")
    
    with open(rf"F:\Trainee_TUVOC\Beautiful_Soup\g{no}.html", "w", encoding="utf-8") as f:
        f.write(r.text)