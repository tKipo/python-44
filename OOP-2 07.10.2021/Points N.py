class Point:
    def __init__(self, *args):
        [int(x) for x in args]
        self.choords = args

    def __abs__(self):
        return sum([x ** 2 for x in self.choords]) ** 0.5

    @property
    def shape(self):
        return len(self.choords)


class Line:

    def __init__(self, first_point, second_point):
        self.point1 = Point(*first_point)
        self.point2 = Point(*second_point)
        assert self.point1.shape == self.point2.shape

    def __abs__(self):
        return sum(
            [(x - y) ** 2
             for x, y in zip(
                self.point1.choords, self.point2.choords
            )
             ]
        ) ** 0.5

    def to_null(self):
        a = [
            (x * 0, y - x)
            for x, y in zip(
                self.point1.choords, self.point2.choords
            )
                ]
        point1, point2 = zip(*a)
        return point1, point2


l = Line((1, 2, 3, 4), (1, 3, 4, 5))
print(abs(l))
p = Point(1, 2, 3, 4)
print(abs(p))
print(l.to_null())

