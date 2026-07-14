print("******************")
print("DATA TYPES - TUPLE")
print("******************")

employee_details = (
    1001,
    "Ramesh Srinivasan",
    "Associate Architect",
    "01-Jan-2020"
)

print("\nEmployee Tuple Information")
print("--------------------------")

print(f"Employee Details : {employee_details}")
print(f"Data Type : {type(employee_details)}")
print(f"Total Elements : {len(employee_details)}")

print("\nTuple Indexing")
print("--------------")

print(f"Employee ID : {employee_details[0]}")
print(f"Employee Name : {employee_details[1]}")
print(f"Designation : {employee_details[2]}")
print(f"Date Of Joining : {employee_details[3]}")
print(f"Last Element : {employee_details[-1]}")

print("\nTuple Slicing")
print("-------------")

print(f"First 2 Elements : {employee_details[0:2]}")
print(f"Last 2 Elements : {employee_details[-2:]}")
print(f"All Elements : {employee_details[:]}")

print("\nMembership Checks")
print("-----------------")

print(f"Contains 'Ramesh Srinivasan'? : {'Ramesh Srinivasan' in employee_details}")
print(f"Contains 'Manager'? : {'Manager' in employee_details}")

print("\nTuple Methods")
print("-------------")

employee_ratings = (5, 4, 5, 3, 5, 4)

print(f"Employee Ratings : {employee_ratings}")
print(f"Count Of Rating 5 : {employee_ratings.count(5)}")

print("\nFinding Position")
print("----------------")

print(f"Index Of Rating 3 : {employee_ratings.index(3)}")

print("\nLoop Through Tuple")
print("------------------")

for detail in employee_details:
    print(f"Value : {detail}")

print("\nTuple Packing")
print("-------------")

employee_info = (1001, "Ramesh", "Architect")

print(f"Packed Tuple : {employee_info}")

print("\nTuple Unpacking")
print("---------------")

employee_id, employee_name, designation = employee_info

print(f"Employee ID  : {employee_id}")
print(f"Employee Name : {employee_name}")
print(f"Designation : {designation}")

print("\nTuple Functions")
print("---------------")

project_scores = (85, 90, 88, 95, 92)

print(f"Project Scores : {project_scores}")
print(f"Maximum Score : {max(project_scores)}")
print(f"Minimum Score : {min(project_scores)}")
print(f"Total Score : {sum(project_scores)}")
print(f"Average Score : {sum(project_scores) / len(project_scores):.2f}")