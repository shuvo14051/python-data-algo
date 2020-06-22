class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

mt_f = Fraction(3,5)
print(mt_f)
