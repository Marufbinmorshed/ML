# Store monthly sales report
sales = {
    "Jan": [1200, 1500, 1800],
    "Feb": [1100, 1300],
    "Mar": [2000, 2200]
}

for month, values in sales.items():
    total = 0
    for v in values:
        total += v
    print(month, "Total Sales:", total)
