from flask import redirect, url_for, request
from app import db
import json

@app.route("/")
def index():
    return "Hello world"

@app.route('/addname/<name>/')
def addname(name):
    db.users_collection.insert_one({"name": name.lower()})
    return redirect(url_for('getnames'))

@app.route('/getnames/')
def getnames():
    names_json = []
    if db.users_collection.find({}):
        for name in db.users_collection.find({}).sort("name"):
            names_json.append({"name": name['name'], "id": str(name['_id'])})
    return json.dumps(names_json)

#test to insert data to the data base
@app.route("/test")
def test():
    db.products_collection.insert_one({"name": "John"})
    return "Connected to the data base!"

# the real deal
@app.route('/getproducts/', methods=['GET'])
def getproducts():
    products_json = []
    if db.products_collection.find({}):
        for product in db.products_collection.find({}).sort("name"):
            products_json.append({"id": str(product['_id']), "name": product['name']})
    return json.dumps(products_json)

@app.route('/addproduct/', methods=['POST'])
def addproduct():
    product = {
        'name': request.json['name'],
        'desc': request.json['desc']
    }
    db.products_collection.insert_one(product)
    return redirect(url_for('getproducts'))





