# 连续抛掷骰子问题合集

## 问题 01

考虑一只均匀的六面体骰子, 抛掷直到出现6为止. 问期望抛掷次数. 如果抛掷直到连续两次出现6停止, 问期望抛掷次数

### 分析和解答

对于第一问, 我们可以直接考虑第 $k$ 次才第一次得到6的概率 (令一次出现 $6$ 的概率为 $p$, 对于均匀六面体骰子显然 $p=1/6$):

$$
p_k = (1-p)^{k-1} p.
$$

从而

$$
\mathbb{E}(n) = \sum_{k=1}^\infty k p_k = \frac 1 p.
$$

或者我们可以讨论条件期望:

$$
\begin{aligned}
\mathbb{E}(n) &= p(\textrm{get 6 at 1}) \mathbb{E}(n|\textrm{get 6 at 1}) + p(\textrm{not 6 at 1})\mathbb{E}(n|\textrm{not 6 at 1}) \\
&= p \times 1 + (1-p)\times (1+\mathbb{E}(n))
\end{aligned}
$$

从而有

$$
\mathbb{E}(n) = \frac 1 p.
$$

对于第二问, 我们可以沿用条件期望的讨论方法:

$$
\begin{aligned}
\mathbb{E}(n) &= p \mathbb{E}(n|1: 6) + (1-p) \mathbb{E}(n|1: \neq 6) \\
&=p^2 \times 2 + p(1-p) (2 + \mathbb{E}(n)) + (1-p) (1 + \mathbb{E}(n))
\end{aligned}
$$

从而解出

$$
\mathbb{E}(n) = \frac {1+p} {p^2}.
$$



## 问题 02

考虑一只均匀的六面体骰子, 抛掷直到出现6为止. 问期望抛掷次数, 条件为从来没有抛掷出5


### 分析和解答

考察第 $k$ 次才得到 $6$ 的条件概率, 按照条件概率定义, 应当有:

$$
p_k = \frac {\mathbb{P}(k:6, \textrm{no }5)} {\mathbb{P}(\textrm{no } 5)} = \frac {(1-p-p)^{k-1} p} {(1-p)^k} = \frac {p} {1-p} \Big(\frac {1-2p} {1-p}\Big)^{k-1}.
$$

从而

$$
\mathbb{E}(n|\textrm{no }5) = \frac {p(1-p)} {(1-2p)^2}.
$$