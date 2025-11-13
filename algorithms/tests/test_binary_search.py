import unittest

from algorithms.searching.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_single_element_no_match(self):
        self.assertEqual(binary_search([1], 12), -1)

    def test_single_element_match(self):
        self.assertEqual(binary_search([5], 5), 0)

    def test_multiple_elements_match_middle(self):
        nums_list = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(binary_search(nums_list, 9), 4)

    def test_target_first_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)

    def test_target_last_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)

    def test_target_not_present_middle(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 4), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 10), -1)

    def test_target_less_than_all(self):
        self.assertEqual(binary_search([-5, -3, -1], -6), -1)

    def test_target_greater_than_all(self):
        self.assertEqual(binary_search([1, 2, 3], 10), -1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
