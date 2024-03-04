

num1 = int(input("Please enter the first number: \n"))
num2 = int(input("Please enter the second number: \n"))

def add(x, y):
    return x + y

def subtract(x, y):
    if x > y:
        return x - y
    else:
        print("SYNTAX ERROR")

def multiply(x, y):
    return x * y

def divide(x, y):
    if y > 0:
        return x / y
    else:
        print("SYNTAX ERROR")

def calculate(num1, num2):
    operand = int(input("Please Choose operand: \n--------------------\n1.addition\n2.subtraction\n3.multiplication\n4.division\n"))

    if operand == 1:
        answer = add(num1, num2)
    elif operand == 2:
        answer = subtract(num1, num2)

    elif operand == 3:
        answer = multiply(num1, num2)

    elif operand == 4:
        answer = divide(num1, num2)
    else:
        print("Invalid Choice")

    print("The result is: ", answer)

if __name__ == "__main__":
    calculate(num1, num2)