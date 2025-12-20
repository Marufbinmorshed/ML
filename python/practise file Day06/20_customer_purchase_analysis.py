# Customer purchase analysis
purchases = {
    "Rahim": [120, 250, 300],
    "Karim": [80, 150],
    "Ayesha": [500, 200]
}

for name, bills in purchases.items():
    total = 0
    for b in bills:
        total += b
    print(name, "Total Purchase:", total)
