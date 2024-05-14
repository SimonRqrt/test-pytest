import math
import pytest

import source.shapes as shapes

def test_not_the_same_area(my_circle, my_rectangle):
    assert my_circle.area() != my_rectangle.area()