# Dictionary report generation
report = {
    "sales": [1000, 1200, 1100],
    "profit": [200, 250, 230]
}

for section, data in report.items():
    total = 0
    for d in data:
        total += d
    print(section, "Total:", total)
