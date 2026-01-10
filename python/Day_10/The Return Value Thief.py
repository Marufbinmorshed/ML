def wrapper(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner

@wrapper
def multiply(a, b):
    return a * b

print(multiply(3, 4))
