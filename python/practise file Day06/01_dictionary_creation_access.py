# Dictionary creation and access
student = {
    "name": "Rahim",
    "age": 21,
    "department": "CSE"
}

print("Name:", student["name"])
print("Age:", student.get("age"))
print("Department:", student["department"])

for key in student:
    print(key, "=>", student[key])
