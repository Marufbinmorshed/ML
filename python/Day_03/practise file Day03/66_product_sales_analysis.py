# Product sales analysis
sales = {
    "Pen": [10, 12, 15, 9],
    "Notebook": [5, 7, 6, 8],
    "Bag": [2, 3, 4, 3]
}

for product, qtys in sales.items():
    total = 0
    for q in qtys:
        total += q
    print(product, "Total sold:", total)
