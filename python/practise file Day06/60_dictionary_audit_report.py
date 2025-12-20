# Dictionary audit report
report = {
    "income": [1000, 1200, 1100],
    "expense": [500, 600, 550]
}

for section, data in report.items():
    total = 0
    for d in data:
        total += d
    print(section, "Total:", total)
