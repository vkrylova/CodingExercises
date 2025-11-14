import pytest

from algorithms.searching.permute_palindrome import can_form_palindrome

palindrome_test_cases = [
    ("civic", True),
    ("ivicc", True),
    ("aabb", True),
    ("aab", True),
    ("rraceca", True),  # rearranges to "racecar"
    ("", True),  # empty string is palindromic
    ("x", True),  # single character
    ("hello", False),
    ("abc", False),
    ("aabc", False),
    ("abcd", False),
]

palindrome_test_ids = [
    "classic_palindrome",
    "can_rearrange_to_palindrome",
    "even_counts",
    "one_odd_count",
    "becomes_racecar",
    "empty_string",
    "single_character",
    "hello_not_palindromic",
    "abc_not_palindromic",
    "aabc_not_palindromic",
    "abcd_not_palindromic",
]


@pytest.mark.parametrize(
    "text, expected",
    palindrome_test_cases,
    ids=palindrome_test_ids
)
def test_permute_palindrome(text, expected):
    # Ensures that each provided string is correctly classified
    # as being rearrangeable (or not) into a palindrome
    assert can_form_palindrome(text) is expected
