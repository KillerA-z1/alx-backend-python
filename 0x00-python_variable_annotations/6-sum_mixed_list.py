#!/usr/bin/env python3
"""
    Calculate the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all elements in the list.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Outputs sum of elements of mxd_list. '''
    return sum(mxd_lst)
