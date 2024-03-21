#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters."""
    operations = 0
    factor = 2
    if n < 2:
        return 0

    while factor <= n:
        while n % factor == 0:
            operations += factor
            n = n // factor
        factor += 1 
    
    return operations
