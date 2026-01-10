def wrapper(func):
    def inner():
        print("Before function")
        func()
        print("After function")
    return inner

@wrapper
def say_hi():
    print("Hi!")

say_hi()
