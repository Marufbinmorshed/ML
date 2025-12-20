# School exam schedule
schedule = {
    "Day1": ["Math", "Physics"],
    "Day2": ["Chemistry", "Biology"],
    "Day3": ["English"]
}

for day, exams in schedule.items():
    print(day)
    for e in exams:
        print(" -", e)
