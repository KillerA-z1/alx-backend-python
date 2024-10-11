#!/usr/bin/env python3
"""
    floor(n: float) -> int

    Return the largest integer value less than or equal to the given float.

    Parameters:
    n (float): The float number to be floored.

    Returns:
    int: The largest integer value less than or equal to n.
"""


def floor(n: float) -> int:
    ''' Return largest int value less than or equal to n. '''
    return int(n) if n >= 0 else int(n) - 1
