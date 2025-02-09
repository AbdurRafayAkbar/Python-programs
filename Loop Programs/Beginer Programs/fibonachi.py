# fibonacci series= 0,1,1,2,3,5,7...
# 0,1,1+0,1+1,2+1,3+2,5+3,7+5.... 
number=int(input("Enter the number : "))
a=0
b=1
print(a)
print(b)
for i in range(2,number):
    c=a+b
    a=b
    b=c
    print(c)

