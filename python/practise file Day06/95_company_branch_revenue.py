# Company branch revenue
branches = {
    "Dhaka": [50000, 60000, 55000],
    "Chittagong": [40000, 42000]
}

for branch, revs in branches.items():
    total = 0
    for r in revs:
        total += r
    print(branch, "Total Revenue:", total)
