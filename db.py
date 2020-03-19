from flask import Flask
from flask_pymongo import pymongo
from app import app
CONNECTION_STRING="mongodb+srv://MongoUser:mgbkelf1022@marcelotestemileage-cg9tw.gcp.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('teste1')
user_collection = pymongo.collection.Collection(db, 'testee')