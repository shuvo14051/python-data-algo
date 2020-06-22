class MyClass:

    #example of @classemethod decorator
    def __init__(self):
        pass

    def square(self, x):
        return x**2

    @classmethod
    def cube(self,x):
        return x**3

if __name__ == "__main__":
    obj = MyClass()
    print(obj.square(12))
    print(obj.cube(2))
    print(MyClass.cube(4))
    try:
        print(MyClass.square(12))
    except TypeError:
        print("It's not a class method. It can't be called via the class")

