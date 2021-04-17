# 分治策略

## 最大子数组问题

最大子数组问题描述为:

-  **Input**:
   给定长度为 $N$ 的数组 `a`, 
-  **Output**:
   数组起点 `i` 和长度 `l` 使得 `a[i:i+l]` 是所有可能配置里和最大的.

数学的写法为

$$
\begin{aligned}
\textrm{maximize}\indent & \sum_{k=i}^{i+l-1} a_k \\
\textrm{subject to}\indent & 0\leq i \leq i+l \lt N
\end{aligned}
$$

1.  **暴力穷举**
    
    该算法通过枚举所有可能的 $i, l$ 并求和然后给出其中最大的. 其时间复杂度来自于
    1.  所有可能的 $i,l$ 对, 共 $n_1 = \sum_{i=0}^{N-1} \sum_{l=1}^{N-i-1}1 = (N-1)(N-2)/2$
    2.  对所有可能的子数组求和, 需要执行的加法计算为 $n_2 = \sum_{i=0}^{N-1} \sum_{l=1}^{N-i-1} l \in \Theta(n^3)$

    从而, 该算法的时间复杂度应当为 $\Theta(n^3)$.

    如下我们给出一个`python`实现. 
    
    ```python
    def brute_force(arr: list):
        ansDict = {}
        N = len(arr)
        for i in range(N):
            for l in range(1, N - i + 1):
                ansDict[(i,l)] = sum(arr[i:i+l])
        sumChecker = arr[0]
        kRig = (0, 1)
        for k in ansDict:
            if ansDict[k] > sumChecker:
                sumChecker = ansDict[k]
                kRig = k
        return kRig, sumChecker
    ```
    
2.  **迭代方法**

    考虑 $i$ 给定的情况, 这时最大的子数组应当从 $i+1$ 为起点开始向右找到最大的子数组. 因此我们可以得到如下的迭代形式.
    1.  定义函数

        $$
        f(\{a_k\}_{k=0}^{N-1}) = \sum_{k=0}^{l} a_k \ , \ \textrm{in which }l = \arg\max_{0\leq l\lt N} \sum_{k=0}^l a_k
        $$

    2.  函数 $f$ 满足如下的递归形式:
        
        $$
        f(a[k:]) = \max\{a[k] + f(a[k+1:]), a[k]\}
        $$

        以及初始状态

        $$
        f(a[N-1:]) = a[N-1]
        $$

    3.  从而, 我们从右往左循环遍历数组, 每个循环确认从索引 $i$ 开始的最大子数组. 当循环终止时我们就得到了关于 $i$ 的列表. 访问列表找到最大的元素即可得到. 实际实现时可以让函数 $f$ 同时返回取值的 $l$, 从而得到输出. 
    
    迭代方法的一个`python`实现
    
    ```python
    def iter_method(arr: list):
        valist = [(0,0)] * len(arr)
        valist[-1] = (arr[-1], 1)
        for k in range(len(arr) - 2, -1, -1):
            tester = arr[k] + valist[k+1][0]
            if tester > arr[k]:
                valist[k] = (tester, valist[k+1][1] + 1)
            else:
                valist[k] = (arr[k], 1)
        sumChecker = arr[0]
        kRig = (0, 1)
        for k in range(len(valist)):
            if valist[k][0] > sumChecker:
                sumChecker = valist[k][0]
                kRig = (k, valist[k][1])
        return kRig, sumChecker
    ```
    
    