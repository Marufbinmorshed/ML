# Salary increment calculation
employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 40000},
    {"name": "C", "salary": 50000}
]

for emp in employees:
    if emp["salary"] < 40000:
        emp["salary"] += 5000
    else:
        emp["salary"] += 3000

for emp in employees:
    print(emp["name"], emp["salary"])
