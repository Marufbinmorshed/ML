# Employee department transfer
employees = {
    "Rahim": "IT",
    "Karim": "HR",
    "Ayesha": "Sales"
}

employees["Karim"] = "IT"

for emp, dept in employees.items():
    print(emp, "Department:", dept)
