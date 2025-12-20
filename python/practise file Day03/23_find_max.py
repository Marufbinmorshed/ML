# Find maximum number using loop
nums = [5, 12, 3, 21, 8]
max_val = nums[0]
for n in nums:
    if n > max_val:
        max_val = n
print("Max:", max_val)
