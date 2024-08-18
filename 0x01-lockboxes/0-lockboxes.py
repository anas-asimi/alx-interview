#!/usr/bin/python3
"""
0-lockboxes.py
"""


def unlockBox(box, boxes):
    """
    unlockBox
    Args:
        box (_type_): _description_
        boxes (_type_): _description_
    """
    box["isOpened"] = True
    for key in box["keys"]:
        if key < len(boxes) and not boxes[key]["isOpened"]:
            unlockBox(boxes[key], boxes)


def canUnlockAll(boxes):
    """
    canUnlockAll
    Args:
        boxes (_type_): _description_

    Returns:
        _type_: _description_
    """
    import sys
    sys.setrecursionlimit(1500)
    boxes = [{"keys": x, "isOpened": False} for x in boxes]
    unlockBox(boxes[0], boxes)
    for box in boxes:
        if not box["isOpened"]:
            return False
    return True
