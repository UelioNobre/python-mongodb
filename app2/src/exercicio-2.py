from rich import print
from pymongo import MongoClient

# Ordena a coleção listing pela quantidade
# de quartos (bedrooms) em ordem crescente,
# mostrando apenas o nome (name) e a quantidade de quartos
with MongoClient() as client:
    db = client.project

    projection = {"name": True, "bedrooms": True}
    sort = {"bedrooms": 1}

    for document in db.listing.find({}, projection).sort(sort):
        if "bedrooms" in document:
            print(f"Name: {document['name']}")
            print(f"Bedrooms: {document['bedrooms']}")
