numbers = [5, 3, -1, 7]

any_negative = any(x < 0 for x in numbers)
all_positive = all(x > 0 for x in numbers)

print("Any negative:", any_negative)
print("All positive:", all_positive)
