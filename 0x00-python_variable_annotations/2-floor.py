#!/usr/bin/env python3
"""
This module contains a function that returns the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of the given float.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of the float.
    """
    return math.floor(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
