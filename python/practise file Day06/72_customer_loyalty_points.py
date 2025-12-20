# Customer loyalty points
customers = {
    "Rahim": [100, 200, 150],
    "Karim": [50, 80],
    "Ayesha": [300, 200]
}

for name, points in customers.items():
    total = 0
    for p in points:
        total += p
    print(name, "Total Points:", total)
