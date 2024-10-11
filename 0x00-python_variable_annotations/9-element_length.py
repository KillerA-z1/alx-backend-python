#!/usr/bin/env python3
"""
Function to compute the length of elements in an iterable of sequences.

Args:
    lst (Iterable[Sequence]): An iterable containing sequence elements.

Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a
        sequence from the input iterable and its corresponding length.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Outputs list of tuples, one for each element, of which
       consists of the element itself and its length.
    '''
    return [(i, len(i)) for i in lst]
