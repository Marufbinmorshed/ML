# University department analysis
departments = {
    "CSE": [120, 130, 140],
    "EEE": [100, 110, 105],
    "BBA": [90, 95, 100]
}

for dept, students in departments.items():
    total = 0
    for s in students:
        total += s
    avg = total / len(students)
    print(dept, "Average Students:", avg)
