def binary_search(nums, target):
    """
    Performs binary search on a sorted list to find the target element.

    Args:
        nums: A sorted list of elements in ascending order.
        target: The element to search for in the list.

    Returns:
        int: Index of the target element if found, otherwise -1.
    """
    right = len(nums) - 1
    left = 0
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
