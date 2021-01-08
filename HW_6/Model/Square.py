from HW_6.Model.Fugure import Fugure


class Square(Fugure):
    @property
    def angles(self):
        return NotImplemented

    def __init__(self, a):
        super().__init__(a)

    @property
    def area(self):
        return self.a ** 2

    @property
    def perimeter(self):
        return 4 * self.a
