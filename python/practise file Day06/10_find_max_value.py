# Find key with maximum value
scores = {"A": 85, "B": 92, "C": 78}

max_key = None
max_val = -1

for k, v in scores.items():
    if v > max_val:
        max_val = v
        max_key = k

print("Top scorer:", max_key, max_val)
