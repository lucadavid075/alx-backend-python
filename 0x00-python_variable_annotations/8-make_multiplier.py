#!/usr/bin/env python3
"""
Type-annotated funtion make_multiplier
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    """
    return lambda x: x * multiplier