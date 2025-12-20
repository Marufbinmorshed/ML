# Employee performance evaluation
employees = {
    "Rahim": [80, 85, 90],
    "Karim": [60, 65, 70],
    "Ayesha": [90, 92, 95]
}

for name, scores in employees.items():
    total = 0
    for s in scores:
        total += s
    avg = total / len(scores)

    if avg >= 85:
        grade = "Excellent"
    elif avg >= 70:
        grade = "Good"
    else:
        grade = "Needs Improvement"

    print(name, "Average:", avg, "Performance:", grade)
