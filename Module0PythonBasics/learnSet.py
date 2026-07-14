print("****************")
print("DATA TYPES - SET")
print("****************")

employee_skills = {
    "Python",
    "SQL",
    "Azure",
    "Python",
    "Machine Learning",
    "SQL"
}

print("\nEmployee Set Information")
print("------------------------")

print(f"Employee Skills : {employee_skills}")
print(f"Data Type : {type(employee_skills)}")
print(f"Total Unique Skills : {len(employee_skills)}")

print("\nDuplicate Removal")
print("-----------------")

skills_list = [
    "Python",
    "SQL",
    "Python",
    "Azure",
    "SQL",
    "FastAPI"
]

print(f"Original List : {skills_list}")

unique_skills = set(skills_list)

print(f"Unique Skills : {unique_skills}")

print("\nAdd Skill")
print("---------")

print(f"Before Add : {employee_skills}")

employee_skills.add("FastAPI")

print(f"After Add : {employee_skills}")

print("\nUpdate Skills")
print("-------------")

print(f"Before Update : {employee_skills}")

employee_skills.update(["Docker", "Kubernetes"])

print(f"After Update : {employee_skills}")

print("\nRemove Skill")
print("------------")

employee_skills.remove("Azure")

print(f"After Remove : {employee_skills}")

print("\nDiscard Skill")
print("-------------")

employee_skills.discard("Java")

print("No Error Generated")

print("\nMembership Check")
print("----------------")

print(f"Has Python Skill? : {'Python' in employee_skills}")
print(f"Has Java Skill? : {'Java' in employee_skills}")

print("\nLoop Through Set")
print("----------------")

for skill in employee_skills:
    print(f"Skill : {skill}")

print("\nSet Operations")
print("--------------")

employee1_skills = {
    "Python",
    "SQL",
    "Azure",
    "FastAPI"
}

employee2_skills = {
    "Python",
    "AI",
    "SQL",
    "Docker"
}

all_skills = employee1_skills.union(employee2_skills)
print(f"Union All Skills : {all_skills}")

common_skills = employee1_skills.intersection(employee2_skills)
print(f"Intersection Common Skills : {common_skills}")

difference_skills = employee1_skills.difference(employee2_skills)
print(f"Difference Skills : {difference_skills}")


print("\nCopy Set")
print("--------")
copied_skills = employee1_skills.copy()
print(f"Copied Skills : {copied_skills}")

print("\nClear Set")
print("---------")

temp_skills = {"Python", "SQL"}

print(f"Before Clear : {temp_skills}")

temp_skills.clear()

print(f"After Clear : {temp_skills}")

