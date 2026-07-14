from fastapi import FastAPI, HTTPException

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
    }
]


@app.get("/")
def home():

    return {
        "message": "Exception Handling Demo"
    }

@app.post("/employees")
def create_employee(employee: dict):

    for existing_employee in employees:

        if existing_employee["employee_id"] == employee["employee_id"]:

            raise HTTPException(
                status_code=409,
                detail="Employee Already Exists"
            )

    employees.append(employee)

    return {
        "message": "Employee Created Successfully"
    }


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:

        if employee["employee_id"] == employee_id:

            return employee

    raise HTTPException(
        status_code=404,
        detail=f"Employee Id {employee_id} Not Found"
    )


@app.get("/bonus")
def calculate_bonus(
        salary: float,
        percentage: float
):

    if percentage < 0:

        raise HTTPException(
            status_code=400,
            detail="Percentage Cannot Be Negative"
        )

    return {
        "bonus": salary * percentage / 100
    }


@app.get("/division")
def division(
        a: int,
        b: int
):

    try:

        return {
            "result": a / b
        }

    except ZeroDivisionError:

        raise HTTPException(
            status_code=400,
            detail="Division By Zero Is Not Allowed"
        )