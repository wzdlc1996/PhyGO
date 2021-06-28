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

    def setValue(self, **kwargs):
        ptr = super().setValue(**kwargs)
        if "color" not in kwargs:
            col = 1
        else:
            col = kwargs["color"]
        if ptr < self.size:
            self.colors[ptr] = col
        else:
            self.colors.append(col)

    def insert(self, z):
        ptr = super().insert(z)
        self.colors[ptr] = 1
        return ptr

    def delete(self, key):
        return super().delete(key)
        

