from rich import print
from pymongo import MongoClient

# Retorne o identificador do host (host.host_id),
# nome (host.host_name) e
# localização (host.host_location) de todos os
# superhost (host.host_is_superhost)
with MongoClient() as client:
    db = client.project

    query = {"host.host_is_superhost": {"$eq": True}}
    projection = {
        "host.host_id": True,
        "host.host_name": True,
        "host.host_location": True,
    }

    for document in db.listing.find(query, projection):
        print(document)
