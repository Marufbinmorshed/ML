# Weather alert system
weather = {
    "Dhaka": 38,
    "Chittagong": 34,
    "Sylhet": 36
}

for city, temp in weather.items():
    if temp >= 37:
        print(city, "Heat Alert")
