# Online course progress
students = {
    "Rahim": [1,1,1,0,1],
    "Karim": [1,0,0,0,1],
    "Ayesha": [1,1,1,1,1]
}

for name, progress in students.items():
    completed = 0
    for p in progress:
        if p == 1:
            completed += 1
    percent = (completed / len(progress)) * 100
    print(name, "Completion:", percent, "%")
