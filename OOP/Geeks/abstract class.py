from abc import ABCMeta, abstractmethod


class Shape(metaclass= ABCMeta):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def message(self):
        print("This is a class")


r = Rectangle(12,5)

r.message()
print("The area is:", r.area())
