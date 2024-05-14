import source.shapes as shapes
import pytest

def test_my_rectangle(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    assert my_rectangle.area() == 10 * 20

def test_perimeter(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    assert my_rectangle.perimeter() == 10 * 2 + 20 * 2

def test_eq(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    another_same_rectangle = rectangle_factory(10,20)
    assert my_rectangle == another_same_rectangle

def test_ne(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    another_diff_rectangle = rectangle_factory(30,45)
    assert my_rectangle != another_diff_rectangle


