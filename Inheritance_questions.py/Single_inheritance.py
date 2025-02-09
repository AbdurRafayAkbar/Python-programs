# Create a base class Animal with a method speak(), and a derived class Dog that overrides the speak() method to print "Bark".

class Animal:
    def speak(self):
        return "Sound "
    

class Dog(Animal):
    def speak(self):
        return "BARK"
    
d=Dog()
print(d.speak())
