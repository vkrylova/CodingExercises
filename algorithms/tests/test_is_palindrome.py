import pytest
from algorithms.searching.is_palindrome import is_palindrome

palindrome_test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("racecar", True),
    ("No lemon, no melon", True),
    ("", True),              # empty string
    ("x", True),             # single character
    ("race a car", False),
    ("hello", False),
    ("abc", False),
]

palindrome_test_ids = [
    "famous_palindrome_phrase",
    "simple_palindrome",
    "palindrome_with_spaces",
    "empty_string",
    "single_character",
    "non_palindrome_phrase",
    "non_palindrome_hello",
    "non_palindrome_abc",
]

@pytest.mark.parametrize(
    "text, expected",
    palindrome_test_cases,
    ids=palindrome_test_ids
)
def test_is_palindrome(text, expected):
    # Verifies that each string is correctly identified as a palindrome or not
    assert is_palindrome(text) is expected