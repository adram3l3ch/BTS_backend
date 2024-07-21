import pymongo
import os

url = os.getenv("MONGO_URI")
client = pymongo.MongoClient(url)
db = client["BTS"]

# @ = %40

# {
#     "BTS" :{
            # "Booking"
            #"Vehicle"
#     }
# }