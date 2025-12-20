# Department budget analysis
budgets = {
    "IT": [50000, 60000, 55000],
    "HR": [30000, 32000, 31000],
    "Sales": [70000, 75000, 72000]
}

for dept, vals in budgets.items():
    total = 0
    for v in vals:
        total += v
    print(dept, "Total Budget:", total)
