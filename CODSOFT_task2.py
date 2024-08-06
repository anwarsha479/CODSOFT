def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
def calculate(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    else:
        return "Invalid operation"
def calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        result = calculate(num1, num2, operation)
        print(f"The result is: {result}")
if __name__ == "__main__":
    calculator()
