# Validate dictionary data
records = {
    "id": [101, 102, 103],
    "name": ["A", "B", "C"],
    "age": [20, 21, 22]
}

valid = True
length = None
for key, values in records.items():
    if length is None:
        length = len(values)
    elif len(values) != length:
        valid = False

print("Data valid:", valid)
