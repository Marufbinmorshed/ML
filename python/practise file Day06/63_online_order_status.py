# Online order status system
orders = {
    "ORD1": "Delivered",
    "ORD2": "Pending",
    "ORD3": "Cancelled"
}

for oid, status in orders.items():
    print(oid, "Status:", status)
