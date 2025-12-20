# Employee retirement check
employees = {
    "Rahim": 58,
    "Karim": 55,
    "Ayesha": 45
}

for name, age in employees.items():
    if age >= 60:
        print(name, "Eligible for Retirement")
    else:
        print(name, "Not Eligible")
