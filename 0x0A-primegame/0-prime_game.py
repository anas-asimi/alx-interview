#!/usr/bin/python3
"""
0-prime_game.py
This module defines a game to determine the winner
based on the number of prime numbers up to a given n.
"""

def count_prime(n):
    """
    Count the number of prime numbers from 1 to n.
    
    Args:
        n (int): The upper limit of numbers to check for primes.
    
    Returns:
        int: The number of prime numbers up to and including n.
    """
    if n < 2:
        return 0

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i ** 2, n + 1, i):
                primes[j] = False

    return sum(primes)

def isWinner(x, nums):
    """
    Determine the winner of the game based on the number of primes.
    
    Args:
        x (int): The number of rounds.
        nums (list of int): List of integers representing the upper limits for each round.
    
    Returns:
        str: The name of the winner ('Maria' or 'Ben') or None if it's a tie.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = count_prime(n)
        if moves % 2 == 0:
            ben_wins += 1  # Ben wins if moves are even
        else:
            maria_wins += 1  # Maria wins if moves are odd

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
