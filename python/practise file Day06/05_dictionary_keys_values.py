# Using keys() and values()
population = {"Dhaka": 20000000, "Chittagong": 8000000, "Khulna": 3000000}

for city in population.keys():
    print("City:", city)

for people in population.values():
    print("Population:", people)
