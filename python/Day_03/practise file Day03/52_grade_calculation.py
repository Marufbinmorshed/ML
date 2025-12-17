# Grade calculation
marks = [85, 72, 90, 60, 55]
grades = []

for m in marks:
    if m >= 80:
        grades.append("A")
    elif m >= 70:
        grades.append("B")
    elif m >= 60:
        grades.append("C")
    else:
        grades.append("F")

print("Grades:", grades)
