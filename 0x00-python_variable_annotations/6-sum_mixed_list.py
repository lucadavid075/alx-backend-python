#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Funtion that takes a list of integer numbers
    returns the sum their sum as float.
    """
    return float(sum(mxd_lst))