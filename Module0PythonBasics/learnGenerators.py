print("********************")
print("GENERATORS IN PYTHON")
print("********************")

print("\nNormal Function")
print("---------------")

def employee_ids():

    return [1001, 1002, 1003]

ids = employee_ids()

print(ids)


print("\nGenerator Function")
print("------------------")

def employee_ids():

    yield 1001
    yield 1002
    yield 1003

ids = employee_ids()

print(ids)
print("Because values are not generated yet.")


print("\nUsing next()")
print("------------")

def employee_ids():

    yield 1001
    yield 1002
    yield 1003

ids = employee_ids()

print(next(ids))
print(next(ids))
print(next(ids))


print("\nLoop Through Generator")
print("----------------------")

def employee_ids():

    yield 1001
    yield 1002
    yield 1003
    yield 1004
    yield 1005

for employee_id in employee_ids():

    print(
        f"Employee ID : {employee_id}"
    )



print("\nSalary Generator")
print("----------------")

def salary_generator():

    salaries = [
        50000,
        75000,
        100000,
        125000
    ]

    for salary in salaries:

        yield salary

for salary in salary_generator():

    print(
        f"Salary : {salary:,.2f}"
    )



print("\nInfinite Generator")
print("------------------")

def generate_employee_ids():

    employee_id = 1001

    while True:

        yield employee_id

        employee_id += 1

ids = generate_employee_ids()

print(next(ids))
print(next(ids))
print(next(ids))
print("Generator can theoretically run forever.")



print("\nBonus Generator")
print("---------------")

def bonus_generator():

    salaries = [
        50000,
        75000,
        100000
    ]

    for salary in salaries:

        bonus = salary * 0.10

        yield bonus

for bonus in bonus_generator():

    print(
        f"Bonus : {bonus:,.2f}"
    )




print("\nEmployee Data Processing")
print("------------------------")

def process_employees():

    for employee_id in range(
            1001,
            1011
    ):

        yield {
            "employee_id": employee_id,
            "status": "Processed"
        }

for employee in process_employees():

    print(employee)

