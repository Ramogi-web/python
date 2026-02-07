# Adictionary is a data type that stores data in terms of key -value pair
# It is introduced introduced by the use of curly braces{}
# The values stored inside of a dictionary can be of any data type
#To access the value in a dictionary we use the keys


phonebook ={
    "Benson": "2547234567",
    "Mary": "2540987654",
    "Stephen":"254987654"
}

#showing the entire dictionary
print(phonebook)
print(type(phonebook))

#print out Bensons number
print(phonebook["Benson"])

print('==========================')

player ={
    "name" :"Messi",
    "age" : 40,
    "teams":["PSG", "Barcelona" ,"Argentina"],
    "more":{
        "children" : 3,
        "residence": "US",
        "phone" : (254774542, 254765344, 25476531)
    }
}

#print barcelona 
print(player["teams"][1])
print("Messi's second number:", player["more"]["phone"][1])