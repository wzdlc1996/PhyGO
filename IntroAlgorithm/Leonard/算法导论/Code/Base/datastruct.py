#!/usr/bin/env python

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

    def setValue(self, ptr, **kwargs):
        k = kwargs["key"]
        v = kwargs["value"]
        l = kwargs["left"]
        r = kwargs["right"]
        p = kwargs["parent"]
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

        ptr = self.setValue(
            ptr=-1, 
            key=key, 
            value=val, 
            left=None, 
            right=None, 
            parent=y
        )
        
        if y is None:
            self.root = 0
        else:
            if key < self.key[y]:
                self.leftInd[y] = ptr
            else:
                self.rightInd[y] = ptr

        return ptr

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
        return ptr