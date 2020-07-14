class Parent:
    def __init__(self,name):
        self.name = name
        print("Inside parent class:" + self.name)

class Child(Parent):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
        print("Inside child class:" + self.name)





a = Child("husp")
