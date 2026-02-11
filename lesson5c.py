# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

def si(p,r,t):
    si=p*r*t/100
    print(f"si",si)

si(12000, 7, 2)

# Each list is [Principal, Rate, Time]
other_rounds = [[1000, 5, 2], [5000, 10, 3]]

for data in other_rounds:
    si(data[0], data[1], data[2])
