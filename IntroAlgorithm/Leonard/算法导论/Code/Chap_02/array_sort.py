#!/usr/bin/env python3

import random

# insertion sort
def insert_sort(input_array: list):
    A = input_array.copy()
    for i in range(1, len(A)):
        key = A[i]
        i = i - 1
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

# merge two sorted array
def merg(a, b):
    res = [0] * (len(a) + len(b))
    i_a = 0
    i_b = 0
    i_res = 0
    while(i_a < len(a) and i_b < len(b)):
        if a[i_a] < b[i_b]:
            res[i_res] = a[i_a]
            i_a += 1
        else:
            res[i_res] = b[i_b]
            i_b += 1
        i_res += 1
    if i_a == len(a):
        res[i_res:] = b[i_b:]
    else:
        res[i_res:] = a[i_a:]
    return res

# merge sort
def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        flip = int(len(a) / 2)
        p1 = merge_sort(a[:flip])
        p2 = merge_sort(a[flip:])
        return merg(p1, p2)

# bubble sort
def bubble_sort(a_):
    a = a_.copy()
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
    return a

def test_sort(input_array: list):
    check = True
    for i in range(len(input_array) - 1):
        check = check and (input_array[i] <= input_array[i+1])
    return check

def main(sortfunc):
    for i in range(10):
        test_a = [0] * i
        for l in range(len(test_a)):
            test_a[l] = random.randint(0, 10)
        print("Test {}: {}; input:{}, output:{}".format(i, 
            test_sort(sortfunc(test_a)),
            test_a,
            sortfunc(test_a)
        ))

if __name__ == "__main__":
    print("Test: insert_sort")
    main(insert_sort)
    print("------------------------------")
    print("Test: merge_sort")
    main(merge_sort)
    print("------------------------------")
    print("Test: bubble_sort")
    main(bubble_sort)

        
