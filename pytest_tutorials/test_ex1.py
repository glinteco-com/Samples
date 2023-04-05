# Write a test for a function that returns the sum of two integers.

def add(x, y):
    return x + y


def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
