# Loops -> sometimes we may need to aply a piece of work a number of repeated times in such a case we may use a loops
#a loop

#Below is a syntax of a for loop:
"""
for variable in range(n):
   # block of code to be executed 
"""
for greeting in range(5):
    print("Hello Moses", greeting)

print("========================")

for number in range(10,20):
    print(number)


print("===============================")

#find the even numbers in the range of 50 to 71
for number in range(50, 71, 2):
    print(number)

print("===============================")
# create apython program that prints the odd numbers from 100 to 150

for number in range(101 ,150, 2 ):
    print(number)

print("===============================")

# create a program that prints the multiples of 3 starting from 201 to 150
for number in range(201 ,149, -3 ):
    print(number)

print("===============================")

# create a python program that prints the leap years in between 2000 and 2024
for year in range(2000, 2025 , 4 ):
    print(year)

