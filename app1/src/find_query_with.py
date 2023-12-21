from time import sleep
from rich import print
from pymongo import MongoClient

# Usando gerenciador de contexto with
with MongoClient() as client:
    db = client.catalogue

    for book in db.books.find({}):
        print(book)
        sleep(0.5)
