#!/usr/bin/env python3
"""
Type annoation added to the function safely_get_valur
"""

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Function that retrieves a value from a dict using a given key.
    """    
    if key in dct:
        return dct[key]
    else:
        return default