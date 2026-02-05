#Tuple
#A tuple is an immutable type of a list (It cannot change)
# To introduce a tuple we use the parenthesis

counties =  ("Nairobi", "Mombasa", "Nakuru","Eldoret", "Kajiado", "Kissi")
print(counties)
print(type(counties))

#slicing of tuples
print(counties[3:])

# Accesssing items by use of indexes
print(counties[5])

#Note :Below will generate an error
#Attribute error
counties.append("Machakos")
print(counties)