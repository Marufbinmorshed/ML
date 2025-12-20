# Find minimum number using loop
nums = [5, 12, 3, 21, 8]
min_val = nums[0]
for n in nums:
    if n < min_val:
        min_val = n
print("Min:", min_val)
