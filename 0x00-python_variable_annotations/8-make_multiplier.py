#!/usr/bin/env python3
"""
This module provides a function `make_multiplier` that accepts float multiplier
as an argument and returns a function that multiplies a float by the given
multiplier.

Functions:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
        Accepts a float multiplier and returns a function that multiplies float
        by the multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Outputs function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier
