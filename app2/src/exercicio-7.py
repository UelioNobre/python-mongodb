from rich import print
from pymongo import MongoClient


# Retorne o nome da acomodação (name), o resumo da
# acomodação (summary), seu preço (price) e todos as
# notas de reviews (review_score) dos superhosts
# (host.host_is_superhost) com número de reviews
# (number_of_reviews) superior a 500
with MongoClient() as client:
    db = client.project

    query = {
        "$and": [
            {"host.host_is_superhost": True},
            {"number_of_reviews": {"$gte": 500}},
        ]
    }
    projection = {
        "name": True,
        "summary": True,
        "price": True,
        "number_of_reviews": True,
    }

    for document in db.listing.find(query, projection):
        print(document)
