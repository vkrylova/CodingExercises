def is_anagram(str1, str2):
    """
    Determine whether two strings are anagrams of each other.

    Two strings are considered anagrams if they contain exactly the same
    characters in the same quantities, though possibly arranged in a
    different order.

    The function first checks whether the lengths differ — if so, they
    cannot be anagrams. It then builds a frequency map for characters in
    the first string, decreases the counts while traversing the second,
    and finally verifies that all counts return to zero.

    Parameters:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings are anagrams, otherwise False.
    """
    if len(str1) != len(str2):
        return False
    chars_map = {}
    for ch in str1:
        if ch in chars_map:
            chars_map[ch] += 1
        else:
            chars_map[ch] = 1

    for ch in str2:
        if ch in chars_map:
            chars_map[ch] -= 1

    return all(value == 0 for value in chars_map.values())