#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """determine the winner of the game based on the number of rounds."""
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    # generate prime nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    for idx1, is_prime in enumerate(primes, 1):
        if idx1 == 1 or not is_prime:
            continue
        for idx2 in range(idx1 + idx1, n + 1, idx1):
            primes[idx2 - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda X: X, primes[0: n])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1

    if maria_wins == ben_wins:
        return None

    return "Maria" if maria_wins > ben_wins else "Ben"
