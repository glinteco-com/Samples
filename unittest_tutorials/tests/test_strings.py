import unittest

from libs.strings import count_e_letters


class TestCountELetters(unittest.TestCase):
    def test_count_e_letters_with_a_string(self):
        count = count_e_letters("Joe")
        self.assertEqual(1, count)

    def test_count_e_letters_with_a_none_input(self):
        count = count_e_letters(None)
        self.assertEqual(0, count)
