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


    def __str__(self):
        def vec2str(x):
            return "\t".join([str(z) if (z != self.inf) else "inf" for z in x])
        return "\n" + "\n".join([vec2str(x) for x in self.body]) + "\n"



if __name__ == "__main__":
    y = youngTableau(list(range(5)), (3, 3))
    print(y)
    y.extractMin()
    print(y)
    y.insert(5)
    print(y)
    y.insert(0)
    print(y)
