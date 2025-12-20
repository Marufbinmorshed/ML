# Exam result summary
results = {
    "A": {"Math": 85, "Physics": 80},
    "B": {"Math": 70, "Physics": 65},
    "C": {"Math": 90, "Physics": 88}
}

for student, subs in results.items():
    total = 0
    for m in subs.values():
        total += m
    print(student, "Total Marks:", total)
