class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def details(self):
        return (f'Name : {self.name}, Age : {self.age}')
    

class Employee(Person):
    def __init__(self, name, age,emp_id,salary):
        super().__init__(name, age)
        self.emp_id=emp_id
        self.salary=salary

    
    def details(self):
        print (f"{super().details()}, Employee ID : {self.emp_id}, Salary : {self.salary}")

def get_employee_details():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = int(input("Enter Employee ID: "))
    salary = float(input("Enter Salary: "))
    return Employee(name, age, emp_id, salary) 

Employee1=get_employee_details()
Employee1.details()

    