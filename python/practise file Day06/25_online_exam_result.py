# Online exam result processing
results = {
    "Rahim": {"Math": 80, "Physics": 75},
    "Karim": {"Math": 60, "Physics": 55},
    "Ayesha": {"Math": 90, "Physics": 88}
}

for student, subjects in results.items():
    total = 0
    for mark in subjects.values():
        total += mark
    avg = total / len(subjects)
    print(student, "Average:", avg)
