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

def iter_method(arr: list):
    valist = [(0,0)] * len(arr)
    valist[-1] = (arr[-1], 1)
    for k in range(len(arr) - 2, -1, -1):
        tester = arr[k] + valist[k+1][0]
        if tester > arr[k]:
            valist[k] = (tester, valist[k+1][1] + 1)
        else:
            valist[k] = (arr[k], 1)
    sumChecker = arr[0]
    kRig = (0, 1)
    for k in range(len(valist)):
        if valist[k][0] > sumChecker:
            sumChecker = valist[k][0]
            kRig = (k, valist[k][1])
    return kRig, sumChecker

def main():
    pass


if __name__ == "__main__":
    #main()
    inputSize = []
    bfTime = []
    imTime = []
    for l in range(10, 3000, 150):
        inputSize.append(l)
        v = rand.randArr1D(l, (-4,4))
        st = time.time()
        bfRes = brute_force(v)
        ed = time.time()
        bfTime.append(ed - st)
        st = time.time()
        imRes = iter_method(v)
        ed = time.time()
        imTime.append(ed - st)
        print("Testing for input size: {}, brute_force vs iter_method: {}".format(
            l,
            imRes == bfRes
        ))
    
    import matplotlib.pyplot as plt
    import numpy as np
    norm = lambda x: np.array(x) / np.max(x)
    plt.figure()
    plt.plot(inputSize, norm(bfTime), label="Brute Force")
    plt.plot(inputSize, norm(imTime), label="Iterative Method")
    plt.title("Time Complexity Scaling")
    plt.legend()
    plt.savefig(os.path.realpath(__file__ + "/../") + "/time_complexity.png")
    plt.show()
