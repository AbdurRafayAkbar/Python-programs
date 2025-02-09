factorial=1
number=int(input("Enter a number to Check : "))
for i in range(1,number+1):
    factorial*=i
print(factorial)