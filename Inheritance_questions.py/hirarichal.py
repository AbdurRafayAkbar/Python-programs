# Create a base class Shape with a method area(). Then, create two derived classes Rectangle and Circle that inherit from Shape and implement their own area() method.
# yhan pr main aik class ha aur us ki do sub classes hn ji different kaam krti hn
import math
class Shape:
    def area(self):
        pass

class Recatangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi *self.radius*self.radius
        
rect=Recatangle(4,7)
circle=Circle(7)
print(rect.area())
print(circle.area())
