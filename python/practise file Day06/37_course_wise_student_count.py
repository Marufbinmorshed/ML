# Course-wise student count
courses = {
    "Python": ["A", "B", "C"],
    "ML": ["A", "C"],
    "DS": ["B", "C", "D", "E"]
}

for course, students in courses.items():
    print(course, "Students:", len(students))
