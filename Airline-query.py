print("Name: Latifa")
print("Lastname: AziziVakili")
print(".........................\n")

print("Aireline-Queries")
print("===============================")

#a: Authentication ---
import re
from pymongo import MongoClient
from pprint import pprint

client = MongoClient(
    host="127.0.0.1",
    port = 27017,
    username="admin",
    password="pass",
    authSource="admin"
)



#B): List of database names ---
# Access the database and collection
database_name = "AirlineDB"
database = client[database_name]
collection = database["AirlinesDelay"]


#C: List of collections ---
print("List of Collections: ", )
print("Collection name: ",collection)



#=== Print headers
headers = ["Aircraft", "FlightType", "Origin", "Destination", "Departure_Date", "Departure_Time", "Arrival_Date", "Arrival_Time", "EA_Time_Minutes", "RA_Time_Minutes", "Delay_Time"]
print("Headers:")
print("\t".join(headers))



#=== Print data in JSON format: 

print("AirlinesDelay table in JSON format: ")
collection = database["AirlinesDelay"]
cursor = collection.find({})
for document in cursor:
	pprint(document)


#=== Print data in CSV format: 

#print("AirlinesDelay table in CVS format: ")
#cursor = collection.find({})
#for document in cursor:
#    data = [document[header] for header in headers]
#    pprint("\t".join(str(value) for value in data))


#=== Print only the "Aircraft" column

#print("Aircraft Column:")
#cursor = collection.find({}, {"Aircraft": 1, "_id": 0})  # Only retrieve the "Aircraft" field, exclude the "_id"
#for document in cursor:
#    print(document["Aircraft"])


#=== Print rows with destination of "El Dorado Int'l (BOG / SKBO)"

#query = {"Destination": "El Dorado Int'l (BOG / SKBO)"}
# Find documents matching the query
#cursor = collection.find(query)
#print("Rows with destination 'El Dorado Int'l (BOG / SKBO)':")
#for document in cursor: 	
#    print(document)



#==== Print count of destination defined in above query:

#count = collection.count_documents(query)
#print("Number of Flights to this Destination: ", count)

