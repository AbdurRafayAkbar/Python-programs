while True:
    def palyndrome():
        text=str(input("Enter Text : "))
        if text==text[::-1]:
            print(f'The {text} is Palyndrome ')
        else:
            print("Not Palyndrome")
    palyndrome()

