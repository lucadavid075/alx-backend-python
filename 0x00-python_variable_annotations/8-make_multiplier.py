#!/usr/bin/env python3
"""
Type-annotated funtion make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a multiplier as float and returns
    a function that multiplies a float by the multiplier
    """
    return lambda x: x * multiplier
