# Course completion status
courses = {
    "Rahim": {"Python": True, "ML": False},
    "Karim": {"Python": True, "ML": True}
}

for name, course in courses.items():
    completed = 0
    for status in course.values():
        if status:
            completed += 1
    print(name, "Completed Courses:", completed)
