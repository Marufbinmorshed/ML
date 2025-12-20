# Final dictionary report
report = {
    "users": [100, 120, 150],
    "orders": [40, 60, 80],
    "revenue": [50000, 65000, 80000]
}

for key, values in report.items():
    total = 0
    for v in values:
        total += v
    print(key, "Total:", total)
