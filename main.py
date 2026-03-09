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



                # Task  3. Simple Class and Inheritance

# Define the Person class + greet() method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print (f"Hello, my name is {self.name} and I am {self.age} years old.")

# Define the Student class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

# Define the main script and student object

student_object = Student("Slim Shady", 27, 42)
student_object.greet()

print(f"My student ID is:", student_object.student_id)



                # Task 1. File to List Converter

# Ask for input and clean
filename = input("Please enter a file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    clean_list = [line.strip() for line in lines]

    print(clean_list)

    print(f"Displaying file content as a list: {clean_list}")

# Put in exceptions
except FileNotFoundError:
    print(f"File {filename} does not exist or wasn´t found. Please try again.")
except Exception as e:
    print(f"Something went wrong, sorry {e}")

