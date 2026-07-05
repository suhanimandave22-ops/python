a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
ch = int(input("Choose an option: "))
if ch == 1:
    print("Addition:", add(a, b))
elif ch == 2:
    print("Subtraction:", sub(a, b))
elif ch == 3:
    print("Multiplication:", mult(a, b))
elif ch == 4:
    if b != 0:
        print("Division:", div(a, b))
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid Choice")

print("Thank you")