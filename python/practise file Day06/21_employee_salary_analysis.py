# Employee salary analysis using dictionary
employees = {
    "Rahim": [30000, 32000, 35000],
    "Karim": [25000, 26000, 28000],
    "Ayesha": [40000, 42000, 45000]
}

for name, salaries in employees.items():
    total = 0
    for s in salaries:
        total += s
    avg = total / len(salaries)
    print(name, "Average Salary:", avg)
