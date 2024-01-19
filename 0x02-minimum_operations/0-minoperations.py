#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    calculate the fewest no. of operations needed to result
    in exactly n H characters in the file.
    """
    if not isinstance(n, int) or n <= 0:
        return 0
    num_operations = 0
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            num_operations += divisor
        else:
            divisor += 1
    if n > 1:
        num_operations += n
    return num_operations
