# Group words by first letter
words = ["apple", "ant", "banana", "ball", "cat", "car"]
groups = {}

for w in words:
    first = w[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(w)

print("Groups:", groups)
