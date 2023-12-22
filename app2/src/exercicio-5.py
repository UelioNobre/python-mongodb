from rich import print
from pymongo import MongoClient


# Retorne o nome, número de reviews (number_of_reviews) e as
# notas dos TODOS os reviews dos 500 primeiros valores que
# tiverem número de reviews maior que 300 ou nota dos reviews
# (review_scores.review_scores_rating) maior ou igual a 95
# ordenado por maior quantidade de reviews, maior nota de
# reviews e ordem alfabética
with MongoClient() as client:
    db = client.project

    query = {
        "$or": [
            {"number_of_reviews": {"$gt": 300}},
            {"review_scores.review_scores_rating": {"$gte": 95}},
        ]
    }

    projection = {
        "name": True,
        "number_of_reviews": True,
        "review_scores.review_scores_rating": True,
    }

    sort = [
        ("number_of_reviews", -1),
        ("review_scores.review_scores_rating", -1),
        ("name", 1),
    ]

    for document in db.listing.find(query, projection, sort=sort).limit(500):
        print(document)
