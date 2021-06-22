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

class binSearchTree:
    def __init__(self):
        self.body = []
        self.leftInd = []
        self.rightInd = []
        self.pInd = []
    
    def left(self, x):
        return self.leftInd[x]
    
    def right(self, x):
        return self.rightInd[x]

    def par(self, x):
        return self.pInd[x]

    def isEmpty(self, x):
        return x is None

    def inorderTreeWalk(self, x):
        if not self.isEmpty(x):
            self.inorderTreeWalk(self.left(x))
            print(self.body[x])
            self.inorderTreeWalk(self.right(x))

    def serInit(self, size):
        """
        Initialize a binary search tree sequentially, well balanced, for test

        :param size: tree size
        """
        x = list(range(size))
        self.body = list(range(size))
        self.leftInd = [None] * size
        self.rightInd = [None] * size
        self.pInd = [None] * size

        def binize(indlist, rt, mode, sf):
            size = len(indlist)
            if size == 0:
                return
            elif size == 1:
                x = indlist[0]
                if mode == 0:
                    sf.leftInd[rt] = x
                else:
                    sf.rightInd[rt] = x
                sf.pInd[x] = rt
                return

            hf = int(size / 2)
            binize(indlist[:hf], hf, 0, sf)
            binize(indlist[hf+1:], hf, 1, sf)
        
        binize(x, x[int(size / 2)], 0, self)

    def __str__(self):
        return "Tree size: {}\nL list: {}\nR list: {}".format(
            len(self.body),
            str(self.leftInd),
            str(self.rightInd)
        )


if __name__ == "__main__":
    bt = binSearchTree()
    bt.serInit(10)
    print(bt)
    bt.inorderTreeWalk(5)


