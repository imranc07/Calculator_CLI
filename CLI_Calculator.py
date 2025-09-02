# Problem Statement 
"""
Build a simple command line calculator that performs basic arithmetic:
addition, subtraction, multiplication, and division
"""

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division with zero-check
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Display calculator menu
print("=== Simple Calculator ===")
print("Choose operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# Take operator choice as input
op = input("Enter your choice (+, -, *, /): ")

# Take two numbers as input from the user
a = float(input("Enter First number: "))
b = float(input("Enter Second number: "))

# Perform calculation based on user choice
if op == '+':
    result = add(a, b)
elif op == '-':
    result = subtract(a, b)
elif op == '*':
    result = multiply(a, b)
elif op == '/':
    result = divide(a, b)
else:
    result = "Invalid Operator"

# Display the result
print("Result:", result)
