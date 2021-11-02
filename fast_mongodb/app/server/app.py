#create base route

from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return{"message: welcome to the app demo of fastapi with mongodb"}
