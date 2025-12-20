# Employee bonus calculation
employees = {
    "Rahim": 50000,
    "Karim": 30000,
    "Ayesha": 70000
}

for name, salary in employees.items():
    bonus = salary * 0.10
    print(name, "Bonus:", bonus)
