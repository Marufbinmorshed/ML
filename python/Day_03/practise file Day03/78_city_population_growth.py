# City population growth
population = [100000, 105000, 110000, 120000]

for i in range(1, len(population)):
    growth = population[i] - population[i-1]
    print("Year", i, "Growth:", growth)
