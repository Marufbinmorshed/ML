# Weather data analysis
temps = [30, 32, 35, 33, 31, 29]
total = 0

for t in temps:
    total += t

avg = total / len(temps)

above_avg = []
for t in temps:
    if t > avg:
        above_avg.append(t)

print("Average:", avg)
print("Above average temps:", above_avg)
