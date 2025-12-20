# Class attendance summary
classes = {
    "Class 1": [1,1,0,1],
    "Class 2": [0,1,1,1],
    "Class 3": [1,1,1,1]
}

for cls, data in classes.items():
    present = 0
    for d in data:
        if d == 1:
            present += 1
    print(cls, "Attendance:", present, "/", len(data))
