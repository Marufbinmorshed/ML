# School fee management
fees = {
    "Rahim": [2000, 1500, 1800],
    "Karim": [1500, 1500],
    "Ayesha": [3000, 2500]
}

for name, payments in fees.items():
    total = 0
    for p in payments:
        total += p
    print(name, "Total Fees Paid:", total)
