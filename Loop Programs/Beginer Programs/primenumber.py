number=int(input("Enter a number to Check : "))
for i in range(2,number):
    if number%i==0:
        print("Not Prime Number ")
        break
    else:
        print("Prime Number")
        break