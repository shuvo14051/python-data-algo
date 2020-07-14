class Base1:
    def __init__(self):
        self.name = "Base Class 1"
        print(self.name)

class Base2:
    def __init__(self):
        self.age = "Base Class 2"
        print(self.age)

class Derived(Base1):
    def __init__(self):
        Base2.__init__(self)
        Base1.__init__(self)
        print("Derived class")

    def printStrs(self):
        print(self.name, self.age)


obj = Derived()
obj.printStrs()
