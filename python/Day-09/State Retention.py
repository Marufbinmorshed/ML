import sys

lst = [x for x in range(1_000_000)]
gen = (x for x in range(1_000_000))

print("List size:", sys.getsizeof(lst))
print("Generator size:", sys.getsizeof(gen))
