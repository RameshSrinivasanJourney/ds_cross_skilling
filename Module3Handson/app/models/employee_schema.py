from pydantic import BaseModel


class EmployeeSchema(BaseModel):

    name: str

    department: str

    salary: int

    location: str