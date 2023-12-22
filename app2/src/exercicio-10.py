from rich import print
from pymongo import MongoClient

with MongoClient() as client:
    db = client.project
    regex = r"/^https:\/\/(a0\.muscache\.com)([\\/\-a-z0-9]*)(.jpg)/"
    query = {
        "$and": [
            {"images": {"$exists": True}},
            {"images.picture_url": {"$not": {"$regex": regex}}},
        ]
    }

    projection = {
        "_id": 1,
        "images": 1,
    }

    for document in db.listing.find(query, projection):
        print(document)
