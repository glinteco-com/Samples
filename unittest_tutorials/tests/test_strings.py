import unittest

from libs.strings import count_e_letters, is_palindrome


class TestCountELetters(unittest.TestCase):
    def test_count_e_letters_with_a_string(self):
        count = count_e_letters("Joe")
        self.assertEqual(1, count)

    def test_count_e_letters_with_a_none_input(self):
        count = count_e_letters(None)
        self.assertEqual(0, count)


class TestIsPalindrome(unittest.TestCase):
    def test_return_true(self):
        result = is_palindrome("malayalam")
        self.assertTrue(result)

    def test_false(self):
        result = is_palindrome("Joe")
        self.assertFalse(result)

    def test_raise_exception(self):
        with self.assertRaises(Exception):
            is_palindrome(123)
