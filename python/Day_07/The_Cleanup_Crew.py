a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
 print(a / b)
except Zero Division:
    print("Division by zero is not allowed")
except Value Error:
    print("Please enter valid numbers")
finally:
    print("Execution Complete")

