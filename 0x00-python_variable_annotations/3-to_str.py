#!/usr/bin/env python3
"""
This module contains a function that converts a
float to its string representation.
"""


def to_str(n: float) -> str:
    """
    Convert a float to its string representation.

    Args:
        n (float): The float number.

    Returns:
        str: The string representation of the float.
    """
    return str(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
