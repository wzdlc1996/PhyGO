#!/usr/bin/env python

import random

def randInt(a, b) -> int:
    """
    Generate a random integer in the interval(left-in-right-out) [a, b)

    :param a: Left start of the interval
    :param b: Right end of the interval
    :return: integer
    """
    if b <= a:
        return 0
    else:
        return random.randint(a, b+1)

def randArr1D(leng: int, rang: slice = (-1,1)) -> list:
    """
    Generate a random 1-D array.

    :param leng: Length of the array (non negative integer)
    :param rang: Range of the random variables (slice of size 2), default (-1,1)
    :return: 1-D array, with its elements randomly distributed in range.
    """
    if len(rang) == 0:
        rr = (-1,1)
    elif len(rang) == 1:
        rr = rang + (1,)
    else:
        rr = rang
    arr = random.choices(range(rr[0], rr[1]), k=leng)
    return arr

def randMatrix(m: int, n: int, rang: slice = (-1,1)) -> list:
    """
    Generate a random matrix. Its elements are independently evenly distributed in the range of rang.

    :param m: the number of rows
    :param n: the number of columes
    :param rang: range of the random variables (slice of size 2), default (-1,1)
    :return: 2-D array, as the matrix of m x n
    """
    if len(rang) == 0:
        rr = (-1,1)
    elif len(rang) == 1:
        rr = rang + (1,)
    else:
        rr = rang
    arr = [[0] * m] * n
    for i in range(m):
        arr[i] = randArr1D(n, rr)