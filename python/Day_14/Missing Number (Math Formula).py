def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)
