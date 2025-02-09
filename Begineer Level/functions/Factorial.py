def factorial(num):
    # num=int(input("Enter number : "))
    if num ==0 and num==1:
        print(f"Write Number other than {num}")
    else:
        return num * factorial(num-1)

factorial(4)
