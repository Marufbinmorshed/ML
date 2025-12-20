# Exam topper by subject
results = {
    "Math": {"A": 80, "B": 90, "C": 70},
    "Physics": {"A": 85, "B": 75, "C": 88}
}

for subject, marks in results.items():
    top_student = None
    top_mark = -1
    for name, mark in marks.items():
        if mark > top_mark:
            top_mark = mark
            top_student = name
    print(subject, "Topper:", top_student, top_mark)
