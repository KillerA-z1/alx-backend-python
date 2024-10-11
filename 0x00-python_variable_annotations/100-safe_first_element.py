#!/usr/bin/env python3
"""
Description:
    This module contains a function `safe_first_element` that returns
    the first element of a sequence if it exists, otherwise returns None.

Functions:
    safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
        Outputs the first element of lst if there is any, otherwise None.

Parameters:
    lst (Sequence[Any]): A sequence of elements of any type.

Returns:
    Union[Any, None]: The first element of the sequence if it exists,
    otherwise None.
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Outputs the first element of lst if there is any, otherwise None. '''
    if lst:
        return lst[0]
    else:
        return None
