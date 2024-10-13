#!/usr/bin/env python3
"""
This module contains a function that adds two float numbers.
"""


def add(a: float, b: float) -> float:
    """
    Add two float numbers and return their sum.

    Args:
        a (float): The first float number.
        b (float): The second float number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
