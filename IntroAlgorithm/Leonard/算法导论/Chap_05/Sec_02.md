# 概率分析和随机算法

## 指示器随机变量

指示器随机变量事实上就是一种指示函数. 不严格地描述为

$$
I(A) = \begin{cases}
1 & \textrm{ if } A \textrm{ happens}\\
0 & \textrm{otherwise}
\end{cases}
$$

它的一个重要性质为:

$$
\mathbb{E}(I(A)) = \mathbb{P}(A)
$$

## 随机算法分析

### 雇佣问题的平均复杂度

我们来考察雇佣问题的平均复杂度. 这里我们使用指示器变量, 将之定义为:

$$
X_i = \begin{cases}
1 & i \textrm{ -th variable to update}\\
0 & \textrm{otherwise}
\end{cases}
$$

从而, 按照我们之前的分析, 时间复杂度正比于更新次数, 我们有:

$$
\begin{aligned}
\mathbb{E}T(n) &= \mathbb{E}\Big\{c \sum_{i=0}^{N-1} X_i\Big\} \\
&= c \sum_{i=0}^{N-1} \mathbb{E} X_i \\
&= c \sum_{i=0}^{N-1} \mathbb{P}(i)
\end{aligned}
$$

其中, $\mathbb{P}(i)$ 为第 $i$ 个变量需要更新的概率, 换言之, 即第 $i$ 个变量比前面每个元素都大的概率. 由于数组是均匀随机的, 这个概率事实上是 $1/(i+1)$. 更详细的推导如下, 考虑数组是 $\{0,1,\cdots, N-1\}$ 的随机置换.

$$
\begin{aligned}
\mathbb{P}(i) &= \sum_{j=0}^{N-1} \mathbb{P}(a_i = j \textrm{ and } \max_{k\lt i} a_k \lt j) \\
&= \sum_{j=0}^{N-1} \frac {1} {N!} A_{j}^{i} A_{N-1-i}^{N-1-i} \\
&= \sum_{j=i}^{N-1} \frac 1 {N!} \frac {j!} {(j-i)!} (N-1-i)! \\
\end{aligned}
$$

其中

$$
\sum_{j=i}^{N-1} \frac {j!} {(j-i)!} = \sum_{l=0}^{N-1-i} \frac {(l+i)!} {l!}
$$

我们来证明:

$$
\sum_{l=0}^{n} \frac {(l+i)!} {l!} = \sum_{l=0}^n \prod_{k=1}^i (l+k) = \frac {(i+n+1)!} {(i+1) n!}
$$

显然, $n=0$ 时, 我们有 $\textrm{l.h.s.}=i!=(i+1)!/(i+1) = \textrm{r.h.s.}$. 我们假设它对于所有 $n\leq m$ 的 $n$ 都成立, 我们考察 $n=m+1$ 的情形:

$$
\begin{aligned}
\sum_{l=0}^{m+1} \frac {(l+i)!} {l!} &=\sum_{l=0}^m \frac {(l+i)!} {l!} + \frac {(m+1+i)!} {(m+1)!} \\
&= \frac {(i+m+1)!} {(i+1)m!} + \frac {(m+1+i)!} {(m+1)!}\\
&= \frac {(i+m+1)!\times (m+1+i+1)} {(i+1)(m+1)!}\\
&= \frac {(i+m+2)!} {(i+1)(m+1)!}
\end{aligned}
$$

正是所证. 从而原命题得证. 从而:

$$
\mathbb{P}(i) = \frac {(N-1-i)!} {N!} \frac {(i+1+N-1-i)!} {(i+1)(N-1-i)!} = \frac 1 {i+1}
$$

从而, 我们有雇佣问题的平均复杂度:

$$
\mathbb{E} T(n) = c\sum_{i=0}^{N-1}\frac 1 {i+1} = c\log n + O(1)
$$
