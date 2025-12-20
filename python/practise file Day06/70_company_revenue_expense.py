# Company revenue vs expense
finance = {
    "revenue": [10000, 12000, 11000],
    "expense": [6000, 6500, 6200]
}

for key, values in finance.items():
    total = 0
    for v in values:
        total += v
    print(key, "Total:", total)
