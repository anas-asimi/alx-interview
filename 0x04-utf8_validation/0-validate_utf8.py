#!/usr/bin/python3
"""
0-validate_utf8.py
"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """validUTF8
    Args:
        data (List): _description_
    Returns:
        bool: _description_
    """
    if len(data) == 0:
        return False
    for n in data:
        if isinstance(n, int) and n <= 127:
            continue
        return False
    return True
