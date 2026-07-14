print("*******************************")
print("CONTROL STATEMENTS - WHILE LOOP")
print("*******************************")

print("\nBasic While Loop")
print("----------------")

counter = 1

while counter <= 5:
    print(f"Iteration : {counter}")
    counter += 1

print("\nEmployee ID Generation")
print("----------------------")

employee_id = 1001

while employee_id <= 1005:
    print(f"Employee ID : {employee_id}")
    employee_id += 1

print("\nSalary Growth Simulation")
print("------------------------")

salary = 50000
year = 1

while year <= 5:

    salary = salary * 1.10

    print(
        f"Year {year} Salary : {salary:,.2f}"
    )

    year += 1


print("\nEmployee Experience Tracker")
print("---------------------------")

experience = 1

while experience <= 10:

    print(
        f"Experience : {experience} Years"
    )

    experience += 1

# ==================================================
# While With IF ELSE
# ==================================================

print("\nWhile With IF ELSE - Promotion Eligibility")
print("------------------------------------------")

experience = 5

while experience <= 15:

    if experience >= 10:
        print(
            f"{experience} Years -> Eligible"
        )
    else:
        print(
            f"{experience} Years -> Not Eligible"
        )

    experience += 1

# ==================================================
# Break Statement
# ==================================================

print("\nBreak Example")
print("-------------")

employee_id = 1001

while True:

    print(f"Checking Employee : {employee_id}")

    if employee_id == 1005:
        print("Employee Found")
        break

    employee_id += 1

# ==================================================
# Continue Statement
# ==================================================

print("\nContinue Example")
print("----------------")

employee_id = 1001

while employee_id <= 1005:

    employee_id += 1

    if employee_id == 1003:
        continue

    print(f"Employee ID : {employee_id}")

# ==================================================
# User Input Validation
# ==================================================

print("\nUser Input Validation - Employee Rating Validation")
print("--------------------------------------------------")

rating = 0

while rating < 1 or rating > 5:

    rating = int(
        input("Enter Employee Rating (1-5): ")
    )

    if rating < 1 or rating > 5:
        print("Invalid Rating. Try Again.")

print(f"Valid Rating Entered : {rating}")


print("\nPassword Validation")
print("-------------------")

password = ""

while password != "admin123":

    password = input(
        "Enter Password : "
    )

    if password != "admin123":
        print("Incorrect Password")

print("Login Successful")


print("\nEmployee Evaluation Report")
print("==========================")

employee_count = 1

while employee_count <= 5:

    print(
        f"Employee {employee_count} Processed Successfully"
    )

    employee_count += 1