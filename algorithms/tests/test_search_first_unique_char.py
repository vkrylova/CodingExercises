import unittest

from algorithms.searching.search_first_unique_char import search_first_unique_char


class TestSearchFirstUniqueChar(unittest.TestCase):

    def test_unique_at_start(self):
        # Test when the first character is unique
        self.assertEqual(search_first_unique_char("good"), 0) # 'g' is the first unique character

    def test_unique_at_middle(self):
        # Test when a unique character is in the middle
        self.assertEqual(search_first_unique_char("ssttreet"), 4) # 'r' is the first unique character

    def test_no_unique(self):
        # Test when there are no unique characters
        self.assertEqual(search_first_unique_char("aabbcc"), -1)  # no unique character exists

    def test_single_character(self):
        # Test when the string has only one character
        self.assertEqual(search_first_unique_char("x"), 0) # the single character is unique

    def test_empty_string(self):
        # Test am empty string
        self.assertEqual(search_first_unique_char(""), -1) # no characters, so return -1

    def test_unique_at_the_end(self):
        # Test when the unique character is at the end of the string
        self.assertEqual(search_first_unique_char("aabbcd"), 4) # 'c' is the first unique character

    def test_all_unique(self):
        # Test when all characters are unique
        self.assertEqual(search_first_unique_char("abcdefg"), 0) # the first character is unique

    def test_repeated_characters_with_unique(self):
        # Test a string with repeated characters and one unique character
        self.assertEqual(search_first_unique_char("aaabcccdeeef"), 3) # 'b' is the first unique character