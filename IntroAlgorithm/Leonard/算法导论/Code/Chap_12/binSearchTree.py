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
        self.val = []
        self.key = []
        self.leftInd = []
        self.rightInd = []
        self.pInd = []
        self.root = None
        self.size = 0
    
    def left(self, x):
        return self.leftInd[x]
    
    def right(self, x):
        return self.rightInd[x]

    def par(self, x):
        return self.pInd[x]

    def isEmpty(self, x):
        return x is None

    def getRoot(self):
        return self.root

    def __len__(self):
        return self.size

    def __getitem__(self, k):
        return self.val[k]

    def inorderTreeWalk(self, x):
        if not self.isEmpty(x):
            self.inorderTreeWalk(self.left(x))
            print(self.val[x])
            self.inorderTreeWalk(self.right(x))

    def treeSearch(self, x, key):
        if x is not None:
            print(self.key[x], key)
        if self.isEmpty(x):
            return None, None
        elif self.key[x] == key:
            return self.key[x], self.val[x]
        else:
            if self.key[x] > key:
                return self.treeSearch(self.left(x), key)
            else:
                return self.treeSearch(self.right(x), key)

    def treeDive(self, x, method):
        ch = method(x)
        while not self.isEmpty(ch):
            x = ch
            ch = method(x)
        return self.key[x], self.val[x]

    
    def findMin(self):
        return self.treeDive(self.getRoot(), self.left)

    def findMax(self):
        return self.treeDive(self.getRoot(), self.right)

    def predecessor(self, x):
        return self.treeDive(self.left(x), self.right)

    def successor(self, x):
        return self.treeDive(self.right(x), self.left)

    def serInit(self, size):
        """
        Initialize a binary search tree sequentially, well balanced, for test

        :param size: tree size
        """
        x = list(range(size))
        self.size = size
        self.key = list(range(size))
        self.val = list(range(5,5 + size))
        self.leftInd = [None] * size
        self.rightInd = [None] * size
        self.pInd = [None] * size
        rind = int(size / 2)
        self.root = x[rind]

        def binize(indlist, rt, mode):
            """
            Assign indlist into self with rt as the root, referred by mode as left or right subtree

            :param indlist: index list, subset of x
            :param rt: root index
            :param mode: 0/1 valued, 0 means left subtree, 1 means right subtree
            """
            sz = len(indlist)
            if sz == 0:
                return
            else:
                hf = int(sz / 2)
                r = indlist[hf]
                self.pInd[r] = rt
                if mode == 0:
                    self.leftInd[rt] = r
                else:
                    self.rightInd[rt] = r
                binize(indlist[:hf], r, 0)
                binize(indlist[hf+1:], r, 1)
        
        binize(x[:rind], self.root, 0)
        binize(x[rind+1:], self.root, 1)

    def __str__(self):
        return "Tree size: {}\nKey list: {}\nVal list: {}".format(
            self.size,
            str(self.key),
            str(self.val)
        )


if __name__ == "__main__":
    bt = binSearchTree()
    bt.serInit(10)
    print(bt)
    # bt.inorderTreeWalk(5)
    # print(bt.treeSearch(bt.getRoot(), 4))
    # print(bt.findMin())
    print(bt.successor(5))


