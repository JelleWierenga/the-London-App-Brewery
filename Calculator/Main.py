def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

result = 0

while True:
    if result == 0:
        num1 = float(input("Enter the first number: "))
    else:
        num1 = result

    operation = input("+\n-\n*\n/\nPick an operation:")
    num2 = float(input("Enter the second number: "))

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation. Please select +, -, *, or /.")
        continue

    print(f"Result: {result}")

    choice = input("Type 'y' to continue with the result, or 'n' to start a new calculation: ")
    if choice.lower() != 'y':
        result = 0
        if input("Type 'n' to stop, or any other key to continue: ").lower() == 'n':
            break
