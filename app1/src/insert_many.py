from pymongo import MongoClient

client = MongoClient()

db = client.catalogue

books = [
    {"title": "A Light in the Attic"},
    {"title": "Tipping the Velvet"},
    {"title": "Soumission"},
]

result = db.books.insert_many(books)

print(result)

client.close()
