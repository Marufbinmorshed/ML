# Reverse dictionary mapping
original = {"a": 1, "b": 2, "c": 1}
reversed_map = {}

for k, v in original.items():
    if v not in reversed_map:
        reversed_map[v] = []
    reversed_map[v].append(k)

print("Reversed mapping:", reversed_map)
