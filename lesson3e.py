# below is a grading system based on what a studet would have gotten
marks= int(input("enter student marks: "))
#print("the entered mark is ", marks)
if marks >=0  and marks <30 :
    print("below average")
elif marks>= 30 and marks<40:
    print("average")
elif marks >=40 and marks< 70:
    print("above average")
elif marks >=70 and marks <=100 :
    print("excellent")
else:
    print("invalid")
