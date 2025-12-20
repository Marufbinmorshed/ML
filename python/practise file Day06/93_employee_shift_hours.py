# Employee shift hours
shifts = {
    "Rahim": [8, 9, 8],
    "Karim": [7, 8],
    "Ayesha": [9, 9, 8]
}

for emp, hours in shifts.items():
    total = 0
    for h in hours:
        total += h
    print(emp, "Total Hours:", total)
