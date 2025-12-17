# Bank transaction processing
transactions = [1000, -200, -300, 500, -100]
balance = 0

for t in transactions:
    balance += t
    print("Transaction:", t, "Balance:", balance)

print("Final Balance:", balance)
