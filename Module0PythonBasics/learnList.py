print("*" * 50)
print("DATA TYPES - LIST")
print("***************")

employee_name = "Ramesh Srinivasan"

employee_skills = [
    "Python",
    "SQL",
    "Azure",
    "Machine Learning",
    "FastAPI"
]

print("\nList Properties")
print("---------------")

print(f"Employee Skills : {employee_skills}")
print(f"Total Skills : {len(employee_skills)}")
print(f"Data Type : {type(employee_skills)}")

print("\nList Indexing")
print("-------------")

print(f"First Skill : {employee_skills[0]}")
print(f"Second Skill : {employee_skills[1]}")
print(f"Last Skill : {employee_skills[-1]}")

print("\nList Slicing")
print("------------")

print(f"First 3 Skills : {employee_skills[0:3]}")
print(f"Skills From Index 2 : {employee_skills[2:]}")
print(f"Last 2 Skills : {employee_skills[-2:]}")
print(f"All Skills : {employee_skills[:]}")

print("\nAdding Skills")
print("--------------")

employee_skills.append("Data Science")

print(f"After Append : {employee_skills}")

employee_skills.insert(1, "C#")

print(f"After Insert : {employee_skills}")


print("\nRemoving Skills")
print("---------------")

employee_skills.remove("Azure")

print(f"After Remove : {employee_skills}")

removed_skill = employee_skills.pop()

print(f"Removed Skill Pop : {removed_skill}")
print(f"Remaining Skills : {employee_skills}")


print("\nSearching Skills")
print("----------------")

print(f"Python Exists? : {'Python' in employee_skills}")
print(f"Java Exists? : {'Java' in employee_skills}")

print("\nFinding Position")
print("----------------")

print(f"Index of SQL : {employee_skills.index('SQL')}")

print("\nSorting Skills")
print("---------------")

employee_skills.sort()

print(f"Sorted Skills : {employee_skills}")

print("\nReverse Skills")
print("--------------")

employee_skills.reverse()

print(f"Reversed Skills : {employee_skills}")

print("\nLoop Through List")
print("-----------------")

for skill in employee_skills:
    print(f"Skill : {skill}")