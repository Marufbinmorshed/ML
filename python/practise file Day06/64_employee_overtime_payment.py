# Employee overtime payment calculation
overtime = {
    "Rahim": [2, 3, 1],
    "Karim": [1, 1],
    "Ayesha": [4, 2]
}

rate = 500
for name, hours in overtime.items():
    total_hours = 0
    for h in hours:
        total_hours += h
    print(name, "Overtime Pay:", total_hours * rate)
