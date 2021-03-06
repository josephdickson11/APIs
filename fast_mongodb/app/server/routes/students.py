from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student
)

from app.server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel
)


router = APIRouter()

#add route for adding students
@router.post("/", response_description= "student data added to the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully")

#add route for retrieveing students
@router.get("/", response_description= "Students retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Students data retrieved successfully")
    return  ErrorResponseModel("Empty list returned.")

#add route for retrieveing student
@router.get("/{id}", response_description="Student data retrieved")
async def get_student_data(id):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Student data retrieved successsfully")
    ErrorResponseModel("An error occured", 404, "student doesn't exist.")

#add route for updating students
@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if update_student:
        return ResponseModel(
            "Student with ID: {} name update is successful".format(id),
            "Student name updated successfully"
        )
    return ErrorResponseModel(
        "An error occured",
        404,
        "There was an error updating the student data."
    )


#add route to delete student
@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if delete_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )