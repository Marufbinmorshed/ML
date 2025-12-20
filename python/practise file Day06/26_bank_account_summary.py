# Bank account summary
accounts = {
    "A001": [1000, -200, 500],
    "A002": [2000, -500, -300],
    "A003": [1500, 700, -100]
}

for acc, trans in accounts.items():
    balance = 0
    for t in trans:
        balance += t
    print(acc, "Final Balance:", balance)
