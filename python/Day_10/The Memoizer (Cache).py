def cache(func):
    memo = {}
    def inner(n):
        if n in memo:
            return memo[n]
        memo[n] = func(n)
        return memo[n]
    return inner

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
