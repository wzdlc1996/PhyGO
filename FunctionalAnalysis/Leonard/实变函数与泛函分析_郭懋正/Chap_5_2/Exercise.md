# Exercise in Chap. 5.2

## 6

### Problem 

$M, N$ 是 Hilbert 空间的子集, 求证:
1.  $M\subset N \Rightarrow N^\bot \subset M^\bot$
2.  $(M^\bot)^\bot = \textrm{cl }\textrm{span} M$
其中 $\textrm{cl}$ 指集合的闭包.

### Proof

对第一个命题

我们有: $M^\bot = \{x: \forall y \in M: (x,y) = 0\}$. 从而如果 $M\subset N$:

$$
\forall x \in N^\bot: \forall y \in N: (x,y) = 0 \Rightarrow \forall y \in M: (x,y) = 0\Rightarrow x \in M^\bot
$$

从而 $N^\bot \subset M^\bot$

对第二个命题

有:

$$
\begin{aligned}
(M^\bot)^\bot &= \Big(\{x: \forall y \in M: (x,y) = 0\}\Big)^\bot\\
&=\{x: \forall z \in M^\bot: (x,z) = 0\} \\
&\supset \textrm{span} M
\end{aligned}
$$

由于 $\forall x, y\in M, z\in M^\bot: (z,x+y) = (z,x)+(z,y)=0\Rightarrow x+y \in (M^\bot)^\bot$

类似的由内积的连续性(线性有界泛函), 我们知道进一步有 $\textrm{cl span} M \subset (M^\bot)^\bot$

考虑 $x \notin \textrm{cl span} M$, 则 $\inf\{\|x-y\|: y\in \textrm{cl span} M\} = c \gt 0$. 可做正交分解: $x = x_0+x'$ 其中 $x_0\in \textrm{cl span} M$ 而 $0\neq x' \in (\textrm{cl span} M)^\bot = M^\bot$. 假设 $x\in (M^\bot)^\bot$, 则 $\forall y \in M^\bot: (x,y) = 0$. 从而可取 $y = x'$, 这使得:

$$
(x, y) = (x_0 + x', x') = (x',x') \gt 0
$$

矛盾. 这意味着: $x\notin \textrm{cl span} M \Rightarrow x\notin (M^\bot)^\bot$. 等价于 $(M^\bot)^\bot \subset \textrm{cl span} M$

从而得证:

$$
(M^\bot)^\bot = \textrm{cl span} M
$$

## 7

### Problem

在 $L^2[a,b]$ 中 $S=\{e^{2\pi \ti n x}\}_{n=-\infty}^{\infty}$. 

1.  若 $|b-a|\leq 1$, 求证 $S^\bot = \{0\}$
2.  若 $|b-a|\gt 1$, 求证 $S^\bot \neq \{0\}$

其中 $L^2[a,b]$ 上的内积定义为:

$$
(f,g) = \int_a^b f(x)g^*(x) \td x
$$

### Proof

首先自然不难证明 $\{0\}\subset S^\bot$, 这是平凡的.

1.  考虑这样定义的 $S^\bot(a,b)$, 我们不难证明:

    $$
    b_1 \geq b_2 \Rightarrow S^\bot(a, b_2) \subset S^\bot(a,b_1)
    $$

    因为对短区间上的函数, 总能在更长区间通过补充定义其值为 $0$ 来进行扩充. 从而, 如果在 $S^\bot(a,b_2)$ 里找到了非零函数 $f$, 那么函数:

    $$
    f_{\textrm{new}}(x) = \begin{cases}
    f(x) & x \in [a,b_2] \\
    0 & x\in (b_2, b_1]
    \end{cases}
    $$

    总属于 $S^\bot(a,b_1)$. 为此, 我们只需要证明在 $|b-a| =1$ 时 $S^\bot =\{0\}$ . 此时, 对于周期函数类, 同 $S$ 正交的函数正意味着其 Fourier 系数均为 $0$, 故只能是常函数. 而对于非周期函数的情况, 总能通过调整端点取值而不影响积分值. 在这种情况下仍然可以证明 $S^\bot = \{0\}$

2.  对于这种情况, 考虑 $0\lt \epsilon \lt \min\{b-a-1, 1\}$. 则可以定义:

    $$
    f(x) = \begin{cases}
    g(x)    & x \in [a, a+\epsilon) \\
    0 & x \in [a+\epsilon, a+1] \\
    -g(x) & x \in [a+1, a+1+\epsilon) \\
    0 & x \in [a+1+\epsilon, b]
    \end{cases}
    $$

    从 $S$ 的周期性不难得证 $f \in L^2[a,b]$ 且 $f \in S^\bot$


## 8

## Problem

$\{e_n\}, \{f_n\}$ 是 Hilbert 空间 $H$ 中两个标准正交集, 满足条件:

$$
\sum_{n=1}^\infty \|e_n-f_n\|^2 \lt \infty
$$

求证两者中一个完备蕴含另一个完备

## Solution

我们证明 e => f

根据假设

$$
\sum_n \|e_n - f_n\| \lt \infty
$$

我们有:

$$
\begin{aligned}
\sum_n \|e_n-f_n\| &= \sum_n 2 - 2\textrm{Re}(e_n,f_n) \\
&\geq \sum_n 2 - 2 |(e_n,f_n)|^2 \lt \infty
\end{aligned}
\Rightarrow |(e_n,f_n)|\rightarrow 1
$$

从而, 考虑 $n\gt N$, 我们有 $1+\epsilon \gt|(e_n,f_n)|^2\gt 1-\epsilon$, 且 $\sum_{n\gt N} 1 -|(e_n,f_n)|^2 \lt \epsilon \Rightarrow \sum_{n\gt N} \sum_{m\neq n} |(e_m,f_n)|^2 \lt \epsilon $

考虑 $x\in\textrm{span} \{e_n\}_{n\gt N}$ 且 $\|x\|^2 =1$ 我们有:

$$
\begin{aligned}
\sum_{n\gt N} |(x, f_n)|^2 &= \sum_{n\gt N} \Big|(x, (f_n,e_n)e_n + \sum_{m\neq n} (f_n,e_m)e_m)\Big|^2 \\
&=\sum_{n\gt N}\Big|(x,e_n)(f_n,e_n)^* + \sum_{m\neq n} (x,e_m)(f_n,e_m)^*\Big|^2 \\
&\leq \sum_{n\gt N}|(x,e_n)(f_n,e_n)^*|^2 + \sum_{n\gt N} \sum_{m\neq n} |(x,e_m)|^2 |(f_n,e_m)|^2 \\
&\lt 1+2\epsilon
\end{aligned}
$$

与此同时, 我们有:

$$
\begin{aligned}
\sum_{n\gt N}|(x,f_n)|^2 &= \sum_{n\gt N}\Big|(x,e_n)(f_n,e_n)^* + \sum_{m\neq n} (x,e_m)(f_n,e_m)^*\Big|^2 \\ 
&\geq \sum_{n\gt N }\Big||(x,e_n)|^2 |(f_n,e_n)|^2 - |\sum_{m\neq n} (x,e_m)(f_n,e_m)^* |^2\Big|\\
&\geq \sum_{n\gt N }\Big||(x,e_n)|^2 |(f_n,e_n)|^2 - \sum_{m\neq n} |(x,e_m)|^2|(f_n,e_m) |^2\Big|\\
&\geq \sum_{n\gt N }\Big||(x,e_n)|^2 |(f_n,e_n)|^2 - \sum_{m\neq n} |(f_n,e_m) |^2\Big|\\ 
&=\sum_{n\gt N }\Big||(x,e_n)|^2 |(f_n,e_n)|^2 - (1-|(e_n,f_n)|^2)\Big|\\
&\gt 1 -2\epsilon
\end{aligned}
$$

从而, 我们证明了在 $N$ 足够大时 $\{f_n\}_{n\gt N}$ 同样是 $\textrm{span}\{e_n\}_{n\gt N}$ 的一组基. 而在 $n\leq N$ 对应的有限维空间中的 $N$ 个标准正交矢量天然成为一组基. 从而我们得证 $\{f_n\}$ 也是一组基, 换言之它是完备的.

## 9

### Problem

对 $\forall x , y \in H$, 求证如下平行四边形法则:

$$
\|x+y\|^2 +\|x-y\|^2 = 2\|x\|^2 + 2 \|y\|^2
$$

### Proof

$$
\begin{aligned}
\|x+y\|^2 + \|x-y\|^2 &= (x+y,x+y) + (x-y, x-y) \\
&= (x,x) + (x,y)+ (y,x)+(y,y) + (x,x) -(y,x)-(x,y) + (y,y) \\
&= 2 (x,x) + 2 (y,y)
\end{aligned}
$$

得证.

## 14

### Problem

设 $M$ 为 Hilbert 空间 $H$ 的线性子空间, 求证 $M$ 在 $H$ 中稠密当且仅当 $M^\bot = \{0\}$

### Proof

充分性证明是显然的, 因为此时 $M$ 事实上就是 $H$. 我们证明必要性. 不妨假设此时 $M^\bot = \{0, a\}$. 从而我们可以考虑集合

$$
B = \{x: \|x - a\| \lt \delta\} \subset H
$$

若 $B \cap M \neq \empty$, 不妨设 $y \in M \wedge y \in B$

