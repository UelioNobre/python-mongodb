from rich import print
from pymongo import MongoClient

# Retorne o nome (name), a descrição (description), os nomes e os
# comentários dos reviews apenas (reviews.reviewer_name e
# reviews.comments) e o preço (price) de todas as acomodações que
# tem um review do Filipe (isto é reviews.reviewer_id igual a “20775242”)
with MongoClient() as client:
    db = client.project

    query = {
        "reviews": {"$elemMatch": {"reviewer_id": "20775242"}},
    }
    projection = {
        "name": 1,
        "description": 1,
        "price": 1,
        "reviews.reviewer_name": 1,
        "reviews.comments": 1,
    }

    for document in db.listing.find(query, projection):
        print(document)
