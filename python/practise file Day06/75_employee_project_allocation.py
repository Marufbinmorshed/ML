# Employee project allocation
projects = {
    "ProjectA": ["Rahim", "Karim"],
    "ProjectB": ["Ayesha"]
}

for project, emps in projects.items():
    print(project, "Team Size:", len(emps))
