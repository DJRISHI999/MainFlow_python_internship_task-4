# The intern will build a simple command-line calculator application in Python.

# Design the user interface for the calculator using Python's input function.
# Implement the calculator operations such as addition, subtraction, multiplication, and division.
# The calculator should be able to handle invalid inputs gracefully.

class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return 'Cannot divide by zero'
        return num1 / num2

    def run_calculator(self):
        print('Welcome to the Calculator App!')
        print('Enter the operation you want to perform:')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')

        operation = input('Enter the operation number (1/2/3/4): ')

        if operation not in ['1', '2', '3', '4']:
            print('Invalid operation. Please enter a valid operation number.')
            return

        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))

        if operation == '1':
            result = self.add(num1, num2)
            print(f'The result of addition is: {result}')
        elif operation == '2':
            result = self.subtract(num1, num2)
            print(f'The result of subtraction is: {result}')
        elif operation == '3':
            result = self.multiply(num1, num2)
            print(f'The result of multiplication is: {result}')
        elif operation == '4':
            result = self.divide(num1, num2)
            print(f'The result of division is: {result}')

        print("Creator: Dhruv Kumar Jaiswal")

# Create an instance of the Calculator class and run the calculator application.
calculator = Calculator()
calculator.run_calculator()
