# Note for Chap. 5.1

## 度量空间(Metric Space)

度量空间是对过去我们所研究的欧氏空间的高度抽象. 我们过去对拓扑和极限的理解都基于距离, 度量空间就是从这一点出发抽象得到的概念.

度量空间被表示为一个二元tuple $(X, \rho)$. 其中 $X$ 为一个非空集合, 而 $\rho : X\times X\rightarrow \mathbb{R}$ 满足如下三个条件:
1.  $\forall x, y \in X: \rho(x,y) \geq 0.$ 且 $\rho(x,y)=0 \Leftrightarrow x= y$
2.  $\forall x,y\in X: \rho(x,y) = \rho(y,x)$
3.  $\forall x,y,z\in X: \rho(x,y) +\rho(y,z) \geq \rho(x,z)$

函数 $\rho$ 被称为度量空间上的度量. 类似的立即可以定义度量空间上的开球, 开集, 聚点, 闭集以及稠密性等概念. 

## 度量空间的完备

完备性被这样定义:

如果度量空间 $(X,\rho)$ 中的每个 **基本列**, 即 $\forall x_i\in\{x_n\}, l \in \mathbb{N} : \lim_{i\rightarrow \infty} \rho(x_i, x_{i+l}) = 0 $, 都收敛到 $X$ 中的一个点, 即 $\exists x\in X: \lim_{n\rightarrow\infty} \rho(x,x_n) = 0$. 

而可以证明, 任意一个度量空间 $(X,\rho)$, 都可以找到一个完备的度量空间使得 $(X,\rho)$ 是其中一个稠密子集的等距变换.
1.  稠密子集: $X'\subset X$ 称为度量空间 $(X,\rho)$ 的 **稠密子集**, 如果 $\forall x\in X, \epsilon\gt 0, \exists y \in X'\Rightarrow \rho(x,y)\lt \epsilon$ 
2.  等距变换: $(X,\rho), (X',\rho')$ 中存在一个从 $X$ 到 $X'$ 的等距变换是指存在映射 $T:X\rightarrow X'$ 使得 $\forall x, y \in X: \rho(x,y) = \rho'(Tx,Ty)$. 此时我们称 $X$ 同其像 $TX\subset X'$ 等距同构.

## 列紧性

过去我们在有限维欧氏空间中拥有性质: 有界无穷集必含一个收敛子列. 但在一般的度量空间这个性质可能不成立. 拥有这个性质的度量空间被我们称为 **列紧的**:

_[Definition]_: 给定度量空间 $(X,\rho)$ , 如果 $A\subset X$ 而且 $A$ 中任意点列在 $X$ 中都有一个收敛子列, 则称 $A$ 是 **列紧的**. 如果这个子列还收敛到 $A$ 中的点, 则称 $A$ 为 **自列紧的**. 

在一般的度量空间中, 有界性并不保证其列紧性. 为了刻画列紧性, Hausdorff 引入:

_[Definition]_ : 给定度量空间 $(X,\rho)$, $M\subset X$

1.  设 $N\subset M, \epsilon \gt 0$, 若 $\forall x \in M, \exists y \in N : x\in B(y,\epsilon) = \{x: \rho(x,y)\lt \epsilon\}$. 则称 $N$ 是 $M$ 的一个 **$\epsilon$-网**. 如果 $|N|\lt \infty$ 即 $N$ 为一有穷集, 则称其为 $M$ 的一个 **有穷$\epsilon$-网**
2.  若 $\forall \epsilon \gt 0$, 都存在 $M$ 的一个有穷 $\epsilon$-网, 则称集合 $M$ 是完全有界的.

_[Theorem] (Hausdorff)_ : 设 $(X,\rho)$ 为度量空间, $M\subset X$, 有:
1.  若 $M$ 在 $X$ 中列紧, 则 $M$ 完全有界
2.  若 $X$ 是完备空间, $M$ 完全有界, 则 $M$ 列紧.

除列紧性之外, 还有紧致性的概念:

_[Definition]_ : 设 $M$ 是度量空间 $(X,\rho)$ 的一个子集, $\Sigma = \{G_l\}_{l\in I}$ 是 $X$ 的开集族(即开球族), 若

$$
M\subset \bigcup_{l\in I} G_l
$$

则称 $\Sigma$ 是 $M$ 的一个 **开覆盖**. 如果 $M$ 的任意开覆盖中都有它的有限开覆盖, 即: $\exists S\in I: |S|\lt \infty$ 使得

$$
M \subset \bigcup_{l\in S} G_l
$$

则称 $M$ 是 **紧致的**, 或称为紧集.

_[Theorem]_ : 度量空间中子集的紧致等价于自列紧. 