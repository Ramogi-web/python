income= int(input("enter gross income"))

if income >=0 and income < 5999 :
    print("monthly contribution =150.00")
elif income >=6000 and income <7999:
    print("monthly contribution =300.00")
elif income >=8000 and income <11999:
    print("monthly contribution =400.00")
elif income >=12000 and income <14999:
    print("monthly contribution =500.00")
elif income >=15000 and income <19999:
    print("monthly contribution =600.00")
elif income >=20000 and income <24999:
    print("monthly cntribution =750.00")
elif income >=25000 and income <29999:
    print("monthly contribution =850.00")
elif income >=30000 and income <49999:
    print("monthly contribution =1000.00")
elif income >=50000 and income <99999:
    print("monthly contribution =1500.00")
elif income >=100000:
    print("monthly contribution =2000.00")
else:
    print("invalid")
