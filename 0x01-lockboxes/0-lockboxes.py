#!/usr/bin/python3

def unlockBox(box, boxes):
    box["isOpened"] = True
    for key in box["keys"]:
        if boxes[key] and not boxes[key]["isOpened"]:
            unlockBox(boxes[key], boxes)


def canUnlockAll(boxes):
    boxes = [{"keys": x, "isOpened": False} for x in boxes]
    unlockBox(boxes[0], boxes)
    for box in boxes:
        if not box["isOpened"]:
            return False
    return True
