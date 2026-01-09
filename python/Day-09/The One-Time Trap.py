def numbers():
    for i in range(3):
        yield i

g = numbers()

for x in g:
    print(x)

print("Second loop:")
for x in g:
    print(x)   # Nothing will print
