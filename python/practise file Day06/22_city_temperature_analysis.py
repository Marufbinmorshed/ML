# City temperature analysis
temps = {
    "Dhaka": [30, 32, 35, 33],
    "Chittagong": [28, 29, 31, 30],
    "Sylhet": [26, 27, 28, 29]
}

for city, values in temps.items():
    max_temp = values[0]
    for v in values:
        if v > max_temp:
            max_temp = v
    print(city, "Max Temp:", max_temp)
