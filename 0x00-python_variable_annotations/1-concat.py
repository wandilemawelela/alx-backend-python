#!/usr/bin/env python3
"""
This module contains a function that concatenates two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
