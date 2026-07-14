from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Employee(BaseModel):

    employee_id: int
    employee_name: str = Field(
        min_length=3,
        max_length=50
    )
    designation: str
    salary: float = Field(
        gt=0
    )


employees = []


@app.get("/")
def home():

    return {
        "message": "Employee Management API"
    }


@app.post("/employees")
def create_employee(employee: Employee):

    employees.append(employee)

    return {
        "message": "Employee Created Successfully",
        "employee": employee
    }


@app.get("/employees")
def get_employees():

    return employees