# Scholarship eligibility
students = {
    "Rahim": {"gpa": 3.5, "income": 30000},
    "Karim": {"gpa": 3.2, "income": 50000},
    "Ayesha": {"gpa": 3.9, "income": 25000}
}

for name, info in students.items():
    if info["gpa"] >= 3.5 and info["income"] < 40000:
        print(name, "Eligible for Scholarship")
    else:
        print(name, "Not Eligible")
