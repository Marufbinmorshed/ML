# Search element in list
nums = [4, 7, 9, 2]
target = 9
found = False
for n in nums:
    if n == target:
        found = True
        break
print("Found:", found)
