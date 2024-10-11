#!/usr/bin/env python3
"""
safely_get_value

Description:
    Using the parameters and the return values, add type annotations
    to the function.

Parameters:
    dct (Mapping): The dictionary from which to retrieve the value.
    key (Any): The key to look up in the dictionary.
    default (Union[T, None], optional): The default value to return if
    the key is not found. Defaults to None.

Returns:
    Union[Any, T]: The value associated with the key if it exists,
    otherwise the default value.
"""


from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    ''' Outputs dct[key] if it exists, otherwise return `default`. '''
    if key in dct:
        return dct[key]
    else:
        return default
