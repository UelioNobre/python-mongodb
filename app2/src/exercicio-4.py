from rich import print
from pymongo import MongoClient

# Retorne as hospedagens que os preços (price)
# são maiores que 155 e menores que 200, mostrando
# apenas o nome (name) e o preço, mantendo em
# ordem decrescente de preço e alfabética de nome
with MongoClient() as client:
    db = client.project

    query = {"price": {"$gt": 155, "$lt": 200}}
    projection = {"name": True, "price": True}
    sort = [("price", 1), ("name", 1)]

    for document in db.listing.find(query, projection, sort=sort):
        print(document)
