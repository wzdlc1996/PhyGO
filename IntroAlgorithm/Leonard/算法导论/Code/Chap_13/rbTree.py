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
from Base.datastruct import binSearchTree

class bhTree(binSearchTree):
    def __init__(self):
        super().__init__()
        self.colors = []

    def setValue(self, ptr, **kwargs):
        ptr = super().setValue(ptr=ptr, **kwargs)
        if "color" not in kwargs:
            col = 1
        else:
            col = kwargs["color"]
        if len(self.colors) == self.size:
            self.colors[ptr] = col
        else:
            self.colors.append(col)
        return ptr

    def insert(self, z):
        ptr = super().insert(z)
        self.colors[ptr] = 1
        return ptr

    def delete(self, key):
        return super().delete(key)

    def rightRotate(self, x):
        if self.isEmpty(self.left(x)):
            print("Empty left child, leave tree unchanged")
            return
        
        y = self.left(x)
        p = self.par(x)

        # Modify the child of p into y
        if x == self.root:
            # discuss root separately, since p(root) = None
            self.root = y
        elif x == self.left(p):
            self.leftInd[p] = y
        else:
            self.rightInd[p] = y
        self.pInd[y] = p
        self.pInd[x] = y

        # Modify subtree belonging
        self.rightInd[y], self.leftInd[x] = x, self.rightInd[y]

if __name__ == "__main__":
    testT = bhTree()
    testT.insert((1, None))
    testT.insert((0, None))
    testT.insert((2, None))
    print(testT.left(testT.root), testT.right(testT.root))
    testT.rightRotate(testT.root)
    print(testT.left(testT.root), testT.right(testT.root))


        
        

