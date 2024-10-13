#!/usr/bin/env python3
"""
This module contains a function that safely returns the first
element of a list.
"""

from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely returns the first element of the list if it exists,
    otherwise returns None.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple)
        containing elements of any type.

    Returns:
        Optional[Any]: The first element of the list if it
        exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
