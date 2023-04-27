import pymongo

DATABASEADRESS = "mongodb://localhost:27017/"

#Get a dictionary containing the data already formated and add it to the data base
#data is a dictionary
#No return
def addData(data):
    DBClient = pymongo.MongoClient(DATABASEADRESS)
    DB = DBClient["local"]
    Collec = DB["User"]

    filter = {'Username' : data["Username"], 'Network' : data["Network"]}
    Collec.update_one(filter, { "$set" : data}, upsert=True)

#Get two strings containing the username and the network
#username and network are strings
#return a dictionary or None if nothing found
def getData(username, network):
    DBClient = pymongo.MongoClient(DATABASEADRESS)
    DB = DBClient["local"]
    Collec = DB["User"]

    return Collec.find_one({"Username" : username, "Network" : network})
