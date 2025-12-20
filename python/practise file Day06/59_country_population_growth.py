# Country population growth
population = {
    "2020": 160,
    "2021": 165,
    "2022": 170
}

years = list(population.keys())
for i in range(1, len(years)):
    growth = population[years[i]] - population[years[i-1]]
    print(years[i], "Growth:", growth)
