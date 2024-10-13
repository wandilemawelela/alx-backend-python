#!/usr/bin/env python3
"""
This module contains a function that returns
the length of each element in a list.
"""

from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Args:
        lst (List[Sequence]): A list of sequences
        (strings, lists, tuples, etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
