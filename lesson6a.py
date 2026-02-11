# python modules 
# A python module is a file that contains python definations,statements and/or functions.


def add():
    num1 = 20
    num2 = 30
    sum = num1 + num2
    print("The answer is", sum)


def subtract():
    x =45
    y =30
    difference = x - y
    print("The difference is:", difference)

# These functions defined above on this particular file  they can be called into another file

def rectangle_area():
    length=int(input("Enter the length of the rectangle:"))
    width=int(input("Enter the width of the rectangle:"))
    area = length * width
    print("The area of the rectangle is:", area)