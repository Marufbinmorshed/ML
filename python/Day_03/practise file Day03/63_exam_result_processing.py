# Exam result processing
results = {
    "Math": [78, 85, 90, 60],
    "Physics": [70, 75, 80, 65],
    "Chemistry": [88, 92, 85, 90]
}

for subject, marks in results.items():
    passed = 0
    for m in marks:
        if m >= 40:
            passed += 1
    print(subject, "Pass count:", passed, "Out of:", len(marks))
