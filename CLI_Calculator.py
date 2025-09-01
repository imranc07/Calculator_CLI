# Problem Statement 
""" 
Build a simple command line calculator that performs basic arithmatic:
addition, substraction, multiplication, and division

"""

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error: Division by zero"
    return x/y

print("=== Simple Calculator ===")
print("Choose operation:")
print("1. Add (+)")
print("2. SUbtract (-)")
print("3. Mulriply (*)")
print("4. Divide (/)")

op = input("Enter the your choice (+,-,*,/):")
a = float(input("Enter First number: "))
b = float(input("Enter Second number: "))

if op == '+':
    result = add(a,b)
elif op == '-':
    result = subtract(a,b)
elif op == '*':
    result = multiply(a,b)
elif op == '/':
    result = divide(a,b)
else:
    result = "Invalid Operator"

print("Result:", result)

