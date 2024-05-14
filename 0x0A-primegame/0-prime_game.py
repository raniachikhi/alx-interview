#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.
    """
    # Validate input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Initialize scores
    ben = 0
    maria = 0

    # Create a list to mark primes
    max_num = sorted(nums)[-1]
    a = [1] * (max_num + 1)
    a[0], a[1] = 0, 0  # 0 and 1 are not primes

    # Sieve of Eratosthenes to mark primes
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Play each round
    for i in nums:
        # Ben wins if the number of primes is even, otherwise Maria wins
        if sum(a[:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Marks multiples of a number as non-prime.

    Args:
        ls (list of int): Array to mark primes.
        x (int): The prime number to mark multiples of.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except IndexError:
            break
