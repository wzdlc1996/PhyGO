# Problems in Chap. 05

## 概率计数

利用一个 $b$ 位的计数器(二进制), 通常最大数只能表示到 $2^b -1$. 我们接下来介绍 R. Morris 的一种概率计数法, 使得其可表示到更大的数值, 代价是一定精度损失. 

> 对 $i=0,1,\cdots, 2^b-1$, 令计数器值 $i$ 表示 $n_i$ 的计数, 其中 $n_i$ 构成了一个非负的递增序列. 假设计数器初值为 $0$, 表示计数 $n_0=0$. `increment` 计算单元工作在一个计数器上, 它以概率的方式包含值 $i$. 如果 $i=2^b-1$, 则它报告溢出错误. 否则, `increment` 以概率 $1/ (n_{i+1}-n_i)$ 把计数器增加 $1$, 而以概率 $1 - 1/(n_{i+1}-n_i)$ 保持其不变. 

对所有的 $i\geq 0$, 若选择 $n_i=i$, 则计数器就是一个普通的计数器. 但如果选择其他增加得更快的函数, 则会出现一些有趣的情形. 

### a

证明在执行 $n$ 次 `increment` 方法后, 计数器表示的数期望值正好是 $n$

考虑完成第 $k$ 次 `increment` 方法后, 计数器的值为 $X_i$. 不难看到 $\mathbb{P}(X_0=0) = 1$. 按照 `increment` 方法的规则, 我们有:

$$
X_{k+1} |_{X_k = i} = \begin{cases}
i+1 & \mathbb{P} = 1 / (n_{i+1} - n_i) \\
i & \mathbb{P} = 1- 1/(n_{i+1}-n_i)
\end{cases}
$$

从而, 我们有:

$$
\begin{aligned}
\mathbb{E}(X_{k+1}) &= \mathbb{E}_ i\Big(\mathbb{E}(X_{k+1} | X_k = i)\Big) \\
&= \mathbb{E}_i\Big(\frac {i+1} {n_{i+1}-n_i} + i(1 - \frac 1 {n_{i+1}-n_i})\Big) \\
&= \mathbb{E} \Big(\frac {1} {n_{X_k+1}-n_{X_k}} + X_k\Big)
\end{aligned}
$$

而其概率分布

$$
\begin{aligned}
\mathbb{P}(X_{k+1} = l) &= \sum_{s=0}^{\infty} \mathbb{P}(X_{k+1} = l|X_{k} = s)\mathbb{P}(X_k = s) \\
&= \frac {1} {n_{l} - n_{l-1}} \mathbb{P}(X_k = l-1) + (1-\frac 1 {n_{l+1} - n_{l}}) \mathbb{P}(X_k = l)
\end{aligned}
$$

考虑到计数事实上是计数器值的函数: $i\mapsto n_i$, 我们有:

$$
\begin{aligned}
\mathbb{E}(n_{X_{k+1}}) &= \mathbb{E}_i \Big(\frac {n_{i+1}} {n_{i+1}-n_i} + n_i(1 - \frac 1 {n_{i+1}-n_i})\Big) \\
&= \mathbb{E}_i\Big(n_i + 1\Big) \\
&= \mathbb{E}(n_{X_k}) + 1
\end{aligned}
$$

不难证得. 