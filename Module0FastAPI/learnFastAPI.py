from fastapi import FastAPI

# Create FastAPI Application
app = FastAPI()

# Home API
@app.get("/")
def home():

    return {
        "message": "Welcome To FastAPI"
    }

# Employee API
@app.get("/employee")
def get_employee():

    return {
        "employee_id": 1001,
        "employee_name": "Ramesh Srinivasan",
        "designation": "Architect",
        "salary": 100000
    }

