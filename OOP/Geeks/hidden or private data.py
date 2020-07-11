class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 10

    # A member method that changes
    # __hiddenVariable

    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)


obj = MyClass()

obj.add(2)
obj.add(2)

# This line causes error
print (myObject.__hiddenVariable)

print(obj._MyClass__hiddenVariable)

    