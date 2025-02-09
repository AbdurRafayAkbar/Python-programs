class Vehicle:
    def __init__(self,name,model):
        self.name=name
        self.model=model

class Car_type(Vehicle):
    def __init__(self,name,model,type):
        super().__init__(name,model)
        self.type=type
        
class Wheel_type(Car_type):
    def __init__(self, name, model, type,wheel_type):
        super().__init__(name, model, type)
        self.wheel_type=wheel_type
    def show(self):
        print("| Vehicle Name | Vehicle Model | Vehicle Type | Wheel Type |")
        print(f"|{self.name}         | {self.model}          |{self.type}      | {self.wheel_type}          | ")  
obj=Wheel_type("Tesla",2024,"Electric",4)
obj.show()
