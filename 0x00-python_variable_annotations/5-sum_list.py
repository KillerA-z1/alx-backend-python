#!/usr/bin/env python3
"""
    Calculates the sum of all elements in a list of floats.

    Args:
        input_list (List[float]): A list of floating point numbers.

    Returns:
        float: The sum of all elements in the input list.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Outputs sum of all elements in input_list. '''
    return sum(input_list)
