#!/usr/bin/python3
"""Prime Game"""


def is_prime(num):
    """Helper function to check if a number is prime."""
    if num <= 1:
        return False
    for idx in range(2, int(num**0.5) + 1):
        if num % idx == 0:
            return False
    return True


def isWinner(x, nums):
    """determine the winner of the game based on the number of rounds."""
    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        if len(nums) % 2 == 0:
            ben_wins += 1
        else:
            if is_prime(nums[0]):
                maria_wins += 1
            else:
                ben_wins += 1
        nums = nums[1:]

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
