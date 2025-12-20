# Online payment summary
payments = {
    "TXN1": 500,
    "TXN2": 1200,
    "TXN3": 800
}

total = 0
for amt in payments.values():
    total += amt

print("Total Payment:", total)
