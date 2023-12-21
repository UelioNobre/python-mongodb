from rich import print
from pymongo import MongoClient

# Retorne a hospedagem com maior
# número de quartos (bedrooms),
# mostrando apenas o nome (name)
# e a quantidade de quartos.
client = MongoClient()
db = client.project

projection = {"name": True, "bedrooms": True}
sort = ("bedrooms", -1)

document = db.listing.find_one({}, projection, sort=[sort])

print(document)
