# Inventory update
inventory = {"pen": 10, "book": 5, "eraser": 8}
sold_items = {"pen": 3, "book": 2}

for item, qty in sold_items.items():
    if item in inventory:
        inventory[item] -= qty

print("Updated inventory:", inventory)
