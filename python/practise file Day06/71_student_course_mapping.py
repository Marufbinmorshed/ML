# Student course mapping
courses = {
    "Rahim": ["Python", "ML"],
    "Karim": ["Python"],
    "Ayesha": ["Python", "ML", "DS"]
}

for student, subs in courses.items():
    print(student, "Courses:", ", ".join(subs))
