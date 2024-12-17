import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["django-learn"]

users = db["users"]
announcements = db["announcements"]
posts = db["posts"]



