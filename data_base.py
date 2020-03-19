import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:5000/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]
