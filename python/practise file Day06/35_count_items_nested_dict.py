# Count items in nested dictionary
data = {
    "Group1": {"a": 1, "b": 2},
    "Group2": {"c": 3},
    "Group3": {"d": 4, "e": 5, "f": 6}
}

for group, items in data.items():
    print(group, "Item count:", len(items))
