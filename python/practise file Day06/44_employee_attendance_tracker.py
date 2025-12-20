# Employee attendance tracker
attendance = {
    "Rahim": [1,1,1,0,1],
    "Karim": [1,0,1,0,1],
    "Ayesha": [1,1,1,1,1]
}

for name, days in attendance.items():
    present = 0
    for d in days:
        if d == 1:
            present += 1
    print(name, "Present Days:", present)
