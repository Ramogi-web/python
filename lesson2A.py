#python lists
#A list in python is a collection of items that ordered in a certain way.
#A  list is introduced by the use of the square brackets []
#The items arestored inside of the indexes. Note:In programming we start counting from index zero(0).bmw, benze, hiace,...
# A list is mutable ie the content of a list can be changed


cars =["BMW", "Benze", "Hiace","Prado", "Probox", "Mclarel", "Range"]

print(cars)
print(type(cars))

#Accessing items of a list
print(cars[2])
print("The car on index four is", cars[4])

# List slicing - This is creating a list from a given bigger list
print(cars[4:])

#printingfrom index 0-3
print(cars[0:4])

#printing from hiace to probox
print(cars[2:5])

# List-Mutability
# we use the function append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

# we use a pop function to remove an item from the end of the list
cars.pop()
print(cars)

# we can use an index to add an aitem to the list
cars[5]= "Pajero"
print(cars)

#we can use the sort function to sort items in an alphabetical order
cars.sort()
print(cars)

# we can use the sort function to sort out items in alphabetical order
cars.sort(reverse=True)
print(cars)

del cars[4]
print(cars)

cars.pop(4)
print(cars)

cars.remove("BMW")
print(cars)