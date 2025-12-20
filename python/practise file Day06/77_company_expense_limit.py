# Company expense limit check
expenses = {
    "IT": 45000,
    "HR": 30000,
    "Sales": 70000
}

limit = 50000
for dept, amount in expenses.items():
    if amount > limit:
        print(dept, "Exceeded Limit")
