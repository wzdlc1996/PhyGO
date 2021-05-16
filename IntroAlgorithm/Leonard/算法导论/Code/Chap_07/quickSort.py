#!/usr/bin/env python

import random
import sys
import os
import time

sys.path.append(os.path.realpath(__file__ + "/../.."))
"""
Only works when `pwd` is the location of this file
#sys.path.append("..")
"""
from Base import rand

def qSort(arr):
    quickSort(arr, 0, len(arr) - 1)

def quickSort(arr, i, j):
    if i < j < len(arr):
        q = parti(arr, i, j)
        quickSort(arr, i, q - 1)
        quickSort(arr, q, j)

def parti(arr, i, j):
    x = arr[j]
    s = i - 1
    for r in range(i, j):
        if arr[r] <= x:
            s = s + 1
            arr[s], arr[r] = arr[r], arr[s]
    arr[s+1], arr[j] = arr[j], arr[s+1]
    return s + 1

if __name__ == "__main__":
    arr = rand.randArr1D(10, (-5, 5))
    print(arr)
    qSort(arr)
    print(arr)