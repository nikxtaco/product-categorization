from flask import Flask
import pymongo

CONNECTION_STRING = "mongodb+srv://nikxtaco:qwerty25@cluster0.uaylh.mongodb.net/monthly-tracks?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('monthly-tracks')
expense_budget_collection = pymongo.collection.Collection(db, 'expense-budget')
# users_collection = pymongo.collection.Collection(db, 'users')
# orders_collection = pymongo.collection.Collection(db, 'orders')