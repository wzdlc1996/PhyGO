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

class rbTree(binSearchTree):
    def __init__(self):
        super().__init__()
        self.colors = []

    def setValue(self, ptr, **kwargs):
        ptr = super().setValue(ptr=ptr, **kwargs)
        if "color" not in kwargs:
            col = True
        else:
            col = kwargs["color"]
        if ptr < len(self.colors):
            self.colors[ptr] = col
        else:
            self.colors.append(col)
        return ptr

    def isBlack(self, x):
        return self.isEmpty(x) or x == self.root or self.colors[x]

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
    
    def leftRotate(self, x):
        if self.isEmpty(self.left(x)):
            print("Empty left child, leave tree unchanged")
            return
        
        y = self.right(x)
        p = self.par(x)
        
        # Modify the child of p into y
        if x == self.root:
            # discuss root separately
            self.root = y
        elif x == self.left(p):
            self.leftInd[p] = y
        else:
            self.rightInd[p] = y
        self.pInd[y] = p
        self.pInd[x] = y

        # Modify subtree belonging
        self.leftInd[y], self.rightInd[x] = x, self.leftInd[y]

    def insert_fix(self, ptr):
        # Fix the insert operation
        def isLeftChild(x):
            return x == self.left(self.par(x))
        def setBlack(x):
            self.colors[x] = True
        def setRed(x):
            self.colors[x] = False

        while not self.isBlack(self.pInd[ptr]):
            if isLeftChild(self.par(ptr)):
                y = self.right(self.par(self.par(ptr)))
                if not self.isBlack(y):
                    setBlack(self.par(ptr))
                    setBlack(y)
                    setRed(self.par(y))
                    ptr = self.par(self.par(ptr))
                elif not isLeftChild(ptr):
                    ptr = self.par(ptr)
                    self.leftRotate(ptr)
                setBlack(self.par(ptr))
                setRed(self.par(self.par(ptr)))
                self.rightRotate(self.par(self.par(ptr)))
            else:
                y = self.left(self.par(self.par(ptr)))
                if not self.isBlack(y):
                    setBlack(self.par(ptr))
                    setBlack(y)
                    setRed(self.par(y))
                    ptr = self.par(self.par(ptr))
                elif not isLeftChild(ptr):
                    ptr = self.par(ptr)
                    self.leftRotate(ptr)
                setBlack(self.par(ptr))
                setRed(self.par(self.par(ptr)))
                self.rightRotate(self.par(self.par(ptr)))
        
        setBlack(self.root)

    def insert(self, z):
        ptr = super().insert(z)
        self.setValue(ptr, color=False)
        self.insert_fix(ptr)
        return ptr
        

if __name__ == "__main__":
    testT = rbTree()
    testT.insert((1, None))
    testT.insert((0, None))
    testT.insert((2, None))
    print(testT.left(testT.root), testT.right(testT.root))
    testT.leftRotate(testT.root)
    print(testT.left(testT.root), testT.right(testT.root))
    testT.insert((10, 10))


        
        

