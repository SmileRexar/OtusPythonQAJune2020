from abc import abstractmethod, ABC


class Fugure(ABC):
    size_s = 0
    size_p = 0

    def __init__(self, a):
        self.a = a
        self.name = type(self).__name__

    @property
    @abstractmethod
    def area(self):
        return NotImplemented

    @property
    @abstractmethod
    def angles(self):
        return NotImplemented

    @property
    @abstractmethod
    def perimeter(self):
        return NotImplemented

    @staticmethod
    def add_area(*argv):
        a = 0
        for _ in argv:
            if not isinstance(_, Fugure):
                raise TypeError(f"класс {_} не производный от {Fugure}")
            # print(f'Фигура = {_.name:20s} площадь = {_.area}')
            a += _.area
        size_s = a
        # print(f"Общая площадь {size_s}")
        return size_s

    @staticmethod
    def add_perimetr(*argv):
        a = 0
        for _ in argv:
            if not isinstance(_, Fugure):
                raise TypeError(f"класс {_} не производный от {Fugure}")

            print(f'Фигура = {_.name:20s} периметр = {_.perimeter}')
            a += _.perimeter
        size_p = a
        print(f"Общий периметр {size_p}")
        return size_p


class NotIsFugure:
    pass

# class Circle(Fugure):
#     @property
#     def angles(self):
#         return NotImplemented
#
#     def __init__(self, radius):
#         super().__init__(0)
#         self.radius = radius
#
#     @property
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#     @property
#     def perimeter(self):
#         return 2 * self.radius * math.pi


# class Rectangle(Fugure):
#     @property
#     def angles(self):
#         return NotImplemented
#
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
#     @property
#     def perimeter(self):
#         return 2 * (self.a + self.b)


# class Square(Fugure):
#     @property
#     def angles(self):
#         return NotImplemented
#
#     def __init__(self, a):
#         super().__init__(a)
#
#     @property
#     def area(self):
#         return self.a ** 2
#
#     @property
#     def perimeter(self):
#         return 4 * self.a


# class Triangle(Fugure):
#     @property
#     def angles(self):
#         return NotImplemented
#
#     def __init__(self, a, b, c):
#         super().__init__(a)
#         self.b = b
#         self.c = c
#
#     @property
#     def area(self):
#         s = self.perimeter / 2.0
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
#
#     @property
#     def perimeter(self):
#         return self.a + self.b + self.c
