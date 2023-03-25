import unittest

from lib import find_divisible


class TestFindDivisible(unittest.TestCase):
    def test_divisible_by_2(self):
        result = find_divisible([1, 2, 3, 4, 5, 6], 2)
        self.assertEqual(result, [2, 4, 6])

    def test_divisible_by_3(self):
        result = find_divisible([1, 2, 3, 4, 5, 6], 3)
        self.assertEqual(result, [3, 6])

    def test_divisible_by_5(self):
        result = find_divisible([1, 2, 3, 4, 5, 6], 5)
        self.assertEqual(result, [5])

    def test_no_divisible_numbers(self):
        result = find_divisible([1, 3, 7, 9], 2)
        self.assertEqual(result, [])

    def test_empty_list(self):
        result = find_divisible([], 3)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
