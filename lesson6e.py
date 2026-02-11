# on the try and except block: you run codes /statements and if it is successful the try block will get excecuted other the except block will excecuted when there is an anticipated error
number = 100

answer = number/0

print(answer)

try:
    number =100
    answer =number /0
    print("The answer is: ",answer)
except Exception as e:
    print("There is an error: ",e)

try:
    number =100
    if number > 10:
        print("The number is greater than 10")
except Exception as e:
    print("You have an erroe on your program ",e)

