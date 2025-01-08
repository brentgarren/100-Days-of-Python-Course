def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def operator_select(n1, n2, operator):
    if operator == "+":
        return add(n1, n2)
    elif operator == "-":
        return subtract(n1, n2)
    elif operator == "*":
        return multiply(n1, n2)
    elif operator == "/":
        return divide(n1, n2)

def get_num1():
    return int(input(f"What is your first number? "))

def get_num2():
    return int(input(f"What is your second number? "))

operators = ["+", "-", "*", "/"]
calculator = True
n1 = get_num1()

while calculator:
    for symbol in operators:
        print(symbol)
    operator = input(f"Pick an operation: ")
    n2 = get_num2()
    n3 = operator_select(n1, n2, operator)

    print(f"{n1} {operator} {n2} = {n3}")
    choice = input(f"Type 'y' to continue calculating with {n3}, or type 'n' to start a new calculation: ")
    
    if choice == "n":
        n1 = get_num1()  # Start a new calculation by getting a new n1
    elif choice == "y":
        n1 = n3  # Continue calculating with the current result
    else:
        calculator = False  # Stop the calculator if input is not 'y' or 'n'
