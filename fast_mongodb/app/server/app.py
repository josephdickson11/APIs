#create base route

from fastapi import FastAPI

from app.server.routes.students import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")

@app.get("/", tags=["Root"])
async def read_root():
    return{"message: welcome to the app demo of fastapi with mongodb"}
