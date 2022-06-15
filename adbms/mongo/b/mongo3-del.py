import pymongo

url="mongodb://localhost:27017"
c=pymongo.MongoClient(url)
db=c['sample']
coll=db['student']

coll.delete_one({"mark":90})
