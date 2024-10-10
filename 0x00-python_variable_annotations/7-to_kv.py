#!/usr/bin/env python3i
"""import tuple"""
from typing import Union, Tuple
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing the string k and the square of v."""
    return (k, float(v ** 2))