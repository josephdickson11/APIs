#add mongodb connection detail

import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://127.0.0.1:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection("student_collection")

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

#define CRUD operations for database

#CRUD 1: retrieve all students
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students



#CRUD 2: add new students to the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student.find_one({"_id":ObjectId(id)})
    return student_helper(new_student)


#crud 3: retrieve student with matching id
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id":ObjectId(id)})
    if student:
        return student_helper(student)

#CRUD 4: update student with a matching id
async def update_student(id: str, data: dict):
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id":ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False

#CRUD 4: delete student from database
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True

