#create student model

from typing import Optional
from pydantic import Basemodel, Emailstr, Field


class StudentSchema(Basemodel):
    fullname: str = Field(...)
    email: Emailstr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=6)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Oladipupo Ibeun",
                "email": "oladipupo@gmail.com",
                "course_of_study": "Information Technology",
                "year": 4,
                "gpa": "4.0",
            }
        }

class UpdateStudentModel(Basemodel):
    fullname: Optional[str]
    email: Optional[Emailstr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Oladipupo Joseph Ibeun",
                "email": "oladipupo@gmail.com",
                "course_of_study": "Info tech",
                "year": 3,
                "gpa": "4.0"
            }
        }

def ResponseModel(data, message):
    return{
        "data":[data],
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return{
        "error": error,
        "code": code,
        "mesage": message
    }

