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