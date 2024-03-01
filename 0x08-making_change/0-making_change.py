#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):
    """
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    result = 0

    for coin in coins:
        numCoins = total // coin
        result += numCoins
        total -= numCoins * coin

    if total != 0:
        return -1
    return result
