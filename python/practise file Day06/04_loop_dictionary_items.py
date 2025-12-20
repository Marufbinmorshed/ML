# Loop through dictionary items
marks = {"Math": 85, "Physics": 78, "Chemistry": 90}

total = 0
for subject, mark in marks.items():
    print(subject, "=", mark)
    total += mark

average = total / len(marks)
print("Average marks:", average)
