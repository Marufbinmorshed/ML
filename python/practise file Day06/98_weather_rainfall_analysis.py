# Weather rainfall analysis
rainfall = {
    "Jan": [10, 12, 8],
    "Feb": [5, 7, 6]
}

for month, rains in rainfall.items():
    print(month, "Total Rainfall:", sum(rains))
