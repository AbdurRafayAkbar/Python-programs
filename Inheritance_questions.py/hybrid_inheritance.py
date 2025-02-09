class Employee:
    def showEmployee(self):
        print("I am Employee")
    
class Manager(Employee):
    def showManager(self):
        print("I am manger")

class Developer(Employee):
    def showDeveloper(self):
        print("I am Developer")

class TeamLead(Manager,Developer):
    def showTeamLead(self):
        print("This is a team lead")

obj=TeamLead()
obj.showTeamLead()
obj.showManager()
obj.showDeveloper()
obj.showEmployee()

print(TeamLead.mro())