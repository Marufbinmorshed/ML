# Copy vs reference in dictionary
a = {"x": 1, "y": 2}
b = a
c = a.copy()

a["z"] = 3

print("a:", a)
print("b:", b)
print("c:", c)
