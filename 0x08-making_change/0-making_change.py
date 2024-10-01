#!/usr/bin/python3
"""
0-making_change.py
"""
from typing import List


def findFewestCombination(coins: list[int],
                          total: int,
                          initial: int = 0,
                          coinsCounter: int = 0,
                          lastCoin: int = None) -> int:
    """
    findFewestCombination
    Args:
        coins (list[int]):
        total (int):
        initial (int, optional): Defaults to 0.
        coinsCounter (int, optional): Defaults to 0.
        lastCoin (int, optional): Defaults to None.
    Returns:
        int:
    """
    # print(f'total: {total} initial: {initial}  coinsCounter: {coinsCounter}')
    if total == initial:
        return coinsCounter

    for coin in coins:
        if (initial + coin) > total:
            continue

        if lastCoin is not None and coin > lastCoin:
            continue

        # print(f'lets add: {coin}')
        combination = findFewestCombination(
            coins, total, initial+coin, coinsCounter + 1, coin)
        if combination is not None:
            return combination


def makeChange(coins, total: int) -> int:
    """
    makeChange
    Args:
        coins (_type_):
        total (int):

    Returns:
        int:
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    change = findFewestCombination(sorted_coins, total)
    if change is not None:
        return change
    return -1
