class Person():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):
    def __init__(self, name, eid):
        super().__init__(name)
        self.eid = eid

    def isEmployee(self):
        return True

    def getID(self):
        return self.eid


emp = Employee("Geek1", "E101")
emp2 = Employee("Fut", "007")
print(emp.getName(), emp.isEmployee(), emp.getID())
