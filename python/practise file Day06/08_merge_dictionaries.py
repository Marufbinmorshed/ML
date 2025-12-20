# Merge two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = {}
for d in (d1, d2):
    for k, v in d.items():
        merged[k] = v

print("Merged dictionary:", merged)
