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
from Base import randArr


def brute_force(arr: list):
    ansDict = {}
    N = len(arr)
    for i in range(N):
        for l in range(1, N - i + 1):
            ansDict[(i,l)] = sum(arr[i:i+l])
    sumChecker = arr[0]
    kRig = (0, 1)
    for k in ansDict:
        if ansDict[k] > sumChecker:
            sumChecker = ansDict[k]
            kRig = k
    return kRig, sumChecker

def main():
    pass


if __name__ == "__main__":
    #main()
    v = [0] * 4
    for i in range(len(v)):
        v[i] = random.randint(-10, 10)
    print(v)
    print(brute_force(v))
