#!/usr/bin/env python

import random

def randArr1D(leng: int, rang: slice) -> list:
    """
    Generate a random 1-D array.

    Keyword arguments:
    leng:   Length of the array (non negative integer)
    rang:   Range of the random variables (slice of size 2)
    """
    if len(rang) == 0:
        rr = (-1,1)
    elif len(rang) == 1:
        rr = rang + (1,)
    else:
        rr = rang
    arr = [0] * leng
    for i in range(len(arr)):
        arr[i] = random.randint(rr[0], rr[1])
    return arr