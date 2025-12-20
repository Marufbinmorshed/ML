# Mobile data usage calculation
usage = [500, 750, 300, 900, 600]
limit = 3000

total = 0
for u in usage:
    total += u
    print("Used:", u, "MB | Total:", total)

if total > limit:
    print("Data limit exceeded")
else:
    print("Within limit")
