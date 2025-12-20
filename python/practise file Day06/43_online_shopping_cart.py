# Online shopping cart using dictionary
cart = {
    "pen": 3,
    "book": 2,
    "bag": 1
}
prices = {
    "pen": 10,
    "book": 50,
    "bag": 400
}

total = 0
for item, qty in cart.items():
    cost = prices[item] * qty
    total += cost
    print(item, "Cost:", cost)

print("Total Bill:", total)
