from rich import print
from pymongo import MongoClient

client = MongoClient()

db = client.catalogue

# Busca um documento, sem filtros
a_book = db.books.find_one()

print(f"{a_book}")
print(f"__id: {a_book['_id']}")
print(f"title: {a_book['title']}")

client.close()
