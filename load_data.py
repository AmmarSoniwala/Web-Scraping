from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv(r"F:\Trainee_TUVOC\Beautiful_Soup\env\.env")

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["Product_Data"]

collection = db["products"]

with open(r"F:\Trainee_TUVOC\Beautiful_Soup\product.json", "r", encoding="utf-8") as product:
    products = json.load(product)

result = collection.insert_many(products)

if result.acknowledged:
    print("Products Inserted Successfully")
else:
    print("Error Occurred while Inserting the Products")