from pymongo import MongoClient
import pymongo

# MongoDB Connection
client = MongoClient("mongodb+srv://thanishmamilla:thanish123@cluster0.1x0tmmk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["chatDB"]
chats_collection = db["chats"]

# Create Indexes for Optimized Queries
chats_collection.create_index([("conversation_id", pymongo.ASCENDING)])
chats_collection.create_index([("user_id", pymongo.ASCENDING)])
chats_collection.create_index([("timestamp", pymongo.DESCENDING)])
