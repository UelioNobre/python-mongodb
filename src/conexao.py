from pymongo import MongoClient

client = MongoClient()
db = client.catalogue
students = db.books
client.close()
