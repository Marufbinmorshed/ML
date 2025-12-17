# Monthly temperature report
temps = [
    [30, 32, 31, 33],
    [28, 29, 30, 31],
    [35, 36, 34, 33]
]

month = 1
for week in temps:
    total = 0
    for t in week:
        total += t
    avg = total / len(week)
    print("Month", month, "Average Temp:", avg)
    month += 1
