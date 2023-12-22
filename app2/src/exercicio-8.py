from rich import print
from pymongo import MongoClient

with MongoClient() as client:
    db = client.project

    # db.listing.find({ amenities: { $in: ["Pets allowed"] } }, { name: 1, number_of_reviews: 1, price: 1, amenities: 1, _id: 0 }).sort({ number_of_reviews: -1, price: 1, name: 1 })

    query = {"amenities": {"$in": ["Pets allowed"]}}
    projection = {}
    sort = []

    for document in db.listing.find(query, projection).limit(1):
        print(document)

print("Fim")
