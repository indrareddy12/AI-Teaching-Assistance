import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client[os.getenv("MONGO_DB_NAME", "tutor_rag_db")]

users_collection = db["users"]
chunk_collection = db["chunks"]
chat_history_collection = db["chat_history"]
quizzes_collection = db["quizzes"]
quiz_history = db["quiz_history"]
