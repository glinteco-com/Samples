# Write a test for a function that converts a temperature from Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32


def test_temperature_conversion():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
