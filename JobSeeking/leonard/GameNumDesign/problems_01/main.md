# Problems, at 22-03-15

## Problem 1

考虑一种抽卡机制, 每次抽到稀有度A类的物品概率为 $p$. 如果前 $m$ 次连续没有抽到A, 那么下一次必定获得. 

可以对这个问题进行模拟, 见 `./problem01.py`

数学上来考虑平均抽取A的概率或平均抽数可以考虑到在大规模抽取的极限情况下, 我们可以按照 $m+1$ 次抽取这一个周期来考虑结果, 对精确结果的偏差会逐渐变小. 因此考虑事件 "第$n$次才抽到A" 的概率 $p_n = \mathbb{P}(X_n=1, X_{n-1,\cdots,1}=0)$, 由于:

$$
\mathbb{P}(X_n=1| X_{n-1,\cdots,1}=0) = \begin{cases}
\mathbb{P}(X_n=1| X_{n-1,\cdots,1}) =p & n \leq m \\
1 & n = m
\end{cases}
$$

从而

$$
\begin{aligned}
p_1 &= p \\
p_2 &= \mathbb{P}(X_2=1|X_0=0)\mathbb{P}(X_0=0) = p(1-p) \\
p_3 &= p (1-p)^2 \\
\cdots & \\
p_m &= p (1-p)^{m-1} \\
p_{m+1} &= (1-p)^m
\end{aligned}
$$

这同样是大规模抽取历史中出现这样的序列的概率. 那么考虑这样的大规模抽取历史, 以 $(0,\cdots,0,1)$ 为模式进行划分 (代表连续出现非A最后出现一个A), 那么出现有 $i-1$ 个 0 的序列的概率应为 $p_{i}$. 因而平均抽取概率应当有:

$$
\bar{p} = \frac {\#(A)} {N} = \frac {1} {\sum_{l=1}^{m+1} l p_l}
$$

因此应当有平均抽数:

$$
\bar{n} = \sum_{l=1}^{m+1} l p_l = \frac {1-(1-p)^{m+1}} {p}
$$

对于模拟的 $p=0.1, m=9$, 应当有 $\bar{n} = 6.51322$, 换言之平均概率应为 $\bar{p} \sim 1/\bar{n} = 0.153534$, 同数值模拟一致. 

## Problem 2

考虑两种副本奖励机制:
-  a) 以 $p_1$ 的概率掉落战利品A, 以 $p_2$ 概率掉落B, $1-p_1-p_2$ 概率一无所获
-  b) AB的掉落独立为 $p_1, p_2$. 

试计算平均刷取次数以获得两种战利品. 

ab两种模式事实上是一致的, 区别就在于刷本的四种可能状态: $(AB, A, B, 0)$ 的概率分布. a机制为 $(0, p_1, p_2, 1-p_1-p_2)$, 而 b机制为 $(p_1p_2, p_1(1-p_2), p_2(1-p_1), (1-p_1)(1-p_2))$. 在接下来我们讨论普遍的 $(x, y, z, w)$ 的情况, 注意 $x+y+z+w=1$

考虑事件直到第 $n$ 次才刷齐, 那么根据前面的战利品情况可以分为三种可能:
1.  此前一直是一无所获, 那么要求最后一次出现 AB
2.  此前未获得过B, 但不是一无所获, 那么要求最后一次出现 AB + B
2.  此前未获得过A, 但不是一无所获, 那么要求最后一次出现 AB + A

故应有:

$$
p_n = w^{n-1} x + \Big((1-x-y)^{n-1} - w^{n-1}\Big) (x + z) + \Big((1-x-z)^{n-1} - w^{n-1}\Big) (x + y)
$$

因而平均刷本次数为

$$
\bar{n} = \sum_{n=1}^{\infty} n p_n = \frac 1 {x+y} + \frac 1 {x + z} - \frac {1} {1 - w}
$$

另一种可以考虑事件直到第 $n$ 次副本才刷齐, 根据最后一次出现战利品的情况可以分为三种可能性:
1.  AB: 那么要求前面$n-1$次从没出过A, 或者从没出过B
2.  A: 那么要求前面 $n-1$ 次没出过A但出过B
3.  B: 那么要求前面 $n-1$ 次没出过B但出过A

故应有:

$$
p_n = x \Big((1-x-y)^{n-1} + (1-x-z)^{n-1} - w^{n-1}\Big) + y ((1-x-y)^{n-1} - w^{n-1}) + z((1-x-z)^{n-1} - w^{n-1})
$$

可以看到这两种计算方法是一致的, 其本质在于

$$
\begin{aligned}
\mathbb{P}(n\textrm{ reach}) &= \sum_{E\in \{AB,A,B\}}\mathbb{P}(n\textrm{ reach}~\wedge~n:E) \\
&=\sum_{E\in \{0^{n-1}, B^k, A^k\}}\mathbb{P}(n\textrm{ reach}~\wedge~n-1,\cdots,1: E)
\end{aligned}
$$

数值模拟也肯定了我们的推导: `./problem02.py`

## Problem 3

一种强化模型. 考虑从等级 $i$ 变为 $j$ 的概率为 $p_{ji}$, 计算平均多少次可以强化到最大值 $N$. 其中 $i,j \leq N$. 

这是一个简单的 Markov chain 停时问题. 我们可以考虑第 $n$ 次未经过$N$到达 $j$ 概率为 $P_{n,j}=\mathbb{P}(X_n=j|X_{n-1,\cdots}\neq N)$. 那么应当有递推关系:

$$
\begin{aligned}
P_{n+1, j} &= \mathbb{P}(X_{n+1}=j|X_{n}\neq N, X_{n-1,\cdots}\neq N) \\
&= \sum_{l\neq N}\mathbb{P}(X_{n+1}=j|X_n = l) \mathbb{P}(X_n=l|X_n\neq N, X_{n-1,\cdots}\neq N) \\
&=\sum_{l\neq N} p_{j, l} \mathbb{P}(X_n=l| X_{n-1,\cdots}\neq N) \\
&=\sum_{l\neq N} p_{j,l} P_{n,l}
\end{aligned}
$$

注意到 $P_{1,l}$ 是初始条件, 而我们想知道的第$n$次才强化到最大值的概率正是 $P_{n,N}$, 从而得到求解.
