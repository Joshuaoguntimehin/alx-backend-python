#!/usr/bin/env python3
"""import union"""
from typing import List, Union
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats."""
    return float(sum(mxd_lst))