from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    n1 = float(input("Enter the first number:\n"))
    cont = True
    while cont:
        op = input("Enter the operation to be performed:\n+\n-\n*\n/\n")
        n2 = float(input("Enter the second number:\n"))
        result = operations[op](n1,n2)
        print(f"{n1} {op} {n2} = {result}")
        go = input(f"Type y to keep going with {result} or type n to start a new calculation\n").lower()
        if go == "y":
            n1 = result
        if go == "n":
            cont = False
            calculator()

calculator()