import math
def fibonacci():
    num=int(input("Enter number : " ))
    if num<=0:
        print("Invalid Input! The number should be Positive")
    elif num==1 or num==2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
fibonacci()
