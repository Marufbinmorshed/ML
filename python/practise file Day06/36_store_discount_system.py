# Store discount system
customers = {
    "Rahim": 1200,
    "Karim": 800,
    "Ayesha": 2000
}

for name, amount in customers.items():
    if amount >= 1500:
        discount = 0.15
    elif amount >= 1000:
        discount = 0.10
    else:
        discount = 0.05
    final_amount = amount - (amount * discount)
    print(name, "Final Amount:", final_amount)
