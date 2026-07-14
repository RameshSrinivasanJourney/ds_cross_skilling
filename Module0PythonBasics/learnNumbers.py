print("************")
print("Data Types:-")
print("************")
print("\nLearn Numbers (int + float) :-")
print("==============================")

import math

employee_name = "Ramesh Srinivasan"

# Integer Values
employee_id = 1001
years_of_experience = 15
working_days_in_month = 30

# Float Values
monthly_salary = 100000.50
performance_rating = 4.7
salary_hike_percentage = 12.5

print("\nEmployee Information")
print("--------------------")

print(f"Employee ID : {employee_id}")
print(f"Employee Name : {employee_name}")
print(f"Monthly Salary : {monthly_salary:.2f}")
print(f"Years of Experience : {years_of_experience}")
print(f"Working Days Per Month : {working_days_in_month}")
print(f"Performance Rating : {performance_rating}")
print(f"Salary Hike Percentage : {salary_hike_percentage}%")

print("\nArithmetic Operations")
print("---------------------")

annual_salary = monthly_salary * 12
annual_bonus_amount = annual_salary * salary_hike_percentage / 100
annual_salary_after_bonus = f"{annual_salary + annual_bonus_amount:.2f}"

monthly_bonus_amount = monthly_salary * salary_hike_percentage / 100
monthly_salary_after_bonus = f"{monthly_salary + monthly_bonus_amount:.2f}"

daily_salary = monthly_salary / working_days_in_month
daily_bonus_amount = daily_salary * salary_hike_percentage / 100
daily_salary_after_bonus = f"{daily_salary + daily_bonus_amount:.2f}"

print(f"Annual Salary : {annual_salary:.2f}  | Bonus : {annual_bonus_amount:.2f} | After Bonus : {annual_salary_after_bonus}")
print(f"Monthly Salary : {monthly_salary:.2f} | Bonus : {monthly_bonus_amount:.2f} | After Bonus : {monthly_salary_after_bonus}")
print(f"Daily Salary : {daily_salary:.2f} | Bonus : {daily_bonus_amount:.2f} | After Bonus : {daily_salary_after_bonus}")

print(f"Experience After 5 Years : {years_of_experience + 5}")
print(f"Years Remaining To Reach 20 : {20 - years_of_experience}")

print("\nNumber Functions")
print("----------------")

print(f"Round Rating {performance_rating} : {round(performance_rating)}")
print(f"Ceiling Rating {performance_rating} : {math.ceil(performance_rating)}")
print(f"Floor Rating {performance_rating} : {math.floor(performance_rating)}")

salary_difference = -2500.75

print(f"Salary Difference : {salary_difference}")
print(f"Absolute Difference : {abs(salary_difference)}")

print(f"Maximum Value : {max(monthly_salary, annual_salary)}")
print(f"Minimum Value : {min(monthly_salary, annual_salary)}")

print("\nEmployee Eligibility Checks")
print("---------------------------")

print(f"Eligible For Senior Role? : {years_of_experience >= 10}")
print(f"Salary Above 50K? : {monthly_salary > 50000}")
print(f"Rating Above 4.5? : {performance_rating > 4.5}")
print(f"Experience Above 20 Years? : {years_of_experience > 20}")

print("\nType Conversion")
print("---------------")

employee_code = input("Enter Employee Code: ")

print(f"Employee Code Value : {employee_code}")
print(f"Original Data Type : {type(employee_code)}")

employee_code_int = int(employee_code)

print(f"Converted Value : {employee_code_int}")
print(f"Converted Data Type : {type(employee_code_int)}")

print("\nNumber Formatting")
print("-----------------")

print(f"Monthly Salary : {monthly_salary:.2f}")
print(f"Annual Salary : {annual_salary:,.2f}")
print(f"Bonus Amount : {monthly_bonus_amount:.2f}")
print(f"Performance Rating : {performance_rating:.1f}")