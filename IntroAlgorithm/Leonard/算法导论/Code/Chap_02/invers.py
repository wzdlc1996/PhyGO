#!/usr/bin/env python3

import random

def findMutInv(a, b):
    aind = a.copy()
    bind = b.copy()
    aind.sort()
    bind.sort()
    invList = []
    a_pos = 0
    b_pos = 0
    for _ in range(len(a) + len(b)):
        if a_pos == len(a) or b_pos == len(b):
            """
            If one needs only the number of inversions, 
            this part can be optimized into of O(n):
            by adding the counter with len(bind) * (len(aind) - a_pos - 1)
            """
            if b_pos == len(b):
                for x in aind[a_pos+1:]:
                    for y in bind:
                        invList.append((x[1], y[1]))
            break

        x = aind[a_pos]
        y = bind[b_pos]
        if x[0] > y[0]:
            invList.append((x[1], y[1]))
            b_pos += 1
        else:
            a_pos += 1
    return invList
    
def findInvIter(a: list):
    if len(a) <= 1:
        return []
    spl = int(len(a) / 2)
    a_left = a[:spl]
    a_right = a[spl:]
    return findInvIter(a_left) + findInvIter(a_right) + findMutInv(a_left, a_right)

def findInv(a:list):
    indized = [(a[i], i) for i in range(len(a))]
    return findInvIter(indized)

def main():
    testr = list(range(10))
    #testr.reverse()
    print(testr)
    print(len(findInv(testr)))
    print(10 * (10-1) /2)

if __name__ == "__main__":
    main()
    







