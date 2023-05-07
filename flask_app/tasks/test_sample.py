import pytest

from .sample import add_numbers


@pytest.mark.parametrize(
    "number1,number2,expected_result", [(1, 2, 3), (2, 6, 8), (9, 2, 11)]
)
def test_add_numbers(number1, number2, expected_result):
    calculated_result = add_numbers(number1, number2)
    assert calculated_result == expected_result
