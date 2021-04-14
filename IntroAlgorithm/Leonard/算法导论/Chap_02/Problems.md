# Problems in Chap. 02

## 2.1, 在归并排序中对小数组采用插入排序

-  a. 证明插入排序在最坏情况可以在 $\Theta(nk)$ 的时间内排序每个长度为 $k$ 的 $n/k$ 个子表
   
   注意到插入排序最坏情况的时间复杂度在 (对于长度为 $k$ 的列表) $\Theta(k^2)$. 从而可以看到对于 $n/k$ 个这样的列表时间复杂度为 $\Theta(k^2) \times n/k = \Theta(nk)$

-  b. 分治法的递归式现在成为:

   $$
   T(n) = \begin{cases}
   2 T(n/2) + \Theta(n) & n/2 \gt k \\
   k^2 & n/2 \leq k
   \end{cases}
   $$

   一如描述, 它相当于让通常的归并排序的叶子变粗. 从而这样的树的深度 $l$ 只到 $n/2^l = k$, 即 $l = \log n/k$. 而加总这些合并的时间 ($\propto n$)给出总的合并用的时间:

   $$
   t_{\textrm{merge}} = \Theta(n\log n/k)
   $$

-  c. 为使得两者拥有相同的运行时间, 我们要求:

   $$
   \Theta(n\log n) = \Theta(nk + n\log n/k) \Rightarrow k - \log k \leq c \log n\Rightarrow k \leq \Theta(\log n)
   $$

## 2.2, 冒泡排序的正确性

```python {.line-numbers}
# Bubble sort code
def bubble_sort(a_):
    a = a_.copy()
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
    return a
```

我们将通过证明5~9行的循环体满足某种循环不变式来进行证明. 

1.  研究对象的状态用第4行定义的循环指标 $i$ 来标记, 状态 $s_i$ 代表循环 $i$ 完成后的数组. 我们研究的性质是, $s_i$ 的 $i$ 个元素是 $s_i[i:]$ 中的最小值. 即它比它右边的每个元素都要小.
2.  **初始化**, 对于初始时 $i=0$, 该次循环从后往前遍历数组中所有相邻对, 如果靠后的大就交换次序. 从而使得最小的数出现在数组的最左边. 这个的证明同样可以使用循环不变式来进行, 只需要指出每次循环交换的相邻元素左边总小于右边, 从而得证左边元素小于右边所有. 
3.  **保持**, 在下次循环中, 最左边的数字是不参与计算的. 因为 $j$ 的循环范围到 $i+1$ (python中的`range`不包含右端点), 这使得上面的论证得到保持, 即数组中第二个元素是第二小的
4.  **终止**, 当 $i$ 的循环结束(它总会结束)时, 数组的元素实现了第 $i$ 位是所有元素中第 $i$ 小的. 从而排序的正确性得到证明.

## 2.4, 逆序对

一个数组 (又索引-值对 $(i, a_i), i=0,\cdots,N-1$ 定义)的 **逆序对(inversion)** 定义为如下集合的元素

$$
I(a) = \{(i,j)\in\{0,\cdots,N-1\}^{\otimes 2}: i\lt j, a_i \gt a_j\}
$$

对于集合 $\{0,\cdots,N-1\}$ 上的数组(即它的重排), 拥有最多逆序对是降序数组 $[N-1,N-2,\cdots,0]$, 此时任何两个不同元素都对应一个逆序对, 共有 $|I(a)| = C_n^2 = n(n-1)/2$ 个.

插入排序的运行时间事实上由数组中的逆序对数量决定, 由于每个循环中进行数组移位操作的时候事实上减少了一个逆序对. 

一个简单的找到数组中所有逆序对的程序

```python {.line-number}
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
```

The optimal time complexity of find the number of inversions is of $\Theta(n\log n)$, but to find all pair, one at least requires $\Theta(n^2)$, since the reversal ordering has $C_n^2$ inversion pairs.