#!/usr/bin/env python3
"""
Annotated the function’s parameter below
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes a list lst as input and returns a new list of tuples
    """
    return [(i, len(i)) for i in lst]
