print("******************")
print("EXCEPTION HANDLING")
print("******************")

print("\nBasic Try Except")
print("------------------")
print("sample input ABC")
try:
    employee_id = int(input("Enter Employee ID: "))
    print(f"Employee ID : {employee_id}")

except ValueError:
    print("Invalid Employee ID. Numbers only.")


print("\nDivision By Zero")
print("----------------")
print("sample input 100000,0")
try:

    monthly_salary = float(
        input("Enter Monthly Salary: ")
    )

    working_days = int(
        input("Enter Working Days: ")
    )

    daily_salary = monthly_salary / working_days

    print(f"Daily Salary : {daily_salary:.2f}")

except ZeroDivisionError:
    print("Working Days cannot be zero.")


print("\nMultiple Exceptions")
print("-------------------")
print("sample input ABC,0")
try:

    employee_id = int(input("Enter Employee ID: "))
    experience = int(input("Enter Experience: "))

    result = employee_id / experience

    print(result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Experience cannot be zero.")


print("\nGeneric Exception")
print("-----------------")

try:

    employee = {
        "employee_id": 1001,
        "employee_name": "Ramesh Srinivasan"
    }

    print(employee["salary"])

except Exception as ex:
    print(f"Error : {ex}")


print("\nElse Block")
print("----------")

try:

    rating = float(
        input("Enter Rating: ")
    )

except ValueError:

    print("Invalid Rating")

else:

    print(f"Rating Entered : {rating}")



print("\nFinally Block")
print("-------------")

try:

    salary = 100000
    print(f"Salary : {salary}")

except Exception:

    print("Error Occurred")

finally:

    print("Execution Completed")


print("\nFile Handling")
print("-------------")

try:

    file = open("employee.txt", "r")

    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:

    print("employee.txt file not found.")


print("\nCustom Exception")
print("----------------")
print("sample input 8")
try:

    performance_rating = float(
        input("Enter Performance Rating (1-5): ")
    )

    if performance_rating < 1 or performance_rating > 5:
        raise ValueError(
            "Rating must be between 1 and 5"
        )

    print(
        f"Performance Rating : {performance_rating}"
    )

except ValueError as ex:

    print(f"Validation Error : {ex}")



print("\nEmployee Salary Validation")
print("--------------------------")

try:

    monthly_salary = float(
        input("Enter Monthly Salary: ")
    )

    if monthly_salary < 0:
        raise Exception(
            "Salary cannot be negative."
        )

    print(
        f"Monthly Salary : {monthly_salary:.2f}"
    )

except Exception as ex:

    print(f"Error : {ex}")


print("\nEmployee Evaluation Report")
print("==========================")

try:

    employee_name = input(
        "Enter Employee Name: "
    )

    experience = int(
        input("Enter Experience: ")
    )

    rating = float(
        input("Enter Rating: ")
    )

    print(f"Employee Name : {employee_name}")
    print(f"Experience    : {experience}")
    print(f"Rating        : {rating}")

except ValueError:

    print("Invalid numeric value entered.")

finally:

    print("Employee Processing Completed.")