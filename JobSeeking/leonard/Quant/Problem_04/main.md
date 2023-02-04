# 问题

考虑AB两人玩一个游戏. B先从 [1, 2, ..., N] 中挑选一个数字 $x$, 然后A猜这个数字. 如果A猜中, 那么 AB的回报为 $(x, -x)$, 否则回报为 $(0, 0)$, 问最优策略

## 分析和解答

如果考虑 B 选择数字 $x$ 的概率为 $p_x$, 那么A的理想策略自然是要最大化 $\sum_x x p_x q_x$. 其中 $q_x$ 为 A 选择数字 $x$ 的概率, 事实上也就是A的决策. 从而

$$
q^* = \argmax_q \sum_x xp_x^* q_x
$$

而对于 B, 他必须最小化这个风险, 从而为

$$
p^* = \argmin_p \sum_x x p_x q_x^*
$$

而博弈均衡正是这组方程的解. 

对于 $N=2$ 的特殊情况, 策略被简化为单变量 $p, q$ 指选择数字 $1$ 的概率, 而有

$$
\begin{aligned}
p^* &= \argmin_p pq^* + 2(1-p)(1-q^*) = \argmin_p (3q^* - 2)p \\
q^* &= \argmax_q p^*q+ 2(1-p^*)(1-q) = \argmax_q (3p^* - 2)q
\end{aligned}
$$

可以看到事实上正有

$$
p^* = \begin{cases}
0 & q^* \gt 2/3 \\
1 & q^* \lt 2/3
\end{cases}, q^* = \begin{cases}
1 & p^* \gt 2/3 \\
0 & p^* \lt 2/3
\end{cases}
$$

可以看到只有一个混合Nash均衡: $(2/3, 2/3)$. 

那么现在考虑一般的情况, 令 $p_N = p$ 而 $q_N = q$, 那么

$$
\begin{aligned}
p^* &= \argmin_p E_{N-1} (1-p)(1-q^*) + N p q^* \\
q^* &= \argmax_q E_{N-1} (1-q)(1-p^*) + N q p^*
\end{aligned}
$$

其中 $E_{N-1}$ 正是对于 $N-1$ 个数时候的博弈结果中 A 的期望回报, 注意到作为零和博弈 B 的损失正是这个值. 从而我们立即发现均衡时应当有 

$$
p_N^* = q_N^* = \frac {E_{N-1}} {N + E_{N-1}}
$$

而此时的期望回报自然是

$$
E_N = \frac {N^2 E_{N-1}} {(N + E_{N-1})^2} + \frac {N E_{N-1}^2} {(N + E_{N-1})^2} = \frac {1} {\frac 1 N + \frac 1 {E_{N-1}}}
$$

或者

$$
\frac 1 {E_N} = \frac 1 N + \frac 1 {E_{N-1}}
$$

从 $E_2 = \frac 2 3$, 我们不难给出

$$
E_N = \frac 1 {1 + \frac 1 2 + \cdots + \frac 1 N}
$$

从而均衡点位置自然也是

$$
p_N^* = q_N^* = \frac {E_{N-1}} {N + E_{N-1}}
$$

其他项:

$$
p_{N-1}^* = q_{N-1}^* = \frac {N} {N + E_{N-1}} \times \frac {E_{N-2}} {N-1+E_{N-2}} ...\\
p_k^* = q_k^* = (1 - p_N^* - p_{N-1}^* - \cdots - p_{k+1}^*) \times \frac {E_{k-1}} {k + E_{k-1}} ... \\
p_1^* = q_1^* = (1 - p_N^* - p_{N-1}^* - \cdots - p_{2}^*)
$$
