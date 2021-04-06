# 算法基础

## 插入排序与循环不变式

插入排序:

```python {.line-numbers}
def insert_sort(input_array: list):
    A = input_array.copy()
    for i in range(1, A):
        key = A[i]
        i = j - 1
        while (i > 0 and A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A
```