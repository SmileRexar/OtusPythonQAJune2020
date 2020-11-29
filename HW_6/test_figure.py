import pytest

from HW_6.Model.Circle import Circle
from HW_6.Model.Fugure import Fugure, NotIsFugure
from HW_6.Model.Rectangle import Rectangle
from HW_6.Model.Square import Square
from HW_6.Model.Triangle import Triangle


@pytest.mark.parametrize("a ,b, c, area, rerimetr", [
    (10, 5, 12, 24.544602257930357, 27),
])
def test_triangle(a, b, c, area, rerimetr):
    tr = Triangle(a, b, c)
    assert tr.area == area
    assert tr.perimeter == rerimetr


@pytest.mark.parametrize("a ,b, area, rerimetr", [
    (12, 10, 120, 44),
])
def test_rectangle(a, b, area, rerimetr):
    rec = Rectangle(a, b)
    assert rec.area == area
    assert rec.perimeter == rerimetr


@pytest.mark.parametrize("a, area, rerimetr", [
    (16, 256, 64),
])
def test_square(a, area, rerimetr):
    sq = Square(a)
    assert sq.area == area
    assert sq.perimeter == rerimetr


@pytest.mark.parametrize("a, area, rerimetr", [
    (10, 314.1592653589793, 62.83185307179586),
])
def test_circle(a, area, rerimetr):
    cr = Circle(a)
    assert cr.area == area
    assert cr.perimeter == rerimetr


def test_add_area():
    a = Fugure.add_area(
        Triangle(10, 5, 12),
        Rectangle(12, 10),
        Square(16),
        Circle(10),
    )
    assert a == 714.7038676169097


def test_perimetr():
    a = Fugure.add_perimetr(
        Triangle(2, 5, 12),
        Rectangle(12, 10),
        Square(12),
        Circle(8),
    )
    assert a == 161.2654824574367


def test_raise_error():
    with pytest.raises(TypeError):
        Fugure.add_perimetr(
            Triangle(101, 2, 12),
            Rectangle(4, 10),
            Square(10),
            Circle(4),
            NotIsFugure()
        )
