print("*******************")
print("FUNCTIONS IN PYTHON")
print("*******************")

def display_company_name():
    print("Company Name : Ideas2IT")

print("\nSimple Function")
print("---------------")

display_company_name()


def display_employee(employee_name):
    print(f"Employee Name : {employee_name}")

print("\nFunction With Parameters")
print("------------------------")

display_employee("Ramesh Srinivasan")
display_employee("John Smith")


def employee_details(employee_id, employee_name, salary):
    print(f"Employee ID : {employee_id}")
    print(f"Employee Name : {employee_name}")
    print(f"Salary : {salary:,.2f}")

print("\nFunctions with Multiple Parameters")
print("----------------------------------")

employee_details(
    1001,
    "Ramesh Srinivasan",
    100000.50
)

# ==================================================
# Function Returning Value
# ==================================================

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

print("\nFunction Return Value")
print("---------------------")

annual_salary = calculate_annual_salary(100000)

print(f"Annual Salary : {annual_salary:,.2f}")


def calculate_bonus(monthly_salary):

    bonus = monthly_salary * 0.10
    total_salary = monthly_salary + bonus

    return bonus, total_salary

print("\nFunction Multiple Return Values")
print("-------------------------------")

bonus, total_salary = calculate_bonus(100000)

print(f"Bonus Amount : {bonus:,.2f}")
print(f"Salary After Bonus : {total_salary:,.2f}")


def employee_role(employee_name, role="Developer"):
    print(
        f"Employee : {employee_name} | Role : {role}"
    )

print("\nFunction with Default Parameters")
print("--------------------------------")

employee_role("Ramesh")
employee_role("John", "Architect")


print("\nKeyword Arguments")
print("-----------------")

employee_details(
    employee_name="Ramesh Srinivasan",
    employee_id=1001,
    salary=100000
)

def employee_skills(*skills):

    print("Skills")

    for skill in skills:
        print(f"- {skill}")

print("\nArbitrary Arguments (*args) Example")
print("-----------------------------------")

employee_skills(
    "Python",
    "SQL",
    "FastAPI",
    "Machine Learning"
)


def employee_profile(**details):

    for key, value in details.items():
        print(f"{key} : {value}")

print("\nArbitrary Keyword Arguments (**kwargs) Example")
print("----------------------------------------------")

employee_profile(
    Name="Ramesh Srinivasan",
    Experience=15,
    Salary=100000,
    Department="Engineering"
)


print("\nLambda Function")
print("---------------")

calculate_hike = lambda salary: salary * 1.10

new_salary = calculate_hike(100000)

print(f"Salary After Hike : {new_salary:,.2f}")


def calculate_hra(monthly_salary):
    return monthly_salary * 0.20

def calculate_pf(monthly_salary):
    return monthly_salary * 0.12

def calculate_net_salary(monthly_salary):

    hra = calculate_hra(monthly_salary)
    pf = calculate_pf(monthly_salary)

    return monthly_salary + hra - pf

print("\nFunction Calling Function")
print("-------------------------")

net_salary = calculate_net_salary(100000)

print(f"Net Salary : {net_salary:,.2f}")


# ==================================================
# Employee Evaluation Function
# ==================================================

def evaluate_employee(
        experience,
        rating
):

    if experience >= 10 and rating >= 4.5:
        return "Promotion Eligible"

    elif rating >= 4.0:
        return "Good Performer"

    else:
        return "Needs Improvement"

print("\nEmployee Evaluation")
print("-------------------")

result = evaluate_employee(15, 4.7)

print(f"Evaluation Result : {result}")



# ==================================================
# Main Execution
# ==================================================

print("\nEmployee Summary Report")
print("=======================")

employee_name = "Ramesh Srinivasan"
monthly_salary = 100000

annual_salary = calculate_annual_salary(
    monthly_salary
)

status = evaluate_employee(
    15,
    4.7
)

print(f"Employee Name : {employee_name}")
print(f"Annual Salary : {annual_salary:,.2f}")
print(f"Status        : {status}")