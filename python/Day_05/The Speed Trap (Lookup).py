#  list 
numbers_list = list(range(10))   # imagine this is 1,000,000 numbers

#  set 
numbers_set = set(numbers_list)

# Number to check
target = -1

# List lookup
found_in_list = target in numbers_list

print("Found in list:", found_in_list)

# Set lookup
found_in_set = target in numbers_set

print("Found in set:", found_in_set)
