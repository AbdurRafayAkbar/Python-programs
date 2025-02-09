class Mamal:
    def walk(self):
        print("walk")


class Dog(Mamal):
    def bark(self):
        print("Bark")

class Cat(Mamal):
    pass


obj=Dog
obj.bark()
obj.walk()  # ye function Mamal sy mila ha

