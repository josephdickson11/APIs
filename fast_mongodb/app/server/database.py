#add mongodb connection detail

import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://127.0.0.1:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

students_collection = database.get_collection("student_collection")

#helpers for parsing database query into python dict

def student_helper(student) -> dict:
    return{
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"]
    } 