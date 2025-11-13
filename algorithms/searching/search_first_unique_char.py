def search_first_unique_char(str):
    """
    Find the index of the first non-repeating character in a string.

    This function counts the occurrences of each character in the input string
    and then returns the index of the first character that appears exactly once.
    If no unique character exists, it returns -1.

    Args:
        str (str): The input string to search for a unique character.

    Returns:
        int: The index of the first non-repeating character, or -1 if none exists.
    """
    chars_count = {}
    for ch in str:
        if ch in chars_count:
            chars_count[ch] += 1
        else:
            chars_count[ch] = 1
    print(chars_count)
    return next((i for i, ch in enumerate(str) if chars_count[ch] == 1), -1)
