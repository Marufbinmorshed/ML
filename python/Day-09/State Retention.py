def running_average():
    total = 0
    count = 0
    while True:
        num = yield
        total += num
        count += 1
        yield total / count

avg = running_average()
next(avg)

print(avg.send(10))
next(avg)
print(avg.send(20))
next(avg)
print(avg.send(30))
