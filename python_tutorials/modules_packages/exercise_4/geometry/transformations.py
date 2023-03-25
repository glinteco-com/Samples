# transformations.py module
import math


def rotate(width, height, angle):
    return (
        width * math.cos(angle) - height * math.sin(angle),
        width * math.sin(angle) + height * math.cos(angle),
    )


def translate(x, y, dx, dy):
    return (x + dx, y + dy)
