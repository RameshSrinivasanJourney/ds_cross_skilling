from fastapi import FastAPI

app = FastAPI()

employees = [
    {
        "employee_id": 1001,
        "employee_name": "Ramesh Srinivasan",
        "designation": "Architect",
        "salary": 100000
    },
    {
        "employee_id": 1002,
        "employee_name": "John",
        "designation": "Technical Lead",
        "salary": 90000
    },
    {
        "employee_id": 1003,
        "employee_name": "David",
        "designation": "Senior Developer",
        "salary": 80000
    }
]

@app.get("/")
def home():

    return {
        "message": "Employee API"
    }


@app.get("/employees")
def get_employees():

    return employees


@app.get("/employees/count")
def get_employee_count():

    return {
        "total_employees": len(employees)
    }


@app.get("/employees/statistics")
def get_salary_statistics():

    salaries = [
        employee["salary"]
        for employee in employees
    ]

    return {
        "maximum_salary": max(salaries),
        "minimum_salary": min(salaries),
        "average_salary": sum(salaries) / len(salaries)
    }


@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):

    for employee in employees:

        if employee["employee_id"] == employee_id:

            return employee

    return {
        "message": "Employee Not Found"
    }