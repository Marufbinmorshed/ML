# Number guessing simulation
secret = 7
for guess in range(1, 11):
    if guess == secret:
        print("Guessed correctly:", guess)
        break
