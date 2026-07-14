print("***************************")
print("DATA TYPES - BOOLEAN (BOOL)")
print("***************************")

employee_name = "Ramesh Srinivasan"
years_of_experience = 15
monthly_salary = 100000
performance_rating = 4.7
attendance_percentage = 96.5

print("\nEmployee Information")
print("--------------------")

print(f"Employee Name : {employee_name}")
print(f"Years Of Experience : {years_of_experience}")
print(f"Monthly Salary : {monthly_salary}")
print(f"Performance Rating : {performance_rating}")
print(f"Attendance Percentage : {attendance_percentage}")

is_active_employee = True
is_on_probation = False

print("\nBoolean Values")
print("--------------")

print(f"Is Active Employee? : {is_active_employee}")
print(f"Is On Probation? : {is_on_probation}")
print(f"Data Type : {type(is_active_employee)}")

print("\nComparison Operations")
print("---------------------")

print(f"Experience >= 10 Years? : {years_of_experience >= 10}")
print(f"Salary > 50K? : {monthly_salary > 50000}")
print(f"Rating > 4.5? : {performance_rating > 4.5}")
print(f"Attendance > 95%? : {attendance_percentage > 95}")
print(f"Experience == 15? : {years_of_experience == 15}")
print(f"Salary != 50000? : {monthly_salary != 50000}")

print("\nEmployee Evaluation")
print("-------------------")

is_senior_employee = years_of_experience >= 10
is_high_performer = performance_rating >= 4.5
has_good_attendance = attendance_percentage >= 95

print(f"Senior Employee? : {is_senior_employee}")
print(f"High Performer? : {is_high_performer}")
print(f"Good Attendance? : {has_good_attendance}")

print("\nAND Operator")
print("------------")

eligible_for_promotion = (
        is_senior_employee and
        is_high_performer and
        has_good_attendance
)

print(f"Eligible For Promotion? : {eligible_for_promotion}")

print("\nOR Operator")
print("-----------")

eligible_for_bonus = (
        performance_rating >= 4.5 or
        attendance_percentage >= 98
)

print(f"Eligible For Bonus? : {eligible_for_bonus}")

print("\nNOT Operator")
print("------------")

print(f"On Probation? : {is_on_probation}")
print(f"Not On Probation? : {not is_on_probation}")

print("\nMembership Checks")
print("-----------------")

employee_skills = ["Python", "SQL", "FastAPI", "Machine Learning"]

print(f"Employee Skills : {employee_skills}")
print(f"Has Python Skill? : {'Python' in employee_skills}")
print(f"Has Java Skill? : {'Java' in employee_skills}")