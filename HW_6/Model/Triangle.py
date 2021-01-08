import math

from HW_6.Model.Fugure import Fugure


class Triangle(Fugure):
    @property
    def angles(self):
        return NotImplemented

    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c

    @property
    def area(self):
        s = self.perimeter / 2.0
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c
