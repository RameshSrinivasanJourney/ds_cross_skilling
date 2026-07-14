from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

class Address(BaseModel):

    city: str
    state: str
    pincode: str

class EmployeeRequest(BaseModel):

    employee_id: int
    employee_name: str = Field(
        min_length=3,
        max_length=50
    )
    designation: str
    salary: float = Field(
        gt=0
    )
    mobile_number: Optional[str] = None
    skills: List[str]
    address: Address


@app.post("/employees")
def create_employee(
        employee: EmployeeRequest
):

    return {
        "message": "Employee Created Successfully",
        "employee": employee
    }

'''
Input
{
  "employee_id": 1001,
  "employee_name": "Ramesh Srinivasan",
  "designation": "Associate Architect",
  "salary": 100000,
  "mobile_number": "9876543210"
  "skills": [
    ".NET",
    "Azure",
    "SQL Server",
    "FastAPI"
  ]
  "address": {
    "city": "Bangalore",
    "state": "Karnataka",
    "pincode": "560067"
  }
}
'''