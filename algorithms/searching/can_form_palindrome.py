def can_form_palindrome(str):
    """
    Determine whether any permutation of the input string can form a palindrome.

    A string can be rearranged into a palindrome if and only if no more than one
    character appears an odd number of times. This method counts the frequency
    of each character and checks how many of them have odd occurrences.

    Args:
        str: The input string to analyze.

    Returns:
        bool: True if the string's characters can be permuted into a palindrome,
              False otherwise.
    """
    frequencies = {}
    for index in str:
        if index in frequencies:
            frequencies[index] += 1
        else:
            frequencies[index] = 1
    count_odd_chars = sum(bool(value % 2)
                          for value in frequencies.values())
    return count_odd_chars <= 1
