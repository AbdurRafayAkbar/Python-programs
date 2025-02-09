my_list=[]
total_length=int(input("Enter Total length of list : "))
for i in range(1,total_length+1):
    numbers=int(input("Enter numbers to add in list : "))
    my_list.append(numbers)
print(my_list)
prime_list=[]
for letters in my_list:
    for i in range(2,letters+1):
        if letters%i==0:
            break
        else:
            prime_list.append(letters)

print(f'Prime numbers are {prime_list}')
