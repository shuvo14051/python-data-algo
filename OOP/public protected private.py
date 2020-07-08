class Car:
    wheel = 5
    def __printWheel(self):
        print("The number of wheel:", self.wheel)


class A(Car):
    pass

a = A()

a.__printWheel()