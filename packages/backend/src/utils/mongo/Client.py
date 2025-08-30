import pymongo
import pymongo.collection
import pymongo.database
from utils.helper.config import Yaml
from utils.console import console

class MongoClient:
    
    user = Yaml().get("database.username")
    passw = Yaml().get("database.password")
    authdb = Yaml().get("database.auth_db")
    uri = f"mongodb://{user}:{passw}@database:29345/{authdb}"
    
    client: pymongo.MongoClient = pymongo.MongoClient(uri)
    
    console.info("Mongo Uri:", uri)
    
    database: pymongo.database.Database = client["app"]
    
    # Collections
    clicks: pymongo.collection.Collection = database["clicks"]