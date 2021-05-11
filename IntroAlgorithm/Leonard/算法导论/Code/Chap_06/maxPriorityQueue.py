#!/usr/bin/env python

class maxPriorityQueue:
    def __init__(self, keys, hands):
        if len(keys) != len(hands):
            raise ValueError("Keys and Handles Size Mismatch")
        self.key = keys
        self.size = len(keys)
        self.hand = hands
        self.buildMaxHeap()

    def __len__(self):
        return self.size
    
    def __getitem__(self, k):
        if k >= len(self):
            raise IndexError("Out of queue range")
        ind = k
        if k < 0:
            ind = len(self) + k
        return self.key[ind], self.hand[ind]

    def max(self):
        return self.hand[0]

    def extractMax(self):
        ele = self.hand[0]
        self.swap(0, self.size - 1)
        self.size -= 1
        self.maxHeapify(0)
        return ele

    def increaseKey(self, i, k):
        x = self.key[i]
        if k < x:
            raise ValueError("IncreasKey requires k >= x")
        self.key[i] = k
        while i > 0 and self.key[int((i - 1) / 2)] < self.key[i]:
            self.swap(int((i - 1) / 2), i)
            i = int((i - 1) / 2)

    def insert(self, x, key):
        if self.size == len(self.key):
            self.key.append(-1)
            self.hand.append(x)
        else:
            self.key[self.size] = -1
            self.hand[self.size] = x
        self.size += 1
        self.increaseKey(self.size - 1, key)

    def swap(self, i, j):
        self.key[i], self.key[j] = self.key[j], self.key[i]
        self.hand[i], self.hand[j] = self.hand[j], self.hand[i]
        

    def maxHeapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.size and self.key[l] > self.key[i]:
            largest = l
        else:
            largest = i
        if r < self.size and self.key[r] > self.key[largest]:
            largest = r
        if largest != i:
            self.swap(i, largest)
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        for i in range(int((self.size - 1) / 2), -1, -1):
            self.maxHeapify(i)


if __name__ == "__main__":
    que = maxPriorityQueue(list(range(5)), ["a", "b", "c", "d", "e"])
    print("Initialized as {}".format({x:y for x, y in zip(que.key, que.hand)}))
    print("-------------------")
    print("Current max: {}".format(que.max()))
    que.insert("f", 10)
    print("Insert ('f', 10), and Max: {}".format(que.max()))
    print("Current content {}".format({x:y for x, y in zip(que.key, que.hand)}))
    print("Pop max: {}".format(que.extractMax()))
    print("Current content {}".format({x:y for x, y in zip(que.key, que.hand)}))
    print("Pop max: {}".format(que.extractMax()))
    print("Current content {}".format({x:y for x, y in zip(que.key, que.hand)}))
    que.insert("g", 11)
    print("Insert ('g', 11), and Max: {}".format(que.max()))
    print("Current content {}".format({x:y for x, y in zip(que.key, que.hand)}))
    print("Pop max: {}".format(que.extractMax()))
    print("Current content {}".format({x:y for x, y in zip(que.key, que.hand)}))
    print("Pop max: {}".format(que.extractMax()))
    print("Current content {}".format({x:y for x, y in zip(que.key, que.hand)}))