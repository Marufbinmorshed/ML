# Monthly weather report
weather = {
    "Jan": [20, 22, 19],
    "Feb": [25, 26, 24],
    "Mar": [30, 32, 31]
}

for month, temps in weather.items():
    avg = sum(temps) / len(temps)
    print(month, "Average Temp:", avg)
