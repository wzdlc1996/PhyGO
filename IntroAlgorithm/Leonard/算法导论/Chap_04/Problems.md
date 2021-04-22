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