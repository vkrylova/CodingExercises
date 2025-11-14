import pytest

from algorithms.searching.anagram import is_anagram


# ——— Anagram pairs ———
@pytest.mark.parametrize(
    "left, right",
    [
        ("listen", "silent"),
        ("evil", "vile"),
        ("aabbcc", "baccab")
    ]
)
def test_simple_anagrams(left, right):
    assert is_anagram(left, right)


# ——— Non-anagram pairs ———
@pytest.mark.parametrize(
    "left, right",
    [
        ("hello", "holleq"),
        ("test", "ttea"),
        ("aabbcc", "aabbc")
    ]
)
def test_non_anagrams(left, right):
    assert not is_anagram(left, right)


# ——— Mixed-case behavior ———
@pytest.mark.parametrize(
    "left, right, expected",
    [
        ("Tea", "eat", False),  # should fail: case mismatch
        ("Tea", "eaT", True),  # should pass: matching case]
    ]
)
def test_case_sensitivity(left, right, expected):
    assert is_anagram(left, right) == expected


# ——— Length mismatch ———
@pytest.mark.parametrize(
    "left,right",
    [
        ("abc", "ab"),
        ("a", ""),
    ]
)
def test_different_lengths(left, right):
    assert not is_anagram(left, right)


# ——— Empty strings ———
@pytest.mark.parametrize(
    "left,right",
    [
        ("", ""),
    ]
)
def test_empty_strings(left, right):
    assert is_anagram(left, right)
