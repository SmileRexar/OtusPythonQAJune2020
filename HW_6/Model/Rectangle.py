from HW_6.Model.Fugure import Fugure


class Rectangle(Fugure):
    @property
    def angles(self):
        return NotImplemented

    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)
