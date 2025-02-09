# def sum_squares():
#     num=int(input("Enter number to which you want the sum of squares : "))
#     for i in range(1,num+1):
#         square=((i**2))
#         print(square)
#         summ=square+i
#         print(summ)
# print(sum_squares())

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

# Example usage
print(sum_of_squares(5))  # Output: 55 (1² + 2² + 3² + 4² + 5²)
