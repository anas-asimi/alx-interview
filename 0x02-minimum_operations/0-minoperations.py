#!/usr/bin/python3
"""
0-minoperations.py
"""
from typing import Union


def find_smallest_number(*args) -> Union[int, None]:
    """_summary_

    Returns:
        int | None: _description_
    """
    smallest = None
    for num in args:
        if num is not None:
            if smallest is None or num < smallest:
                smallest = num
    return smallest


def do_operation(text: str, n: int, operation: str, clipboard: str) -> int:
    """_summary_

    Args:
        text (str): _description_
        n (int): _description_
        operation (str): _description_
        clipboard (str): _description_

    Returns:
        _type_: _description_
    """
    if operation == 'Copy All':
        clipboard = text
    if operation == 'Paste':
        text = text + clipboard
    if len(text) > n:
        return None
    if len(text) == n:
        return 1
    if len(text) < n:
        if operation == 'Copy All':
            op = do_operation(text, n, 'Paste', clipboard)
            return None if op is None else op + 1
        else:
            op1 = do_operation(text, n, 'Copy All', clipboard)
            op2 = do_operation(text, n, 'Paste', clipboard)
            smallest_number = find_smallest_number(op1, op2)
            return None if smallest_number is None else smallest_number + 1


def minOperations(n: int) -> int:
    """_summary_

    Args:
        n (int): _description_

    Returns:
        _type_: _description_
    """
    text = 'H'
    numberOfOp = do_operation(text, n, 'Copy All', '')
    return numberOfOp
