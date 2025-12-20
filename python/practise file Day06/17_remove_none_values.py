# Remove None values from dictionary
data = {"a": 10, "b": None, "c": 30, "d": None}

cleaned = {}
for k, v in data.items():
    if v is not None:
        cleaned[k] = v

print("Cleaned dictionary:", cleaned)
