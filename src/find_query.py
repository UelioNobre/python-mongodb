from rich import print
from pymongo import MongoClient
from time import sleep

client = MongoClient()

db = client.catalogue

for book in db.books.find({"title": {"$regex": "t"}}):
    print(book)
    sleep(1)

client.close()
