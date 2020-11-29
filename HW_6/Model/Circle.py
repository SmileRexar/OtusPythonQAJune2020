import math

from HW_6.Model.Fugure import Fugure


class Circle(Fugure):
    @property
    def angles(self):
        return NotImplemented

    def __init__(self, radius):
        super().__init__(0)
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * self.radius * math.pi
