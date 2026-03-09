                # Task 8. Simple Calculator Module

import calculator

# Ask for user input and handle division by zero

try:
    number1 = float(input("Hi there. Please enter a first number: "))
    number2 = float(input("Please enter a second number: "))
    operation = input("Please enter the type of operation to execute (+, -, * or /): ")

    result = None

    if operation == "+":
        result = calculator.add(number1, number2)
    elif operation == "-":
        result = calculator.subtract(number1, number2)
    elif operation == "*":
        result = calculator.multiply(number1, number2)
    elif operation == "/":
        result = calculator.divide(number1, number2)

    else:
        result = None
        print("Sorry, this is not a valid operation!")

    if result is not None:
        print(f"The result:", result)

except ZeroDivisionError:
            print("Sorry, you can't divide by zero!")
except ValueError:
    print("Sorry, this is not a valid number!")
