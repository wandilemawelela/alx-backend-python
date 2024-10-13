#!/usr/bin/env python3
"""
This module contains a function that creates a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns it multiplied by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function


if __name__ == "__main__":
    import doctest
    doctest.testmod()
