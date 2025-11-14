import pytest

from algorithms.sorting.merge_sorted_arrays import merge_sorted_arrays

# Test cases list
merge_test_cases = [
    ([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6]),
    ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),
    ([1, 2, 3], 3, [], 0, [1, 2, 3]),
    ([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3, [1, 2, 3, 4, 5, 6]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ([1, 2, 2, 0, 0, 0], 3, [2, 3, 4], 3, [1, 2, 2, 2, 3, 4]),
    ([2, 0], 1, [1], 1, [1, 2]),
]

# Name for test cases
merge_test_ids = [
    "normal_case",
    "nums1_empty",
    "nums2_empty",
    "nums1_less_than_nums2",
    "nums1_greater_than_nums2",
    "duplicates_case",
    "single_elements"
]


@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    merge_test_cases,
    ids=merge_test_ids
)
def test_merge_sorted(nums1, m, nums2, n, expected):
    result = merge_sorted_arrays(nums1.copy(), m, nums2.copy(), n)
    assert result == expected
