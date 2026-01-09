def numbers(n):
    for i in range(n):
        yield i

def square(nums):
    for n in nums:
        yield n * n

def even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

pipeline = even(square(numbers(10)))

for value in pipeline:
    print(value)

