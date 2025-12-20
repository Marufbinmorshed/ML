# Nested dictionary example
students = {
    "Rahim": {"Math": 80, "Physics": 75},
    "Karim": {"Math": 70, "Physics": 65},
    "Ayesha": {"Math": 90, "Physics": 88}
}

for name, subjects in students.items():
    total = 0
    for mark in subjects.values():
        total += mark
    avg = total / len(subjects)
    print(name, "Average:", avg)
