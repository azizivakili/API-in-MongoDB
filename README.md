# API-in-MongoDB
### Simple API for MongoDB based database for beginners with easy instructions

### To Run:

* Run docker-compose.yml file to have docker images running
* Database should be created and imported via "AirlineDB.json"
```
mongoimport -d sample -c AirlineDB --authenticationDatabase admin --username admin --password pass --jsonArray --file data/db/AirlineDB.json
```
