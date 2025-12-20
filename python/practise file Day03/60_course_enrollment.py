# Course enrollment summary
courses = {
    "Python": ["A", "B", "C"],
    "ML": ["A", "C"],
    "Data Science": ["B", "C", "D"]
}

for course, students in courses.items():
    print(course, "Total students:", len(students))
    for s in students:
        print("-", s)
