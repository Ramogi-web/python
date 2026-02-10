#Qn 1: Function Without Parameters 
#Create a function that: 
#• Takes no parameters 
#• Uses arithmetic operators to calculate the area of a rectangle • Prints the result 

def area():
    l=40
    w=30
    area=l*w
    print("area=", area)

area()

print("==========================")
#Qn 2: Function With Parameters 
#Create a function that: 
#• Accepts two numbers as parameters 
#• Returns their sum, difference, product, and division

def result(x,y):
    sum = x + y
    difference= x - y
    product= x * y
    quocient= x / y
    print(f"sum",sum)
    print(f"difference", difference)
    print(f"product", product)
    print(f"division",quocient)

result(6,2)

print("==========================")

#Qn 3: Control Statement (if...elif...else) 
#Write a function that: 
#• Accepts a number (use input function) 
#• Checks whether the number is: 
#• Positive 
#• Negative 
#• Zero

number=int(input("Enter number:"))

if number >0:
    print("positive")
elif number <0:
    print("negative")
else :
   print("zero")

print("==========================")


#Qn 4: Loop with Arithmetic 
#Write a function that: 
#• Accepts a number n 
#• Uses a for loop 
#• Calculates the sum of numbers from 1 to n

def sum_up_to(n):
    total = 0
    # We use n + 1 because range is exclusive of the stop number
    for i in range(1, n + 1):
        total += i
    return total

print("==========================")

#Qn 5: While Loop 
#Write a function that: 
#• Accepts a number (Use input() function) 
#• Uses a while loop 
#• Calculates the square of numbers from 1 up to that number

def calculate_squares():
    # Accept user input and convert to integer
    limit = int(input("Enter a number: "))
    
    # Initialize the starting point
    current_number = 1
    
    print(f"Squares from 1 to {limit}:")
    
    # Use a while loop to iterate until the limit is reached
    while current_number <= limit:
        square = current_number ** 2
        print(f"{current_number} squared is: {square}")
        
        # Increment the counter to avoid an infinite loop
        current_number += 1

# Call the function
calculate_squares()



   

