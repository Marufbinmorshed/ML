list_a = list(range(10_000))
list_b = list(range(5_000, 15_000))

duplicates = []

for a in list_a:
    for b in list_b:
        if a == b:
            duplicates.append(a)

print("Duplicates:", len(duplicates))

