from calculator import *

def get_user_input():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    return num1, num2, operator

def perform_operation(num1, num2, operator):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        raise ValueError("Invalid operator!")

def display_result(result):
    print("Result:", result)
