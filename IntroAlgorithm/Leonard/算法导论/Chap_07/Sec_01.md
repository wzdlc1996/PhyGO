# 快速排序

对于包含 $N$ 个数的输入数组, **快速排序** 是一种最坏情况时间复杂度为 $\Theta(N^2)$ 的排序算法. 尽管如此, 它的期望时间复杂度为 $\Theta(N \log N)$ 而且其中的常数因子非常小, 因此它通常是实际排序应用中的最优选择. 此外它还能够进行原址排序. 

## 快速排序的描述

快速排序的实现如下:

```python{.line-numbers}
def quickSort(arr):
    quickSort(arr, 0, len(arr) - 1)

def quickSort(arr, i, j):
    if i < j < len(arr):
        q = parti(arr, i, j)
        quickSort(arr, i, q - 1)
        quickSort(arr, q, j)

def parti(arr, i, j):
    x = arr[j]
    s = i - 1
    for r in range(i, j):
        if arr[r] <= x:
            s = s + 1
            arr[s], arr[r] = arr[r], arr[s]
    arr[s+1], arr[j] = arr[j], arr[s+1]
    return s + 1
```