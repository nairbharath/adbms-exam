import pymongo
url="mongodb://localhost:27017/"
c=pymongo.MongoClient(url)
db=c["exam"]
coll=db["student"]
#Insert One data
"""
entry1={"_id":1,"Name":"Anjali","Place":"Kollam","Phone":8582639562,
"Vaccination_status":"Both vaccinated","RTPCR":"negative",
"Lab_mark":{"Internal":30,"External":45},
"Department":"MCA"}

coll.insert_one(entry1)

"""

#INsert many data
"""
entry2=[{"_id":2,"Name":"Anuradha","Place":"Varkala","Phone":99926639562,
"Vaccination_status":"Both vaccinated","RTPCR":"negative",
"Lab_mark":{"Internal":40,"External":48},
"Department":"Civil"},
{"_id":3,"Name":"Bismiya","Place":"Kollam","Phone":9446639562,
"Vaccination_status":"not vaccinated","RTPCR":"positive",
"Lab_mark":{"Internal":50,"External":39},
"Department":"MCA"},
{"_id":4,"Name":"Vimal","Place":"Ernakulam","Phone":8582639568,
"Vaccination_status":"First dose only","RTPCR":"positive",
"Lab_mark":{"Internal":40,"External":42},
"Department":"Civil"},
{"_id":5,"Name":"Vivek","Place":"Kollam","Phone":8582639777,
"Vaccination_status":"Both vaccinated","RTPCR":"negative",
"Lab_mark":{"Internal":50,"External":50},
"Department":"MCA"}]

coll.insert_many(entry2)

"""
#Nosql to sipaly name and Phone of not vaccinated students
"""
for x in coll.find({"Vaccination_status":"not vaccinated"},{"Name":1,"Phone":1}):
	print(x["Name"]+"\t"+str(x["Phone"]))
"""
#Display name and phone number of top 2 students in MCA dept(based on external marks)
"""
for x in coll.find({"Department":"MCA"},{"Name":1,"Phone":1,"Lab_mark.External":1}).sort("Lab_mark.External",-1).limit(2):
	print(x["Name"]+"\t"+str(x["Phone"])+"\t"+str(x["Lab_mark"]["External"]))
"""
#Display id,name and dept of students whose name starts with 'A'
"""
for x in coll.find({"Name":{"$regex":"^[aA]"}},{"_id":1,"Name":1,"Department":1}):
	print(str(x["_id"])+" "+x["Name"]+" "+x["Department"])
"""

#Update vaccination status as 'both vaccinated' of student whose id=4

myq={"_id":4}
upd={"$set":{"Vaccination_status":"both Vaccinated"}}
coll.update_one(myq,upd)


#name of 

for x in coll.find().sort("Lab_mark.External",-1): 
	print(x["Name"])





