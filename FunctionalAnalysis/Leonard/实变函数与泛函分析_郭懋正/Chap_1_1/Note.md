# Note for Chapter 1.1

## 上极限与下极限

_[Definition]_ : **上确界(supremum)** 被定义在实数域 $\mathbb{R}$ 的子集 $E$ 上. 实数 $h \in \mathbb{R}$ 被称作集合 $E$ 的上确界, 如果下面两个命题为真
1.  $\forall x \in E : x \leq h$
2.  $(\forall h' \in \mathbb{R}: (\forall x \in E : x \leq h')) : h'\geq h$

此时我们记 $h = \sup E$ 同理可以定义 **下确界(infimum)**, 只需修改不等号方向. 下确界记为 $\inf \cdot$

_[Definition]_ : **上(下)极限(limit superior/inferior)** 被如下计算: 对于 $\mathbb{R}$ 中的序列 $\{x_n\}$, 定义如下两个序列:

$$
h_n = \sup\{x_k: k\geq n\} \ ; \ m_n = \inf\{x_k: k\geq n\}
$$

那么我们定义上/下极限:

$$
\limsup x_n = \lim h_n \ ; \ \liminf x_n = \lim m_n
$$


## 集合的上下极限

通过定义集合的特征函数:

$$
\chi_A(x) = \begin{cases}
1 & x \in A \\
0 & x \notin A
\end{cases}
$$

可以表示出集合的上下极限, 为:

$$
\begin{aligned}
\limsup \chi_{A_n} &= \chi_{\limsup A_n} \\
\liminf \chi_{A_n} &= \chi_{\liminf A_n}
\end{aligned}
$$

同样的, 有时集合的上下极限也被定义为:

$$
\begin{aligned}
\limsup A_n &= \bigcap_{m=1}^{\infty} \bigcup_{n=1}^m A_n \\
\liminf A_n &= \bigcup_{m=1}^\infty \bigcap_{n=1}^m A_n
\end{aligned}
$$

我们来证明这两种定义的等价性.

考虑上极限:

$$
\begin{aligned}
\limsup \chi_{A_n}(x) &= \lim_{n\rightarrow \infty} \sup\{\chi_{A_m}(x) : m \geq n\} \\
&= \lim_{n\rightarrow \infty} 
\begin{cases}
1 & x\in \cup_{m\geq n} A_m  \\
0 & x \notin \cup_{m\geq n} A_m
\end{cases} \\
&= \begin{cases}
1 & x \in \cap_n \cup_{m\geq n} A_m \\
0 & x \notin \cap_n \cup_{m\geq n} A_m 
\end{cases} \\
&= \chi_{\cap_n \cup_{m\geq n} A_m} (x)
\end{aligned}
$$

需要注意到

$$
R_n =\bigcup_{m\geq n} A_m
$$

对于指标 $n$ 是一个降列, 即 $n_1 \leq n_2 : R_{n_1} \supset R_{n_2}$. 因此若 $x$ 非其交中的元素, 那么函数序列极限必定是 0, 否则为1. 因此我们得证. 下极限的证明是类似的.