# Analyze student marks using loops
students = {
    "Rahim": [78, 85, 90],
    "Karim": [65, 70, 72],
    "Ayesha": [88, 92, 95]
}

for name, marks in students.items():
    total = 0
    for m in marks:
        total += m
    avg = total / len(marks)
    print(name, "Total:", total, "Average:", avg)
