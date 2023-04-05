# Write a test for a function that raises an exception when given an empty list as input.
import pytest


def find_max(a_list):
    return max(a_list)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max([])
