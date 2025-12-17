# Daily expense tracker
expenses = {
    "Monday": [50, 30, 20],
    "Tuesday": [60, 40],
    "Wednesday": [25, 35, 15]
}

weekly_total = 0
for day, costs in expenses.items():
    day_total = 0
    for c in costs:
        day_total += c
    weekly_total += day_total
    print(day, "Total Expense:", day_total)

print("Weekly Expense:", weekly_total)
