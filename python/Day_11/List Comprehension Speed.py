numbers = [1, 2, 3, 4, 5]

# Using map + lambda
map_result = list(map(lambda x: x * 2, numbers))

# Using list comprehension
list_comp_result = [x * 2 for x in numbers]

print(map_result)
print(list_comp_result)
