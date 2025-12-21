try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("No negatives")
    print("You entered:", num)
except ValueError as ddd:
    print("Error:", ddd)
finally:
    print("Thanks's Bro")
