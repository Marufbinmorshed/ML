# Sort dictionary by value
prices = {"apple": 120, "banana": 40, "mango": 80}

sorted_items = sorted(prices.items(), key=lambda x: x[1])

for item, price in sorted_items:
    print(item, "=>", price)
