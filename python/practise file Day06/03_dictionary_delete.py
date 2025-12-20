# Delete items from dictionary
data = {"a": 10, "b": 20, "c": 30}

del data["b"]
removed = data.pop("c")

print("Removed c:", removed)
print("Remaining data:", data)
