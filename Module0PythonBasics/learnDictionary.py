print("***********************")
print("DATA TYPES - DICTIONARY")
print("***********************")

employee = {
    "employee_id": 1001,
    "employee_name": "Ramesh Srinivasan",
    "designation": "Associate Architect",
    "salary": 100000.50,
    "experience": 15,
    "active": True
}

print("\nEmployee Dictionary Information")
print("-------------------------------")

print(f"Employee Details : {employee}")
print(f"Data Type : {type(employee)}")
print(f"Total Keys : {len(employee)}")

print("\nAccess Values")
print("-------------")

print(f"Employee ID : {employee['employee_id']}")
print(f"Employee Name : {employee['employee_name']}")
print(f"Designation : {employee['designation']}")
print(f"Salary : {employee['salary']}")

print("\nUsing get()")
print("-----------")

print(f"Employee Name : {employee.get('employee_name')}")
print(f"Department : {employee.get('department')}")
print(f"Department : {employee.get('department', 'Not Assigned')}")

print("\nAdd New Key")
print("-----------")

employee["department"] = "Engineering"

print(f"Department Added : {employee['department']}")

print("\nUpdate Existing Value")
print("---------------------")

print(f"Before Salary : {employee['salary']}")

employee["salary"] = 120000
print(f"Updated Salary : {employee['salary']}")

print("\nRemove Key")
print("----------")

print(f"Before Remove : {employee}")

employee.pop("active")
print(f"After Remove : {employee}")

print("\nDictionary Keys")
print("---------------")

print(f"Keys : {employee.keys()}")

print("\nDictionary Values")
print("-----------------")

print(f"Values : {employee.values()}")

print("\nDictionary Items")
print("----------------")

print(f"Items : {employee.items()}")

print("\nCheck Key Exists")
print("----------------")

print(f"salary Exists? : {'salary' in employee}")
print(f"bonus Exists? : {'bonus' in employee}")

print("\nLoop Through Key-Value Pairs")
print("----------------------------")

for key, value in employee.items():
    print(f"{key} : {value}")

print("\nNested Dictionary")
print("-----------------")

employee_profile = {
    "employee_id": 1001,
    "employee_name": "Ramesh Srinivasan",
    "project": {
        "project_name": "AI Learning",
        "duration_months": 6
    }
}

print(f"Project Name : {employee_profile['project']['project_name']}")
print(f"Duration : {employee_profile['project']['duration_months']} Months")

print("\nDictionary Functions")
print("--------------------")

print(f"Total Fields : {len(employee)}")

employee_copy = employee.copy()

print(f"Copied Dictionary : {employee_copy}")

