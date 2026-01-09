def receiver():
    value = yield
    while True:
        value = yield value * 2

gen = receiver()
next(gen)          # Prime the generator

print(gen.send(10))
print(gen.send(5))
