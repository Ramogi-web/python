#python functions
# They are a block of cord/statements that performs a given task/action. They can be reused through out the process to perform different tasks.
# functions are defined using the def keyword.(define)
# we have two main types of functions:
    #1.  In-built functions -> They come preinstalled with the interpreter i.e print(), pop(), range(), append() etc...
    # 2. User defined functions => They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis.
# For the functions, it is usually indented and to invoke a function we use the function name.

def greeting():
    print("Hello ,how are you?")

#below we call the function by use of its name
greeting()

print("==================================")

# Addition function

def addition():
    num1 = 40
    num2 =50
    sum = num1 + num2
    print ("the sum of the numbers is", sum)

addition()
 
print("==================================")

 # create a function that  is able to multiply three values

def multiplication():
    num1 =4
    num2 =5
    num3 =9
    product =num1 * num2 *num3
    print("the product is",product)

multiplication()

print("==================================")
# below is a division function

def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient =number1 / number2
    print("The answer is: ",quotient)
    print("-----------------")
print("---Starting 3 rounds of division.. ---")

for function in range(3):
    divide()




