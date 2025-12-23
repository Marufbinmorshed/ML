import time

data = list(range(1000000))

# Build dictionary
start = time.time()
d = {x: True for x in data}
print("Dictionary build time:", time.time() - start)

# Search
start = time.time()
print(999999 in d)
print("Lookup time:", time.time() - start)
)
