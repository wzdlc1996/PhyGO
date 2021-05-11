# 堆排序

## 堆排序算法

初始的时候, 我们将输入数组 `arr` 通过 `buildMaxHeap` 转换为最大堆. 此时 `arr[0]` 的元素应当是整个数组中最大的. 我们将 `arr[0]` 同 `arr[-1]` 调换位置, 从而使得它处在已排序的正确位置, 然后我们重复上面的过程, 但将输入更改为 `arr[:-1]` (这个过程可以通过更改 `arr` 对应的 `heapSize` 实现). 此时我们不需要重新调用 `buildMaxHeap` 来构造最大堆, 而只用调用 `maxHeapify(arr[:-1], 0)`. 因为根节点的子树并没有在上面的交换中发生变化. 重复这个过程直到 `heapSize` 的值为 `1`. 

其代码实现为:

```python{.line-numbers}
class heapSort:
    def __init__(self, arr):
        self.body = arr
        self.size = len(arr)

    def getSize(self):
        return self.size
    
    def maxHeapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        arr = self.body
        if l < self.size and arr[l] > arr[i]:
            largest = l
        else:
            largest = i
        if r < self.size and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        for i in range(int((len(self.body) - 1)/2), -1, -1):
            self.maxHeapify(i)
    
    def sort(self):
        self.buildMaxHeap()
        for i in range(len(self.body)-1, 0, -1):
            self.body[0], self.body[self.getSize()-1] = self.body[self.getSize()-1], self.body[0]
            self.size -= 1
            self.maxHeapify(0)
        return self.body
```

我们来分析堆排序的算法复杂度. 由于全部操作均是空间原址的, 因此空间复杂度为 $\Theta(1)$. 我们来分析其时间复杂度. 

1.  28行的建堆过程, 其时间复杂度为 $O(N)$
2.  29行开始的 `for` 循环, 总的时间复杂度应为

    $$
    \sum_{i=N-1}^{1} O(\log i) \leq \int_2^N \log x\td x =O(N\log N)
    $$

从而算法的时间复杂度为 $O(N\log N)$. 