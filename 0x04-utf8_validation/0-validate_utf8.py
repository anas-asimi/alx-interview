#!/usr/bin/python3
"""
0-validate_utf8.py
"""


from typing import List


def validUTF8(data: List) -> bool:
    """validUTF8
    Args:
        data (List): _description_
    Returns:
        bool: _description_
    """
    for n in data:
        if n > 127:
            return False
    return True
