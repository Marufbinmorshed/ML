# Attendance percentage
attendance = {
    "Rahim": [1,1,0,1,1],
    "Karim": [1,0,0,1,0],
    "Ayesha": [1,1,1,1,1]
}

for name, days in attendance.items():
    present = 0
    for d in days:
        if d == 1:
            present += 1
    percentage = (present / len(days)) * 100
    print(name, "Attendance:", percentage, "%")
