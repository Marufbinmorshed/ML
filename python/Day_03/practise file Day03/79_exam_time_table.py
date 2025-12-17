# Exam timetable display
timetable = {
    "Day 1": ["Math", "Physics"],
    "Day 2": ["Chemistry", "Biology"]
}

for day, exams in timetable.items():
    print(day)
    for exam in exams:
        print(" -", exam)
