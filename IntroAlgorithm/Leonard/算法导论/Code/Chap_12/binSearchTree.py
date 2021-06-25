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

    def resolv(self, ptr):
        """
        return key, val by the ptr
        """
        if self.isEmpty(ptr):
            return None, None
        return self.key[ptr], self.val[ptr]

    def treeSearchPtr(self, x, key):
        if self.isEmpty(x):
            return None
        elif self.key[x] == key:
            return x
        else:
            if self.key[x] > key:
                return self.treeSearchPtr(self.left(x), key)
            else:
                return self.treeSearchPtr(self.right(x), key)
    
    def treeSearch(self, x, key):
        return self.resolv(self.treeSearchPtr(x, key))

    def treeDive(self, x, method):
        ch = method(x)
        while not self.isEmpty(ch):
            x = ch
            ch = method(x)
        return x

    
    def findMin(self):
        x = self.treeDive(self.getRoot(), self.left)
        return self.resolv(x)

    def findMax(self):
        x = self.treeDive(self.getRoot(), self.right)
        return self.resolv(x)

    def predecessor(self, x):
        return self.treeDive(self.left(x), self.right)

    def successor(self, x):
        return self.treeDive(self.right(x), self.left)

    def setValue(self, ptr, *args):
        k, v, l, r, p = args
        if ptr in range(self.size):
            self.rightInd[ptr] = r
            self.leftInd[ptr] = l
            self.pInd[ptr] = p
            self.key[ptr] = k
            self.val[ptr] = v
            return ptr
        else:
            self.rightInd.append(r)
            self.leftInd.append(l)
            self.pInd.append(p)
            self.key.append(k)
            self.val.append(v)
            self.size += 1
            return self.size - 1


    def insert(self, z):
        key, val = z
        y = x = self.getRoot()
        while not self.isEmpty(x):
            y = x
            if key < self.key[x]:
                x = self.left(x)
            else:
                x = self.right(x)

        ptr = self.setValue(-1, key, val, None, None, y)
        if y is None:
            self.root = 0
        else:
            if key < self.key[y]:
                self.leftInd[y] = ptr
            else:
                self.rightInd[y] = ptr

    def transplant(self, des, src):
        """
        transplant subtree of src to des
        """
        if des == self.root:
            self.root = src
        else:
            par = self.par(des)
            if des == self.left(par):
                self.leftInd[par] = src
            else:
                self.rightInd[par] = src
            if not self.isEmpty(src):
                self.pInd[src] = par

    def delete(self, key):
        ptr = self.treeSearchPtr(self.root, key)
        if self.isEmpty(self.left(ptr)):
            self.transplant(ptr, self.right(ptr))
        elif self.isEmpty(self.right(ptr)):
            self.transplant(ptr, self.left(ptr))
        else:
            y = self.successor(ptr)
            if self.par(y) != ptr:
                self.transplant(y, self.right(y))
                self.rightInd[y] = self.rightInd[ptr]
                self.pInd[self.rightInd[y]] = y
            self.transplant(ptr, y)
            self.leftInd[y] = self.leftInd[ptr]
            self.pInd[self.leftInd[y]] = y

        self.key[ptr] = None
        self.val[ptr] = None
        self.size -= 1


                

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
    # print(bt)
    # bt.inorderTreeWalk(5)
    # print(bt.treeSearch(bt.getRoot(), 4))
    # print(bt.findMin())
    # print(bt.successor(5))
    bt.insert((19, 100))
    print(bt)
    bt.inorderTreeWalk(bt.getRoot())
    bt.delete(4)
    bt.inorderTreeWalk(bt.getRoot())
    


