def merge_sorted_arrays(nums1, m, nums2, n):
    """
    Merge two sorted arrays nums1 and nums2 into one sorted array in-place.

    Args:
        nums1 (List[int]): First sorted array with length m + n.
                           The first m elements are valid; the rest are placeholders (e.g., zeros).
        m (int): Number of valid elements in nums1.
        nums2 (List[int]): Second sorted array with n elements.
        n (int): Number of elements in nums2.

    Returns:
        List[int]: nums1 after merging nums2 into it in sorted order.

    Method:
        - Start merging from the end of nums1 to avoid overwriting existing elements.
        - Use three pointers:
            p1 -> last valid element in nums1 (m - 1)
            p2 -> last element in nums2 (n - 1)
            p  -> last position in nums1 (m + n - 1)
        - Iterate backwards with 'p' from the end to the start of nums1:
            1. If p2 < 0: all elements from nums2 are merged, break the loop.
            2. If p1 >= 0 and nums1[p1] > nums2[p2]: place nums1[p1] at nums1[p], decrement p1.
            3. Else: place nums2[p2] at nums1[p], decrement p2.
        - Continue until all elements from nums2 are merged.
    """
    p1 = m - 1
    p2 = n - 1 
    for p in range(n + m - 1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
    return nums1
