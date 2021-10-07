import math
import sys

class NDot:

    def __init__(self, a, b):
        '''Вводим координаты первой точки'''
        self.first = a
        '''Вводим координаты второй точки'''
        self.second = b

    def checking_all(self):
        if len(self.first) == len(self.second):
            print('Equality - passed')
        else:
            print('Equality - failed')
            sys.exit()
        if ''.join(map(str, self.first)).isdigit() and ''.join(map(str, self.first)).isdigit() is True:
            print('Digit - passed')
        else:
            print('Digit - failed')
            sys.exit()


class Pifagor(NDot):
    def pifo(self):
        n = len(self.first)
        i = 0
        y = 0
        while n > 0:
            y += (self.first[i] - self.second[i]) ** 2
            i += 1
            n -= 1
        return math.sqrt(y)


class FromZero(Pifagor):
    def fromzerocount(self):
        n = len(self.first)
        i = 0
        y = 0
        q = 0
        while n > 0:
            y += (0 - self.first[i]) ** 2
            q += (0 - self.second[i]) ** 2
            i += 1
            n -= 1
        return math.sqrt(y), math.sqrt(q)


k = Pifagor((1, 3423, 3, 4), (1, 3, 4, 5, 9))
d = FromZero((1, 2, 3, 4), (1, 3, 4, 5))
k.checking_all()
print(f'Расстояние между точками: {k.pifo()}')
print(f'Расстояние от начала координат до точек: {d.fromzerocount()}')

