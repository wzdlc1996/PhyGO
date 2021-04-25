# Problems in Chap. 04

## 4-6 Monge 阵列

对一个 $m\times n$ 的实数阵列 $A$, 若对所有满足 $1\leq i \lt k \leq m$ 和 $1\leq j\lt l \leq n$ 的 $i, j, k, l$ 有

$$
A_{i,j} + A_{k,l} \leq A_{i,l} + A_{k,j}
$$

则称 $A$ 是一个 **Monge 阵列(Monge array)**. 换言之, 从阵列中任意两个数, 它们作为对角线能够确定一个矩形, 则它们的和总不大于另外两个顶点对应值的和. 

### Problem 1

证明: 一个数组是 Monge 阵列当且仅当对所有 $i=1,\cdots,m-1$ 和 $j=1,\cdots, n-1$ 有

$$
A_{ij} + A_{i+1,j+1} \leq A_{i,j+1} + A_{i+1,j}
$$

其必要性是显然的, 只需要将 $i,j,k,l$ 做适当的替换即得到证明. 
考虑其充分性, 我们有

$$
\begin{aligned}
A_{ij} + A_{i+1,j+1} &\leq A_{i,j+1} + A_{i+1,j} \\
A_{i,j+1} + A_{i+1,j+2} & \leq A_{i,j+2} + A_{i+1,j+1} 
\end{aligned}
\Rightarrow
A_{i,j} + A_{i+1,j+2} \leq A_{i,j+2} + A_{i+1,j}
$$

从而递归地, 我们给出:

$$
A_{i,j} + A_{i+1,j+s} \leq A_{i,j+s} + A_{i+1,j}
$$

上式对所有合法的 $i$ 成立, 从而我们又有:

$$
A_{i+1,j} + A_{i+2,j+s}\leq A_{i+1,j+s} + A_{i+2,j} \Rightarrow A_{i,j} + A_{i+2,j+s} \leq A_{i,j+s} + A_{i+2,j}
$$

故继续递推, 我们有:

$$
A_{i,j} + A_{i+r,j+s} \leq A_{i,j+s} + A_{i+r,j}
$$

这事实上就证明了 Monge Array 的要求, 从而得证.

### Problem 2

令 $f(i)$ 表示第 $i$ 行的最左最小元素的列下标, 证明, 对任意 $m\times n$ 的 Monge 阵列, $f(1)\leq f(2) \leq \cdots \leq f(m)$

注意到

$$
f(i) = \arg \min_j A_{ij}
$$

如果一行中有多个重复元素, 则取最小的 $j$

考虑第 $1\leq i\leq m-1$ 行和 $i+1$ 行, 考虑格点 $(i, f(i)), (i+1, f(i+1))$ 构成的四边形, 假设 $f(i) \gt f(i+1)$, 则由Monge 阵列的特性:

$$
\begin{aligned}
A_{i, f(i+1)} + A_{i+1, f(i)} &\leq A_{i, f(i)} + A_{i+1, f(i+1)} 
\end{aligned}
$$

从 $f$ 函数的定义:

$$
A_{i,f(i)} \leq A_{i, f(i+1)} \ ; \ A_{i+1, f(i+1)} \leq A_{i+1, f(i)}
$$

从而同上面的不等式一同给出 $A_{i,f(i+1)}= A_{i,f(i+1)} , A_{i+1, f(i+1)} = A_{i+1, f(i)}$. 由于我们规定了 $f$ 取最左边的元素索引, 因此 必须有 $f(i) = f(i+1)$ , 这同我们的假设矛盾. 因此得证.

## Problem 3

下面是一个计算 $m\times n$ 的 Monge 阵列中每一行最左最小元素的分治算法的描述:

> 提取 $A$ 的偶数行构造子矩阵 $A'$, 递归地确定 $A'$ 每行最左最小元素, 然后计算$A$ 奇数行的最左最小元素

在偶数行的最左最小元素确定的情况下, 即 $f(i-1), f(i+1)$ 的值已知, 我们需要给出 $f(i)$ 的取值. 从 Problem 2中证明的结论我们有

$$
f(i-1)\leq f(i)\leq f(i+1)
$$

因此我们只需要找到序列 $A[i, f(i-1): f(i+1)+1]$ 中的最小元素索引. 该索引就是 $f(i)$ 的值. 其时间复杂度为:

$$
\sum_{k=0}^{\textrm{floor}(m/2) -1} O(f(2k+2) - f(2k)) + O(1) = O(f(m) - f(1)) + O(m) = O(m+n)
$$

## Problem 4

该分治算法的时间复杂度由递归式

$$
T(m,n) = \begin{cases}
T(m/2, n) + O(m+n) & m\gt 1\\
O(n) & m=1
\end{cases}
$$

其中在仅一行时, 求解最左最小元素的位置需要 $O(n)$ 的时间复杂度. 使用递归树求解该问题:

$$
\begin{aligned}
T(m,n) &= T(m/2, n) + O(m+n) \\
&= T(m/4, n) + O(m/2 + n) + O(m+n) \\
&= T(1,n) + \sum_{k=0}^{\textrm{floor}(\log m)} O(2^{-k}m +n) \\
&=O(n) + O(m+n\log m) \\
&= O(m+n\log m)
\end{aligned}
$$