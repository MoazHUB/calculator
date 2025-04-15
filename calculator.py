def addition(firstno,secondno):
    add=firstno + secondno
    return add
def subtraction(firstno,secondno) :
    minus=firstno - secondno
    return minus
def multiplication(fristno,secondno) :
    multiply=firstno * secondno
    return multiply
def division(firstno,secondno) :

    if secondno==0 :
        pass
    else:
        divide = firstno / secondno
        return divide
firstno=int(input('enter the first number'))
secondno=int(input(' enter the second number'))
operation=input('enter the function')
if operation== '+' :
    print(addition(firstno,secondno))
elif operation== '-' :
    print(subtraction(firstno,secondno))
elif operation== '*' :
    print(multiplication(firstno,secondno))
elif operation== '/' :
    print(division(firstno,secondno))
else :
    print('Error 404')
