# Write a test for a function that calculates the factorial of a positive integer.

def factorial(x):
    fact = 1
 
    for i in range(1, x+1):
        fact = fact * i

    return fact


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
