# 1. Using a For Loop Print from 2000 to 2024 - Lesson4Task1.py

for years in range(2000,2025):
    print(years)
print("====================================")

# 2. Create a List of Colors Blue, Green, Red, Pink , Black- Using a for Loop, Loop through the Colors - Lesson4Task3.py 

colors =["Blue", "Green", "Red", "Pink", "Black"]

for color in colors:
    print(color)

print("====================================")

# Using a While Loop Print from 20 to 1 - - Lesson4Task2.py

number= 20
while number>=1:
    print(number)
    number =number - 1
print("====================================")

# python functions with parameter-> se parameters as placeholders in their definition to receive input values
# Types of Parameters
    # Positional Parameters- Arguments must be passed in the same order they are defined in the function. Arguments must be passed in the same order they are defined in the function.

def greet(name,age ):
    print(f"Hello {name}, you are {age}")

greet("Alice", 25)

print("====================================")

    #Keyword Arguments- You can call a function by explicitly naming each parameter. This allows you to pass arguments in any order.
greet(age=25, name="Alice")

print("====================================")

    #Default Parameters-You can provide a fallback value if an argument isn't provided. This makes the parameter optional.





