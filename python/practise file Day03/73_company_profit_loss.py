# Company profit/loss analysis
monthly = [5000, -2000, 3000, -1000, 4000]

profit = 0
loss = 0
for m in monthly:
    if m > 0:
        profit += m
    else:
        loss += m

print("Total Profit:", profit)
print("Total Loss:", loss)
