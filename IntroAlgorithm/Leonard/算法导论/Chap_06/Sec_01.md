# 堆排序(Heap Sort)

**排序问题** 描述了如下问题:

-  **Input**: 拥有 $N$ 个数的序列 $(a_0,\cdots,a_{N-1})$
-  **Output**: 这些数的一个排列 $(a_0',\cdots,a_{N-1}')$, 使得 $a_i'\leq a_{i+1}'$

实际的数据结构中要排序的变量很少是单独的数值, 而是数据的一个元素. 当数据很大时, 我们通常是通过排序指针来避免大规模数据移动的. 这也是算法和程序的区别, 算法层面我们不考虑这些细节而直接把问题抽象为数值序列. 

**堆排序(heapsort)** 在时间复杂度上类似于归并排序, 为 $O(n\log n)$. 而在另一方面类似插入排序, 它是 "空间原址" 的, 即 任何时候都只需要常数个额外的元素空间存储临时数据. 

## 堆

**(二叉)堆** 是一个数组, 可以被看作为一个近似的完全二叉树. 

![](https://upload.wikimedia.org/wikipedia/commons/3/38/Max-Heap.svg)

如图就是一个 **最大二叉堆(max binary heap)** 的两种表示. 通常的堆有如下的性质:

1.  它将数组的元素从顶往下, 从左往右依次摆放成为树
2.  在二叉的情形下, 索引为 `i` 个元素的左子元素索引为 `2*i`, 右子元素为 `2*i+1`, 其父节点索引为 `floor(i/2)`. 

二叉堆有两种形式:

1.  **最大堆** 满足 `a[parent(i)] >= a[i]`, 即任意节点的父节点的数值都不比其小.
2.  **最小堆** 满足 `a[parent(i)] <= a[i]`. 

本章的剩余部分中我们介绍如下过程, 以及如何在堆排序和优先队列中使用它们

1.  `maxHeapify`, 其时间复杂度为 $O(n \log n)$, 它是维持最大堆性质的关键
2.  `buildMaxHeap`, 它具有线性时间复杂度来从无序数组生成一个最大堆
3.  `heapSort`, 时间复杂度为 $O(n\log n)$, 它对一个数组进行原址排序
4.  `maxHeapInsert`, `heapExtractMax`, `heapIncreaseKey`, 和 `heapMaximum`, 它们利用堆来实现一个优先队列.

## 维护堆的性质

我们来介绍 `maxHeapify` 的实现, 它是维护堆为一个最大堆的重要过程. 其输入为一个数组 `arr` 和一个下标 `i`, 在调用 `maxHeapify` 是, 我们假定了根节点为 `left(i)`, `right(i)` (即节点 `i` 的左右子节点)的子堆均为最大堆, 但这时 `arr[i]` 可能会小于其子节点. 而 `maxHeapify` 过程就是不断调整 `arr[i]` 的值(在数组中不断交换其位置), 来保证它引导的子堆是一个最大堆. 我们需要让 `arr[i]` 在堆中逐级下降直到它处在一个合理的位置. 

```python{.line-numbers}
def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def heapSize(arr):
    return int(log2(len(arr)))

def maxHeapify(arr, i):
    l = left(i)
    r = right(i)
    if l <= heapSize(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= heapSize(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest)
```

我们来分析这个实现.

1.  1-9行实现的这些函数是为了方便把数组作为堆来进行处理
2.  11-18行比较了节点 `i, l, r`. 找到了其中最大的元素并将其索引赋值给 `largest`. 
3.  19行的 `if` 分支在 `largest` 等于 `i` 时不会运行, 因为此时按照我们的假设(`i` 的子结点开始的子树是最大堆), `i` 引导的子堆自然为最大堆
4.  20行对换了 `arr[i]` 和 `arr[largest]` 的值, 事实上就是将 `arr[i]` 和它最大的子结点之间进行了对换.
5.  21行递归的再次调用 `maxHeapify` 方法, 这使得子堆也将保持最大堆性质. 