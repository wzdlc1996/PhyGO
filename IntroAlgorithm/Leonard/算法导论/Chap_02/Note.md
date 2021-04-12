# 算法基础

## 插入排序与循环不变式

```python {.line-numbers}
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
```

**循环不变式** 类似数学归纳, 我们用它来证明使用了循环的算法的正确性. 循环不变式是对于某个对象的状态 $s$ 的性质 $P(s)$, 即指某个对 $s$ 的命题 $P(s)$ 的正确性. 应用循环不变式我们需要证明如下三部分:

1.  **初始化**, 在循环的第一次迭代前, $P(s)$ 为真
2.  **保持**, $P(s_{i-1}) \rightarrow P(s_{i})$
3.  **终止**, 状态序列终止时, 性质 $P$ 能够为我们提供证明算法正确性的帮助. 

在插入排序中, 这样的循环不变式是如此工作的:

1.  我们研究的主体(状态)是数组 $A$ 的子列. 在第 $i$ 次循环开始时, 它 $s$ 是 `A[:i]`, 性质为已被排序, 即 $P(s)$ 代表 $\forall m,n \lt \textrm{len}(s), m\lt n\rightarrow s_m \leq s_n $
2.  **初始化**, 在第一次循环开始时, 子列 $s$ (即`A[:1]`) 中仅含有一个元素, 性质 $P$ 满足.
3.  **保持**, 按照插入排序的算法, 第 $i$ 次的循环中的状态转移(即循环体5~10行)实现了如下的过程
    1.  变量 `key` 存放了 `A[i]` 的数值
    2.  7~9行的 `while` 循环逆序遍历了子列 $s$, 若 `A[k]` 大于 `key` 的值, 第8行便将其往后移位. 
    3.  第10行将 `key` 的值赋给循环终止时的 `i+1`, 即第一个(由于 $s$ 已被排序)不比 `key` 大的位置的后一个.
    
    从而由这样的状态转移, 如果 $s_i$ 已被排序, 则返回给出:

    $$
    s_{i+1} = (s_i^0,\cdots, s_i^k, A[i], s_i^{k+1},\cdots, s_i^{i-1})
    $$

    其中我们有 $s_i^k \leq A[i] \lt s_i^{k+1}$

    从而不难看到 $s_{i+1}$ 也是被排序的.
4.  **终止**, 当循环终止时, 我们已经遍历的整个数组, 且最终状态的状态包含了数组的所有信息. 既然它是已排序的, 我们证明了插入排序算法的正确性.

## 归并排序与分治算法分析

```python {.line-numbers}
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
```

归并排序是一种分治型算法. 子程序 `merg` 将两个排好序的数组合成一个排好序的数组, 它的时间复杂度为 $\Theta(n)$. 而归并排序本身每次都近似地将输入分成两个相近尺寸的输入并调用自己. 可以使用一种递归式来分析:

$$
T(n) = \begin{cases}
\Theta(1) & n\leq 1\\
2T(n/2) + \Theta(n) & n\gt 1
\end{cases}
$$

这种递归方程的解正是

$$
T(n) = \Theta(n\log n)
$$

从而归并排序比插入排序更快.