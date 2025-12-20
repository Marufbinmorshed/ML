# Online order processing
orders = [
    {"id": 1, "amount": 500, "paid": True},
    {"id": 2, "amount": 1200, "paid": False},
    {"id": 3, "amount": 800, "paid": True}
]

total_paid = 0
for order in orders:
    if order["paid"]:
        total_paid += order["amount"]
        print("Order", order["id"], "Processed")
    else:
        print("Order", order["id"], "Pending")

print("Total Paid Amount:", total_paid)
