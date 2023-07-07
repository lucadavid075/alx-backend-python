#!/usr/bin/env python3
"""
Type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Funtion that takes a string and an integer or float number
    and returns a tuple of string and float
    """
    return (k, (v**2))
