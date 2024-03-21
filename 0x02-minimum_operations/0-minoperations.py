#!/usr/bin/python3
def minOperations(n: int) -> int:
    op = 0
    body_length = 1
    clipboard = 0
    while body_length < n:
        if n % body_length == 0:
            clipboard = body_length
            op += 1
        body_length += clipboard
        op += 1
    return op
