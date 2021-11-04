#create student model

from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class TeacherSchema(BaseModel):
    email: EmailStr  = Field(...)
    password: str = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "email": "soganiyu@gmail.com",
                "password": "AbscdXYz123@!"

            }
        }

class UpdateTeacherModel(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]


    class Config:
        schema_extra = {
            "example": {
                "email": "sganiyu@gmail.com",
                "password": "AbscdXYz123@!"
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