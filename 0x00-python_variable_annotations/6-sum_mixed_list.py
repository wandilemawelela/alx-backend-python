#!/usr/bin/env python3
"""
This module contains a function that sums a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list of integers and floats and return the result as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and
        float numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
