# Student subject count
subjects = {
    "Rahim": ["Math", "Physics", "Chemistry"],
    "Karim": ["Math", "English"]
}

for name, subs in subjects.items():
    print(name, "Subjects Enrolled:", len(subs))
