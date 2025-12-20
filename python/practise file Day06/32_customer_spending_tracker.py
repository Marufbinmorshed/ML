# Customer spending tracker
customers = {
    "Rahim": [120, 300, 150],
    "Karim": [80, 90],
    "Ayesha": [500, 200, 100]
}

for name, spends in customers.items():
    total = 0
    for s in spends:
        total += s
    print(name, "Total Spend:", total)
