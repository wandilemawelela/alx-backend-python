#!/usr/bin/env python3
"""
This module contains a function that creates a tuple
from a string and a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and a number.

    Args:
        k (str): The string element of the tuple.
        v (Union[int, float]): The number to be squared and
        used as the second element of the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element
        is the string `k` and the second element is the square
        of `v` as a float.
    """
    return (k, float(v ** 2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
