#!/usr/bin/env python3
"""
Type-annotated function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Funtion that takes a list of float numbers
    returns the sum their sum as float.
    """
    return float(sum(input_list))
