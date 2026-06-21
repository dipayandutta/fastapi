from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()



@app.get("/")
def read_root():
    return {"Message": "Hello World"}

@app.get("/greet")
def greet():
    return {"Message": "Greetings from FastAPI!"}

#Path Parameter
@app.get("/greet/{name}")
def greet_name(name: str):
    return {"Message": f"Hello {name}"}

#Query Parameter
@app.get("/age")
def get_age(age: int):
    return {"Age": age}

#http://127.0.0.1:8000/age?age=10


# in case of need to one parameter as optional
@app.get("/name/{name}")
def user_name(name: str, age: Optional[int] = None):
    return {"Name": f"Hello {name} you are {age} years old!"}



class Student(BaseModel):
    name: str
    age: int
    email: str
    address: str

@app.post("/create_student")
def create_student(student: Student):
   return {
    "name": student.name,
    "age": student.age,
    "email": student.email,
    "address": student.address
   }