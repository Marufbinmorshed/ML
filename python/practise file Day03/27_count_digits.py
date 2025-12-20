# Count digits in a number
num = 123456
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digits:", count)
