# Student grade system
marks = {"Rahim": 85, "Karim": 65, "Ayesha": 92}

for name, mark in marks.items():
    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"
    print(name, "Grade:", grade)
