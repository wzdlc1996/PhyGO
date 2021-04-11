# Note for Chap. 5.3

## Hilbert 空间上的算子.

_[Definition]_: 数域 $\mathbb{K}$ 上的两个线性空间 $X,Y$, 映射 $A: X \rightarrow Y$ 被称为 ($X$ 到 $Y$) 的 **线性算子**, 如果

$$
\forall x,y\in X, \alpha,\beta\in \mathbb{K}\rightarrow A(\alpha x+\beta y) = \alpha A x + \beta Ay
$$

如果 $Y$ 是数域 $\mathbb{K}$ , 那么 $A$ 进一步被称为 $\mathbb{K}$ 域上的 **线性泛函**, 当 $Y= X$ 则称其为 **线性变换**

_[Definition]_: 设 $H$ 和 $K$ 是 Hilbert 空间, 称线性算子 $A:H\rightarrow K$ 是有界的, 如果

$$
\exists c \geq 0, \forall x \in H \rightarrow  \|Ax\|_K \leq c\|x\|_H
$$

所有 $H$ 到 $K$ 的有界线性算子记作 $\mathcal{B}(H,K)$, 而且不难证明它与通常的映射加法数乘构成了线性空间. 由之前的讨论还能够得到定理:

_[Theorem]_: $A$ 是 $H$ 到 $K$ 的线性算子, 则 "$A$ 是连续算子" 等价于 "$A$ 是有界算子"


