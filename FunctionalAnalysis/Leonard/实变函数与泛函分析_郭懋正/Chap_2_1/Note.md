# Note for Chap. 2.1

## Lebesgue 测度

_[Definition]_: 简单来讲, $\mathbb{R}^n$ 中点集 $E$ 的 **Lebesgue 外测度** 或简称 **外测度**, 是所有它可能的开矩体覆盖的体积的下确界:

$$
I = \{x \in \mathbb{R}^n: a_i\lt x_i\lt b_i , i=1,2,\cdots n\}\Rightarrow |I| = \prod_{i=1}^n (b_i - a_i)
$$

Then $\forall E\subset \mathbb{R}^n$:

$$\lambda^*(E) = \inf\{\sum_k |I_k|: E \subset \bigcup_k I_k, \textrm{for all possible covers}\}$$