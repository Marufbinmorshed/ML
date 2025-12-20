# Expense category summary
expenses = {
    "Food": [120, 150, 200],
    "Transport": [50, 60],
    "Entertainment": [300]
}

for cat, vals in expenses.items():
    total = 0
    for v in vals:
        total += v
    print(cat, "Total Expense:", total)
