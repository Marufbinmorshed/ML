# Shopping cart total
cart = {
    "apple": 120,
    "banana": 40,
    "milk": 60,
    "bread": 50
}

total = 0
for item, price in cart.items():
    print(item, "price:", price)
    total += price

print("Total bill:", total)
