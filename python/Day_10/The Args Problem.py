def wrapper(func):
    def inner(*args, **kwargs):
        print("Before function")
        return func(*args, **kwargs)
    return inner

@wrapper
def add(a, b):
    return a + b

print(add(5, 7))
