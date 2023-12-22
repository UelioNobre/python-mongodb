from rich import print
from pymongo import MongoClient

# Retorne o nome (name), a descrição (description), o número de reviews
# (number_of_reviews), as facilidades (amenities) e o preço (price) das
# acomodações que aceitam pets (amenities deve conter “Pets allowed”)
# ordenado pelo maior número de reviews, menor preço e em ordem alfabética
with MongoClient() as client:
    db = client.project

    query = {
        "amenities": {
            "$all": ["Pets allowed"],
        }
    }
    projection = {
        "name": 1,
        "description": 1,
        "number_of_reviews": 1,
        "price": 1,
        "amenities": 1,
    }
    sort = [
        ("number_of_reviews", -1),
        ("price", 1),
        ("name", 1),
    ]

    for document in db.listing.find(query, projection, sort=sort):
        print(document)
