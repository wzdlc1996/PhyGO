#!/usr/bin/env python

class youngTableau:
    def __init__(self, arr, shape):
        self.shape = shape
        m, n = self.shape
        self.body = [[m * n] * n for _ in range(m)]
        i = 0
        j = 0
        for x in sorted(arr):
            self.body[i][j] = x
            j += 1
            if j == n:
                j = 0
                i += 1
        self.inf = m * n

    def extractMin(self):
        val = self.body[0][0]
        self.body[0][0] = self.inf
        self.sinkElement(0, 0)
        return val
    
    def sinkElement(self, i, j):
        m, n = self.shape
        ele = self.body[i][j]
        if i == m - 1:
            for k in range(j+1, n):
                
                if self.body[i][k] < ele:
                    self.body[i][k-1] = self.body[i][k]
            self.body[i][k] = ele
            return

        if j == n - 1:
            for k in range(i+1, m):
                if self.body[k][j] < ele:
                    self.body[k-1][j] = self.body[k][j]
            self.body[k][j] = ele
            return

        lx, ly = i + 1, j
        rx, ry = i, j + 1
        if self.body[lx][ly] < ele:
            lix, liy = lx, ly
        else:
            lix, liy = i, j
        if self.body[rx][ry] < self.body[lix][liy]:
            lix, liy = rx, ry
        if lix != i or liy != j:
            self.body[lix][liy], self.body[i][j] = self.body[i][j], self.body[lix][liy]
            self.sinkElement(lix, liy)

    def isFull(self):
        return self.body[-1][-1] < self.inf

    def floatElement(self, i, j):
        ele = self.body[i][j]
        lx, ly = max(i - 1, 0), j
        rx, ry = i, max(j - 1, 0)
        if self.body[lx][ly] > ele:
            lix, liy = lx, ly
        else:
            lix, liy = i, j
        if self.body[rx][ry] > self.body[lix][liy]:
            lix, liy = rx, ry
        if lix != i or liy != j:
            self.body[lix][liy], self.body[i][j] = self.body[i][j], self.body[lix][liy]
            self.floatElement(lix, liy)

    def insert(self, x):
        if self.isFull():
            raise ValueError("Tableau is full")

        m, n = self.shape
        self.body[-1][-1] = x
        self.floatElement(m - 1, n - 1)

    def exists(self, x):
        m, n = self.shape
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if self.body[i][j] == x:
                return True
            if self.body[i][j] > x:
                i, j = i - 1, j
            else:
                i, j = i, j + 1
        return False


    def __str__(self):
        def vec2str(x):
            return "\t".join([str(z) if (z != self.inf) else "inf" for z in x])
        return "\n" + "\n".join([vec2str(x) for x in self.body]) + "\n"



if __name__ == "__main__":
    import time
    import matplotlib.pyplot as plt
    import numpy as np
    import os

    lx = 500
    ly = 500
    times = np.zeros((lx * ly, 2))
    for m in range(lx):
        for n in range(ly):
            #y = youngTableau(list(range(m * n)), (m, n))
            y = youngTableau([0], (1, 1))
            y.shape = (m, n)
            y.body = np.arange(1, m * n + 1).reshape((m, n))
            y.inf = m * n 
            st = time.time()
            y.exists(m - 1)
            ed = time.time()
            times[m + n] += np.array([ed - st, 1])
    times = [x / y for i, (x, y) in enumerate(times) if 0 < i < (lx+ly)/2]
    inputSize = np.arange(1, len(times) + 1)
    plt.figure()
    plt.plot(inputSize, times)
    plt.title("Time Complexity Scaling of youngTab.exists, worst case")
    plt.savefig(os.path.realpath(__file__ + "/../") + "/time_complexity_youngTabExists.png")
    plt.show()

            
