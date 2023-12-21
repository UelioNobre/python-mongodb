from rich import print
from pymongo import MongoClient

client = MongoClient()

# Retorne a quantidade de documentos inseridos na coleção
db = client.project
total_documents = db.listing.count_documents({})

client.close()
print(f"Total de documentos: {total_documents}")
