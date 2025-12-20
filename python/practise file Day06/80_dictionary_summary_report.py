# Dictionary summary report
summary = {
    "users": [10, 15, 20],
    "orders": [5, 7, 9]
}

for key, values in summary.items():
    total = 0
    for v in values:
        total += v
    print(key, "Total:", total)
