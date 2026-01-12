data = [(1, 2), (3, 4)]

# This will FAIL because tuples are immutable
try:
    result = list(map(lambda x: x[0].__setitem__(0, 100), data))
except Exception as e:
    print("Error:", e)

# Correct functional approach (create new tuples)
fixed = list(map(lambda x: (x[0] + 10, x[1] + 10), data))

print(fixed)
