import unittest

from lib import reverse_string


class TestReverseString(unittest.TestCase):
    def test_reverse_string_with_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_with_single_character_string(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_string_with_multiple_character_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_string_with_whitespace(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")


if __name__ == "__main__":
    unittest.main()
