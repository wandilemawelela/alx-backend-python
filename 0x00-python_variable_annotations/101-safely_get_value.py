#!/usr/bin/env python3
"""
This module contains a function that safely retrieves a
value from a dictionary.
"""

from typing import TypeVar, Mapping, Any, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T],
        key: Any, default: Optional[T] = None) -> Optional[T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): The default value to return if the key is
        not found.

    Returns:
        Optional[T]: The value associated with the key if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    import doctest
    doctest.testmod()
