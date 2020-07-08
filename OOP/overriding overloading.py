class Calculator:
    """ Calculator class"""

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "It's impossible to divide by zero(0)!"

    """
    #method overloading
    def addition(self,a,b,c):
        return a+b+c*10
    """


class SuperCalculator(Calculator):
    """ SuperCalculator class"""

    # method overriding
    def addition(self, a, b, c):
        return a + b + c

    def square(self, a):
        return a ** 2

    def cube(self, a):
        return a ** 3


cal = SuperCalculator()

temp = cal.addition(1, 1, 1)
print(temp)
