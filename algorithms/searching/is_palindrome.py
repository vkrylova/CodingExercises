def is_palindrome(str_to_check):
    """
    Check whether the input string is a palindrome.

    This method ignores non-alphanumeric characters and is case-insensitive.
    It compares characters from both ends moving towards the center.

    Args:
        str_to_check (str): The string to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(str_to_check) - 1
    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not str_to_check[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        while left < right and not str_to_check[right].isalnum():
            right -= 1
        # Compare characters ignoring case
        if str_to_check[left].lower() != str_to_check[right].lower():
            return False
        left += 1
        right -= 1
    return True
