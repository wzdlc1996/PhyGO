#!/usr/bin/env python

from math import log2

def left(i: int) -> int:
    return 2 * i + 1

def right(i: int) -> int:
    return 2 * i + 2

def heapSize(arr):
    return len(arr)

def maxHeapify(arr, i):
    l = left(i)
    r = right(i)
    if l < heapSize(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < heapSize(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest)

def buildMaxHeap(arr):
    for i in range(int((len(arr) - 1) / 2), -1, -1):
        maxHeapify(arr, i)

if __name__ == "__main__":
    testHeap = list(range(0,10,1))
    testHeap[0] = 0
    print("Initial: {}".format(testHeap))
    buildMaxHeap(testHeap)
    print("Final: {}".format(testHeap))
