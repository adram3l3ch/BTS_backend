import pymongo
url = "mongodb+srv://rahuljames669:rahul%401999@pythonprojects.fwqjmcz.mongodb.net/?retryWrites=true&w=majority&appName=PythonProjects"
client = pymongo.MongoClient(url)
db = client["BTS"]

# @ = %40

# {
#     "BTS" :{
            # "Booking"
            #"Vehicle"
#     }
# }