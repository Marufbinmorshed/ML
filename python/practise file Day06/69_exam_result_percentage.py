# Exam result percentage calculation
results = {
    "Rahim": [80, 75, 70],
    "Karim": [60, 65, 55],
    "Ayesha": [90, 88, 92]
}

for name, marks in results.items():
    total = 0
    for m in marks:
        total += m
    percent = total / len(marks)
    print(name, "Percentage:", percent)
