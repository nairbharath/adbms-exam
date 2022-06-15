import pymongo

url="mongodb://localhost:27017"
c=pymongo.MongoClient(url)
db=c['sample']
coll=db['student']


myquery=({"mark":80})
_update=({"$set":{"mark":90}})

coll.update_many(myquery,_update)
