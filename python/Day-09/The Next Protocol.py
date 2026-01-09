def gen():
    yield 10
    yield 20

g = gen()

try:
    while True:
        print(next(g))
except StopIteration:
    print("Generator finished")

