# main.py script
import math

import geometry.shapes as shapes
import geometry.transformations as trans

width, height = 5, 3
angle = math.pi / 2
dx, dy = 2, 1

area = shapes.area(width, height)
perimeter = shapes.perimeter(width, height)
print(f"The area of a rectangle with width {width} and height {height}")

rotate_value = trans.rotate(width, height, angle)
print(f"the rotate value is {rotate_value}")
