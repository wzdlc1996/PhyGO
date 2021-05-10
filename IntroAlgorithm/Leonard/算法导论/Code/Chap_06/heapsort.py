#!/usr/bin/env python

class heapSort:
    def __init__(self, arr):
        self.body = arr
        self.size = len(arr)

    def getSize(self):
        return self.size
    
    def maxHeapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        arr = self.body
        if l < self.size and arr[l] > arr[i]:
            largest = l
        else:
            largest = i
        if r < self.size and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        for i in range(int((len(self.body) - 1)/2), -1, -1):
            self.maxHeapify(i)
    
    def sort(self):
        self.buildMaxHeap()
        for i in range(len(self.body)-1, 0, -1):
            self.body[0], self.body[self.getSize()-1] = self.body[self.getSize()-1], self.body[0]
            self.size -= 1
            self.maxHeapify(0)
        return self.body

    
if __name__ == "__main__":
    arr = list(range(10, -1, -1))
    print(arr)
    print(heapSort(arr).sort())