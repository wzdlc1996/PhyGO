# 随机过程相关

## 问题 01

考虑一个随机循环的播放器, 共有 $N$ 首歌, 有放回的随机播放, 问首次遍历一遍的次数的期望值

该问题同样有众多刷本集齐装备的期望次数的变形.

### 分析和解答

本题可以通过合适的变形转化为一个Markov chain的计算问题. 考虑第 $t$ 次播放后已经遍历过的歌曲数目为 $N_t$ , 那么事实上就有

$$
\begin{aligned}
\mathbb{P}(N_{t+1} = x+1 | N_t = x) &= \frac {N - x} {N} \\
\mathbb{P}(N_{t+1} = x | N_t = x) &= \frac x N
\end{aligned}
$$

从而问题也就成为了计算随机变量 $T = \min \{t: N_t = N\}$ 的期望. 

对于 Markov chain, 转移 $i\rightarrow j$ 的平均首次到达时间 $\tau_{ij} = \mathbb{E}\min\{t: X(0) = i, X(t) = j, X(s\lt t) \neq j\}$ 满足自洽方程:

$$
\begin{aligned}
\tau_{ij} &= P_{i\rightarrow j} + \mathbb{E}(\mathbb{E}(\tau-1|X(1) = k\neq j, X(\tau) = j) + 1) \\
&= P_{i\rightarrow j} + \sum_{k\neq j} (1+\tau_{kj}) P_{i\rightarrow k} \\
&=_{\tau_{jj} = 0} \sum_{k} (1 + \tau_{kj}) P_{i\rightarrow k} \\
&= 1 + \sum_k \tau_{kj} P_{i\rightarrow k}
\end{aligned}
$$

令 $t_k$ 代表从状态 $k$ 转移到 $N$ 的平均时间, 因此 $\mathbb{E}(T) = t_0$. 而有

$$
t_{N-1} = 1 + P_{N-1\rightarrow N-1} t_{N-1} + P_{N-1\rightarrow N} \times 0 = 1 + \frac {N-1} {N} t_{N-1} \Rightarrow t_{N-1} = N
$$

类似的有

$$
t_{N-2} = 1 + \frac {N-2} N t_{N-2} + \frac 2 N t_{N-1} \Rightarrow t_{N-2} = \frac N 2 + t_{N-1}
$$

进而

$$
t_0 = 1 + t_1 = 1 + \frac N {N-1} + t_2 =\cdots = \sum_{k=0}^{N-1} \frac N {N-k}
$$

## 问题 01_01

考虑一个掉落 $N$ 种装备的副本, 每种装备的掉落概率为 $p_i, i=1,\cdots,N$, 问反复刷取拿到全部装备的期望次数. 

### 分析和解答

是类似问题01的问题. 但由于装备存在多种导致其状态空间的大小变得更大, 更加难以计算. 但分析的思路是一样的. 一般的, 对于 $N$ 种装备状态空间的大小为 $2^N$. 可以想像这些状态分布在一个 $N$ 维单位立方体上, 而我们的目的正是从点 $(0,\cdots,0)$ 计算到体对角线相连的点 $(1,\cdots,1)$. 从而

$$
\begin{aligned}
T_{\bm{0}\rightarrow\bm{1}} &= 1 + \sum_{i=1}^N p_i T_{\bm{e}_i\rightarrow \bm{1}} \\
&= 1 + \sum_{i=1}^N \frac {p_i} {1-p_i}\Big(1 + \sum_j p_j T_{e_{ij}\rightarrow \bm{1}}\Big) \\
&= 1 +\sum_i \frac {p_i} {1-p_i}\Big(1 + \sum_{j\neq i} \frac {p_j} {1-(p_i+p_j)}(1+\sum_{k\neq i, j} p_k T_{ijk\rightarrow \bm{1}})\Big) \\
&=1 + \sum_i \frac {p_i} {1-p_i} + \sum_{i, j\neq i}\frac {p_ip_j} {(1-p_i)(1-p_i-p_j)} \\
&+ \sum_{i, j\neq i, k\neq i, j}\frac {p_ip_jp_k}{(1-p_i)(1-p_i-p_j)(1-p_i-p_j-p_k)} + \cdots
\end{aligned}
$$

求和的序列共有 $N$ 项.

## 问题 01_02

考虑一个抽卡系统, 每次抽取到角色的概率为 $p$, 如果连续 $N-1$ 次没有获得, 则下一次必定出现该角色. 问平均抽取角色需要的次数

### 分析和解答

考虑在当前规则下的平均抽取次数为 $f(N)$, 那么显然由条件期望:

$$
f(N) = \mathbb{P}(第一次抽到) \times 1 + \mathbb{P}(第一次没抽到) (1+f(N-1)) = 1 + (1-p) f(N-1)
$$

显然, 我们有 $f(1) = 1$. 从而

$$
f(N) + k = 1 + k +(1-p)f(N-1) =(1-p) \Big(f(N-1)+ \frac {1+k} {1-p} \Big).
$$

令 $k = -1/p$, 我们给出

$$
f(N) - 1/p = (1-p)^{N-1} (f(1) - 1/p) = -\frac 1 p (1-p)^{N}
$$

即

$$
f(N) = \frac {1 - (1-p)^N} p
$$

当然这个问题还有另一种解决方案, 我们可以直接计算 $k$ 次才抽出角色的概率

$$
p_k = \begin{cases}
(1-p)^{k-1} p & k\lt N \\
(1-p)^{N-1} & k = N
\end{cases}
$$

从而不难验证

$$
f(N) = \sum_{k=1}^N p_k k = \frac {1 - (1-p)^N} p.
$$


## 问题 02

考虑52张牌, 26张黑色和26张红色, 均匀打乱. 定义 block 为连续同色的一个最大子串, 如序列 `01000110` 共有5个block, 对应 `0`, `1`, `000`, `11`, `0`. 问block个数的期待值

### 分析和解答

本题可以推广为考虑 $n$ 个 0 和 $m$ 个 1 的bitstring中的block数目的期待值. 

考虑位置 $i$ 处卡牌的颜色为 $c_i$, 显然 $c_i\in\{0, 1\}$. 对于均匀大乱, 我们可以计算某个位置和其后一个位置颜色不同的概率分布(注意 $c_i$ 彼此之间并不独立):

$$
\begin{aligned}
\mathbb{P}(c_{i+1}\neq c_i) &= \mathbb{P}(c_{i+1}=1, c_i=0) + \mathbb{P}(c_{i+1}=0, c_i=1) \\
&=\frac {C_n^1 C_m^1 A_{m+n-2}^{m+n-2}} {A_{m+n}^{m+n}} + (m\leftrightarrow n) \\
&= \frac {2mn} {(m+n)(m+n-1)}
\end{aligned}
$$

注意到 block 的数量满足

$$
\#\textrm{block} = \sum_{i=1}^{n+m - 1}1_{c_{i+1}\neq c_i} + 1,
$$

从而

$$
\mathbb{E}(\#\textrm{block}) = 1+\sum_{i=1}^{n+m-1} \mathbb{E}(1_{c_{i+1}\neq c_i}) = 1 + (n+m-1)\cdot \frac {2mn} {(m+n)(m+n-1)} \\
=1 + \frac {2mn} {m+n}
$$

对于 $m=n=26$ 的特殊情况, 有 $\mathbb{E}(\#\textrm{block}) = 27$

## 问题 03

考虑一只股票, 初识时价格为 25. 每天有 $55\%$ 概率提高1, $45\%$ 概率降低1. 策略为高等于40卖出, 低于等于10卖出. 问赚到钱的概率. 

该问题同样有众多强化问题期望次数的变形.

### 分析和解答

该问题事实上是Markov chain的条件概率问题. 不妨假设初始价格 $v_0$, 上下界为 $u, d$. +1的转移概率为 $p$. 那么在这个策略下的转移方程事实上正是:

$$
\mathbb{P}(v_{t+1} = x|v_{t}) = \begin{cases}
\delta_{x,u} & v_t = u \\
\delta_{x,d} & v_t = d \\
p\delta_{x, v_t+1} + (1-p)\delta_{x, v_t-1} & \textrm{otherwise}
\end{cases}.
$$

从而赚钱概率正是

$$
\mathbb{P}(v_0 \rightarrow u).
$$

不妨考虑普遍的 $p_x = \mathbb{P}(x\rightarrow u)$, 从而有自洽方程:

$$
p_x = \sum_y \mathbb{P}(x\rightarrow y) \mathbb{P}(y\rightarrow u) = \sum_y \mathbb{P}(x\rightarrow y) p_y.
$$

为此我们需要计算转移概率矩阵的本征值为1的本征向量. 数值计算自然不难, 这里给出一种解析求解的办法:

注意到 $p_u = 1, p_d = 0$, 从而

$$
p_x = p p_{x+1} + (1-p)p_{x-1} \Rightarrow p_x = C_1\lambda_1^x + C_2\lambda_2^x.
$$

带入方程给出

$$
1 = p \lambda + (1-p)\frac 1 \lambda \Rightarrow \lambda = 1, \frac {1-p} p 
$$

从而一般解应当有 $p_x = C_1 + C_2 (\frac {1-p} p)^x\equiv C_1 + C_2 \lambda^x$. 带入边条件给出

$$
\begin{aligned}
C_1 + C_2 \lambda^u &= 1 \\
C_1 + C_2 \lambda^d &= 0
\end{aligned}\Rightarrow 
\begin{cases}
C_1 = - \frac {\lambda^d} {\lambda^u - \lambda^d}\\
C_2 = \frac 1 {\lambda^u - \lambda^d}
\end{cases}
$$

从而我们能够计算出原问题的答案

$$
P = \frac {\lambda^{v_0} - \lambda^d} {\lambda^u - \lambda^d} = 95.3\%.
$$

## 问题 03_01