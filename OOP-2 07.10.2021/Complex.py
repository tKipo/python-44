class Complex:

    def __init__(self, a, b):
        self.complex1 = a
        self.complex2 = b


class Oper(Complex):

    def __add__(self):
        return self.complex1 + self.complex2

    def __sub__(self):
        return self.complex1 - self.complex2

    def __mul__(self):
        return self.complex1 * self.complex2

    def __divmod__(self):
        return self.complex1 / self.complex2


class Abs(Complex):

    def __abs__(self):
        return abs(self.complex1), abs(self.complex2)


r = Oper(22 + 2j, 2 + 3j)
d = Abs(1+2j, 2+2j)
print(r.__mul__())
print(d.__abs__())
