import unittest

from lib import sum_even_numbers


class TestSumEvenNumbers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_even_numbers([]), 0)

    def test_no_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 3, 5]), 0)

    def test_all_even_numbers(self):
        self.assertEqual(sum_even_numbers([2, 4, 6]), 12)

    def test_mixed_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)


if __name__ == "__main__":
    unittest.main()
