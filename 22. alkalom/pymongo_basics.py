"""
pymongo - ez egy driver, amivel a MongoDB-n tudunk műveletek végezni

CRUD műveleteket fogjuk megnézni: create, read, update, delete

###############
Kell egy cliens object -> database object -> collection objectet => a collection objecten fogunk
műveleteket végezni


"""

from pymongo import MongoClient

db_uri = "mongodb://localhost:27017"

client = MongoClient(db_uri)
database = client['pelda']
coll = database['test_col']

my_dict = {
    "Name": "buick skylark 320",
    "Miles_per_Gallon": 15,
    "Cylinders": 8,
    "Displacement": 350,
    "Horsepower": 165,
    "Weight_in_lbs": 3693,
    "Acceleration": 11.5,
    "Year": "1970-01-01",
    "Origin": "USA"
}

#coll.insert_one(my_dict)

