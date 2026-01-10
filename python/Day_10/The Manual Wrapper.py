def wrapper(func):
    def inner():
        print("Before function")
        func()
        print("After function")
    return inner

def say_hello():
    print("Hello!")

new_func = wrapper(say_hello)
new_func()

