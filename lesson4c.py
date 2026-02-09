# For loop can also be used to iterate through a list, tuple, string or even a dictionary.

name = "Ramogi"

for letter in name:
    if letter== "m":
        print("the letter is m")
    else:
        print(letter)

print("===================")

#below is a list of counties

counties = ["Nairobi","Mombasa", "Kisumu","Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)

print("===================")

for county in counties:
    if county == "Nairobi":
        print("County is part of the list")
        break
    else:
        print("county is not part of the list")
print("===================")

#the for loop can also be used to iterate through a dictionary

player={
    "name":"Mbappe",
    "age":25,
    "teams":["PSG","Monaco","France"],
    "nationality":"Frech"
}

for key in player:
    print(key)

print("===================")

for value in player:
    print(player[value])

print("===================")
#loop through the teams the player has played for

for team in player:
    print(player["teams"])

for team in player["teams"]:
    print(team)
