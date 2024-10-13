#!/usr/bin/env python3
"""
This module defines and annotates several variables with specified values.
"""

a: int = 1
"""
a (int): An integer with a value of 1
"""

pi: float = 3.14
"""
pi (float): A float with a value of 3.14
"""

i_understand_annotations: bool = True
"""
i_understand_annotations (bool): A boolean with a value of True
"""

school: str = "Holberton"
"""
school (str): A string with a value of "Holberton"
"""


if __name__ == "__main__":
    print(f"a: {a}")
    print(f"pi: {pi}")
    print(f"i_understand_annotations: {i_understand_annotations}")
    print(f"school: {school}")
