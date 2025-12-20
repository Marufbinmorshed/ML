# Store stock alert
stock = {
    "pen": 2,
    "book": 20,
    "eraser": 1
}

for item, qty in stock.items():
    if qty < 5:
        print(item, "Low Stock Alert")
