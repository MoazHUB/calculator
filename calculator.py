def addition(firstno, secondno):
    return firstno + secondno

def subtraction(firstno, secondno):
    return firstno - secondno

def multiplication(firstno, secondno):
    return firstno * secondno

def division(firstno, secondno):
    if secondno == 0:
        return "Error: Cannot divide by zero"
    else:
        return firstno / secondno

# input
firstno = int(input("Enter the first number: "))
secondno = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# operation selection
if operation == '+':
    print(addition(firstno, secondno))
elif operation == '-':
    print(subtraction(firstno, secondno))
elif operation == '*':
    print(multiplication(firstno, secondno))
elif operation == '/':
    print(division(firstno, secondno))
else:
    print("Error: Invalid operation")
