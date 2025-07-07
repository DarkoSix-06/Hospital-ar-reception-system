from pymongo import MongoClient
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["hospital"]
users = db["patients"]
patients = db["patients"]

def insert_user(data):
    users.insert_one(data)

def get_all_users():
    all_users = users.find()
    return [{
        "name": u["name"],
        "patientID": u["patientID"],
        "reason": u["reason"],
        "illness": u["illness"],
        "face_encoding": np.array(u["face_encoding"], dtype='float64')
    } for u in all_users]

def find_user_by_name_or_id(name=None, patientID=None):
    query = {}
    if name:
        query["name"] = name
    if patientID:
        query["patientID"] = patientID
    return patients.find_one(query)