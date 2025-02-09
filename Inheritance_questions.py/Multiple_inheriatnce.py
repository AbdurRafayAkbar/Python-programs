#Create two base classes Person and Employee. The Employee class should inherit from Person.

class Person:
    def __init__(self,name,id):
        self.name= name     
        self.id=id
       
class Employee(Person):
    def __init__(self,name,id,bps):
        super().__init__(name,id)
        self.bps=bps
    def showEmploy(self):
        print(f"The name of Employee is {self.name} and its id is {self.id} Basic pay scale is {self.bps}")
        
e=Employee("AbdurRafay",2,14)

e.showEmploy()