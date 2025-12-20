# Employee skill matrix
skills = {
    "Rahim": ["Python", "ML"],
    "Karim": ["Excel", "Accounts"],
    "Ayesha": ["Python", "Data Science"]
}

for name, skill_list in skills.items():
    print(name, "Skills:")
    for s in skill_list:
        print(" -", s)
