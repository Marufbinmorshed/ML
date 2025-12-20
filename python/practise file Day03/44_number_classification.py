# Classify numbers
numbers = list(range(1, 51))

even = []
odd = []
div_by_five = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

    if n % 5 == 0:
        div_by_five.append(n)

print("Even:", even)
print("Odd:", odd)
print("Divisible by 5:", div_by_five)
