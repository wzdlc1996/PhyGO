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