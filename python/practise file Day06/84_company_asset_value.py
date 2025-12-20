# Company asset value calculation
assets = {
    "Laptops": [50000, 60000, 55000],
    "Servers": [200000, 180000]
}

for asset, values in assets.items():
    total = 0
    for v in values:
        total += v
    print(asset, "Total Value:", total)
