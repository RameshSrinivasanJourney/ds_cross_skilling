print("*****************************")
print("CONTROL STATEMENTS - FOR LOOP")
print("*****************************")

employees = [
    "Ramesh Srinivasan",
    "John Smith",
    "David Kumar",
    "Rajesh Kumar",
    "Vijay Kumar"
]

print("\nSimple Loop - Employee Names")
print("----------------------------")

for employee in employees:
    print(employee)

print("\nenumerate() Employee Numbering List With Index")
print("----------------------------------------------")
for index, employee in enumerate(employees):
    print(f"{index} - {employee}")

print("\nRange Employee IDs")
print("------------------")

for employee_id in range(1001, 1006):
    print(employee_id)

print("\nLoop + Calculations - Salary Increment Report")
print("---------------------------------------------")

salaries = [50000, 75000, 100000, 125000]

for salary in salaries:
    salary_increment = salary * 10 / 100
    new_salary = salary_increment + salary
    print(f"Current Salary : {salary:,.2f} - Hike : {salary_increment:,.2f} - New Salary : {new_salary:,.2f}")

print("\nLoop + If Else - Promotion Eligibility")
print("--------------------------------------")

experience_years = [5, 8, 10, 12, 15]

for experience in experience_years:
    if experience > 10 :
        print(f"{experience} -  Years Experience -> Eligible")
    else:
        print(f"{experience} -  Years Experience -> Not Eligible")

print("\nDictionary Loop - Employee Details")
print("----------------------------------")

employee = {
    "Id": 1001,
    "Name": "Ramesh Srinivasan",
    "Description": "Associate Architect",
    "Salary" : 100000
}

for key, value in employee.items():
    print(f"{key} - {value}")

print("\nNested Loop - Employee Skills")
print("----------------------------------")

employee_skills = {
    "Ramesh": ["Python", "SQL", "FastAPI"],
    "John": ["Java", "Spring Boot"],
    "David": ["Azure", "Docker"]
}

for employee_name,skills in employee_skills.items():
    print(f"\n Employee : {employee_name}")
    for skill in skills:
        print(f"Skill : {skill}")


print("\nBreak - Stop Loop Example")
print("-------------------------")

for employee_id in range(1001, 1010):

    if employee_id == 1005:
        print(f"Employee : {employee_id} Stop Loop")
        break

    print(employee_id)

print("\nContinue - Skip Record Example")
print("------------------------------")

for employee_id in range(1001, 1006):

    if employee_id == 1003:
        print(f"Employee : {employee_id} Skip Record")
        continue

    print(employee_id)

print("\nLoop +If + ElseIf + Else Employee Evaluation Report")
print("---------------------------------------------------")

employee_ratings = {
    "Ramesh": 4.8,
    "John": 4.1,
    "David": 3.5,
    "Rajesh": 4.6
}

for employee_name, rating in employee_ratings.items():

    if rating >= 4.5:
        status = "Excellent"

    elif rating >= 4.0:
        status = "Good"

    else:
        status = "Average"

    print(
        f"Employee : {employee_name} | " f"Rating : {rating} | " f"Status : {status}"
    )

