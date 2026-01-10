import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Running function")
        return func()
    return wrapper

@my_decorator
def greet():
    """This is greet function"""
    print("Hello!")

print(greet.__name__)
print(greet.__doc__)
