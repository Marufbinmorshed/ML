# Product price update
products = {
    "pen": 10,
    "book": 50,
    "bag": 400
}

for item in products:
    products[item] += products[item] * 0.10

print("Updated prices:", products)
