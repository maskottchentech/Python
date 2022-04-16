import pymongo

#connect to MongoDb
client = pymongo.MongoClient()

#create a db
tdb= client["test_database"]

#create a collection
tcoll = tdb["persons"]

#create document
tdict= {"name": "Karan", "age":31}

#add the document
x= tcoll.insert_one(tdict)

tdict1= [{"name":"Hugo", "age":12, "country":"India"}, {"name":"Shubh", "age":27}]
x= tcoll.insert_many(tdict1)