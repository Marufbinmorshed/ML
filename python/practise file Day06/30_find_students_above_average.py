# Find students above average
scores = {"A": 70, "B": 85, "C": 60, "D": 90}

total = 0
for v in scores.values():
    total += v

avg = total / len(scores)

above_avg = {}
for name, mark in scores.items():
    if mark > avg:
        above_avg[name] = mark

print("Class Average:", avg)
print("Above Average Students:", above_avg)
