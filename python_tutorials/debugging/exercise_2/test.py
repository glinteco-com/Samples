import unittest

from lib import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        numbers = [1, 2, 3, 2, 4, 3, 5]
        expected_result = [1, 2, 3, 4, 5]
        result = remove_duplicates(numbers)
        self.assertEqual(result, expected_result)

    def test_remove_duplicates_with_duplicates_only(self):
        numbers = [1, 1, 1, 1, 1, 1]
        expected_result = [1]
        result = remove_duplicates(numbers)
        self.assertEqual(result, expected_result)

    def test_remove_duplicates_with_empty_list(self):
        numbers = []
        expected_result = []
        result = remove_duplicates(numbers)
        self.assertEqual(result, expected_result)

    def test_remove_duplicates_with_no_duplicates(self):
        numbers = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        result = remove_duplicates(numbers)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
