import time

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return inner

@timer
def slow_function():
    time.sleep(1)

slow_function()

