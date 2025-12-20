# Check prime number
num = 17
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

print("Prime:", is_prime)
