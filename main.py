# from fastapi import FastAPI

# app = FastAPI()

# students = ['Adewale','Sergiu']

# @app.get("/")
# async def root():
#     return {"message": "hello world"}

# @app.post('./students/post/student')
# async def addStudents(student: str):
#     return {
#         students.append(student)
#     }

# @app.get('./students')
# async def getStudents():
#     return [students]

# @app.get('./students/get/name')
# async def individualStudents(name: str):
#     return {f'{name} is a student of our school'}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {f'The item id is: {item_id}'}

from fastapi import FastAPI, HTTPException

app = FastAPI()

# Create an empty list to store student information
students = []

# Define a data model for students using Pydantic
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    location: str
    university: str

# POST endpoint to add a new student
@app.post("/student")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully"}

# GET endpoint to retrieve the list of students
@app.get("/students")
def get_students():
    return students

# GET endpoint to retrieve information about a student by name
@app.get("/student")
def get_student(name: str):
    for student in students:
        if student.name == name:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
