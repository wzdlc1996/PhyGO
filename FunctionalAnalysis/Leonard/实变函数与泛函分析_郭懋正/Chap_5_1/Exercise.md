# Exercise in Chap. 5.1

## 1.1

### Problem

$S$ 为由一切复数列 $x = \{\xi_1,\xi_2,\cdots,\xi_n,\cdots\}$ 组成的集合, 在 $S$ 中定义距离为:

$$
\rho(x,y) = \sum_{k=1}^\infty \frac 1 {2^k} \frac {|\xi_k - \eta_k|} {1+|\xi_k-\eta_k|}
$$

证明它是一个完备的度量空间

### Proof

首先我们证明这个定义确为距离. 对称性和 $x=y \Rightarrow \rho(x,y) = 0$ 是显然的. 我们证明 $\rho(x,y) = 0 \Rightarrow x = y$, 这可以通过假设存在 $\eta_l \neq \xi_l$ 使得该正项级数非零得到. 从而我们只需证明三角不等式:

$$
\begin{aligned}
\rho(x,y)+ \rho(y,z) &= \sum_{k=1}^\infty \frac 1 {2^k} \frac {|x_k-y_k|} {1+|x_k-y_k|} + \sum_{k=1}^\infty \frac 1 {2^k} \frac {|z_k-y_k|} {1+|z_k-y_k|}\\
&=\sum_{k=1}^\infty \frac 1 {2^k} \Big(\frac {|x_k-y_k|+|y_k-z_k|+2|x_k-y_k||z_k-y_k|} {(1+|x_k-y_k|)(1+|y_k-z_k|)}\Big) \\
&\geq \sum_{k=1}^\infty \frac 1 {2^k} \Big(\frac {|x_k-z_k|} {1+|x_k-z_k|}\Big)
\end{aligned}
$$

其中我们使用了不等式, 对 $a,b,c \geq 0$

$$
\begin{aligned}
\frac {|a-b|+|b-c|+2 |a-b||b-c|} {(1+|a-b|)(1+|b-c|)} &=\frac {(|a-b|+|b-c|)^2} {1+|a-b| + |b-c| + |a-b||b-c|} \\
&\geq \frac {|a-b|+|b-c|+2 |a-b||b-c|} {1+|a-b| + |b-c| + 2|a-b||b-c|}\\
&= \frac {\eta} {1+\eta} \Big|_{\eta = |a-b| + |b-c|+2|a-b||b-c|} \\
& \geq  \frac {\eta} {1+\eta}\Big|_{\eta = |a-c|\leq |a-b|+|b-c|+2|a-b||b-c|} \\
&= \frac {|a-c|} {1+|a-c|}
\end{aligned}
$$

函数 $\eta / (1+\eta) = 1 - (1+\eta)^{-1}$ 在 $[0,\infty)$ 上单调增. 上面不等式取等号的条件为 $|a-b||b-c| = 0$

从而三角不等式得证. 

接下来证明度量空间的完备性, 为此我们需要证明任意基本列都收敛到度量空间内的一点. 而作为正项级数, 基本列具备性质: $\forall N:\lim_{n\rightarrow \infty}\rho(x^{(n)},x^{(n+N)}) =0 \Rightarrow \forall k: \lim_{n\rightarrow\infty}|x^{(n)}_k - x^{(n+N)}_k |=0$

从复数域的完备性不难得到极限的存在性, 进而有该度量空间的完备性.

## 1.2

### Problem

在一个度量空间 $(X,\rho)$ 中求证: 基本列是收敛列当切进党其中存在一个收敛子列

### Proof

其必要性不难证明, 因为收敛列自己就是其中的一个收敛子列. 

考虑充分性, 基本列中存在一个收敛子列, 即 $\exists n_k \in \mathbb{N}: \lim_{k\rightarrow \infty} n_k = \infty \Rightarrow \exists x \in X: \lim_{k\rightarrow \infty} \rho(x_{n_k}, x) = 0$

我们有, 对 $n\rightarrow \infty$, 我们总选择 $n_k = \inf \{n_k: n_k\gt n\}$

$$
\begin{aligned}
\lim_{n\rightarrow \infty} \rho(x_n, x) &\leq \lim_{n\rightarrow \infty} \rho(x_n, x_{n_k}) + \rho(x_{n_k}, x) \\
&= 0
\end{aligned}
$$

第一项收敛到零是基本列的性质. 

## 1.3

## Problem

求证 $[0,1]$ 上的多项式全体度量:

$$
\rho(p,q) = \int_0^1 |p(x) - q(x)| \td x \ ; \ (p,q \in \textrm{Poly}(x))
$$

是不完备的, 并指出它的完备化空间

## Solution

一个基本列非收敛的反例为:

$$
p_n(x) = \sum_{l=0}^{n} \frac 1 {l!} x^l
$$

显然:

$$
\rho(x_{n+N},x_n) = \sum_{l=n+1}^{n+N} \frac 1 {(l+1)!} \leq \frac {N} {n!} \rightarrow 0  
$$

而这个序列的极限点为 $e^x$ , 并非此空间中的元素.

从这个意义上, 这个空间的完备化空间为 $[0,1]$ 上的全体解析函数.

## 1.4

