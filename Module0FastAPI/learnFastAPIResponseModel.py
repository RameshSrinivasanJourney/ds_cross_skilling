from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class EmployeeRequest(BaseModel):

    employee_id: int
    employee_name: str
    designation: str
    salary: float

    password: str
    pan_number: str


class EmployeeResponse(BaseModel):

    employee_id: int
    employee_name: str
    designation: str
    salary: float


employees = []


@app.post(
    "/employees",
    response_model=EmployeeResponse
)
def create_employee(
        employee: EmployeeRequest
):

    employees.append(employee.model_dump())

    return employee


@app.get(
    "/employees",
    response_model=List[EmployeeResponse]
)
def get_employees():

    return employees


@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee_by_id(
        employee_id: int
):

    for employee in employees:

        if employee["employee_id"] == employee_id:

            return employee

    return {
        "message": "Employee Not Found"
    }