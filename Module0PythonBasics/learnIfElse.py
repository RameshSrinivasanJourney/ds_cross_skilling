print("****************************")
print("CONTROL STATEMENTS - IF ELSE")
print("****************************")

employee_name = "Ramesh Srinivasan"
years_of_experience = 15
monthly_salary = 100000
performance_rating = 4.7
attendance_percentage = 96

print("\nEmployee Information")
print("--------------------")

print(f"Employee Name : {employee_name}")
print(f"Years Of Experience : {years_of_experience}")
print(f"Monthly Salary : {monthly_salary}")
print(f"Performance Rating : {performance_rating}")
print(f"Attendance Percentage : {attendance_percentage}")

print("\nSimple IF - Senior employee check")
print("---------------------------------")

if years_of_experience >= 10:
    print("Employee is a Senior Employee")

print("\nIF ELSE - Salary category")
print("-------------------------")

if monthly_salary > 50000:
    print("High Salary Employee")
else:
    print("Regular Salary Employee")

print("\nIF ELIF ELSE - Performance rating")
print("---------------------------------")

if performance_rating >= 4.5:
    print("Excellent Performer")
elif performance_rating >= 3.5:
    print("Good Performer")
elif performance_rating >= 2.5:
    print("Average Performer")
else:
    print("Needs Improvement")

print("\nIF with AND - Promotion eligibility")
print("-----------------------------------")

if years_of_experience >= 10 and performance_rating >= 4.5:
    print("Eligible for Promotion")
else:
    print("Not Eligible for Promotion")

print("\nIF with OR - Bonus eligibility")
print("------------------------------")

if performance_rating >= 4.5 or attendance_percentage >= 98:
    print("Eligible for Bonus")
else:
    print("Not Eligible for Bonus")

print("\nNested IF - Leadership role check")
print("---------------------------------")

if years_of_experience >= 10:

    print("Senior Employee")

    if performance_rating >= 4.5:
        print("High Performer")
        print("Eligible for Leadership Role")
    else:
        print("Performance Improvement Required")

else:
    print("Junior Employee")

print("\nBoolean Result - Promotion eligible = True/False")
print("-" * 50)

promotion_eligible = (
        years_of_experience >= 10 and
        performance_rating >= 4.5 and
        attendance_percentage >= 95
)

print(f"Promotion Eligible : {promotion_eligible}")

print("\nTernary Operator - Senior / Junior")
print("----------------------------------")

experience_status = (
    "Senior"
    if years_of_experience >= 10
    else "Junior"
)

print(f"Experience Status : {experience_status}")

print("\nMultiple Conditions")
print("-------------------")

if performance_rating >= 4.5 and attendance_percentage >= 95:
    performance_status = "Excellent"
else:
    performance_status = "Needs Improvement"

print(f"Performance Status : {performance_status}")