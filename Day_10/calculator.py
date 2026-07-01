def add(a: int, b: int):
    output = a + b
    return output

def subtract(a: int, b: int):
    output = a - b
    return output

def multiply(a: int, b: int):
    output = a * b
    return output

def divide(a: int, b: int):
    output = a / b
    return output

print("Welcome to Calculator!")

a = int(input("first number: "))
o = input("Choose an operation (+, -, *, /): ")
b = int(input("second number: "))

if o == "+":
    output = add(a, b)
    print(f"{a} {o} {b} = {output}")
elif o == "-":
    output = subtract(a, b)
    print(f"{a} {o} {b} = {output}")
elif o == "*":
    output = multiply(a, b)
    print(f"{a} {o} {b} = {output}")
elif o == "/":
    output = divide(a, b)
    print(f"{a} {o} {b} = {output}")