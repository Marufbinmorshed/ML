def gen_a():
    yield 1
    yield 2

def gen_b():
    yield 3
    yield 4

def main_gen():
    yield from gen_a()
    yield from gen_b()

for x in main_gen():
    print(x)

