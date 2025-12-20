# Number guessing game simulation
secret = 15
guesses = [5, 10, 15, 20]

for g in guesses:
    if g < secret:
        print(g, "is too small")
    elif g > secret:
        print(g, "is too large")
    else:
        print("Correct guess:", g)
        break
