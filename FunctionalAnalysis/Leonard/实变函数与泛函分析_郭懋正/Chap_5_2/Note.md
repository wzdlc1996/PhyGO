# Note for Chap. 5.2

Hilbert 空间被定义为:

考虑$\mathbb{K}\in \{\mathbb{R},\mathbb{C}\}$ 上的线性空间 $X$, 且装备有内积 $(\cdot,\cdot): X\times X\rightarrow \mathbb{K}$, 使得
1.  $(ax+by,z) = a(x,z) + b(y,z)$
2.  $(z, ax+by) = a^*(z,x) + b^ *(z,y)$
3.  $(x,x)\geq 0, (x,x)=0\Leftrightarrow x=0$
4.  $(x,y) = (y,x)^*$

如果通过内积定义的距离 $\rho(x, y) = \|x-y\|\equiv (x-y,x-y)$ 使得 $(X,\rho)$ 是一个 **完备度量空间**, 那么就称此空间为一个 **Hilbert 空间**

## 正交完备

首先引入完备正交集合的概念:

_[Definition]_ : $\mathcal{E}$ 是 Hilbert 空间中的一个子集合, 若 $\forall e, f\in \mathcal{E}, e\neq f\Rightarrow (e,f)=0$, 则称 $\mathcal{E}$ 是 **正交集**, 如果 $\forall e \in \mathcal{E}:\|e\|=1$ , 则称其为 **标准正交集**, 如果其正交补集合只含零元素 $\mathcal{E}^\bot=\{0\}$, 那么称其为完备的.

_[Theorem]_ : 非零 Hilbert 空间中必存在完备正交集.

该命题的证明需要使用 Zorn 引理, 它是无穷归纳法的一个等价命题. 做粗糙说明的话, 可以想象为我们可以重复操作: 将一个正交集的正交补空间的一个元素放入这个正交集. 这个过程是有上界的, 在集合的包含关系意义下, 这个操作最多只会放入整个 Hilbert 空间. 重复这个过程直到正交集被完备化.


_[Theorem]_ : 若 $\mathcal{E}=\{e_\alpha:\alpha\in \Lambda\}$ 是Hilbert 空间 $H$ 的一个标准正交集, 则以下命题等价:
1.  $\forall x \in H: x = \sum_{\alpha\in\Lambda} (x,e_\alpha) e_\alpha$. 满足这个性质时称 $\mathcal{E}$ 是 $H$ 的一个基
2.  $\mathcal{E}$ 是完备的
3.  Parseval 等式成立, 即:
    $$\forall x\in H:\|x\|^2 = \sum_{\alpha\in\Lambda} |(x,e_\alpha)|^2$$

证明如下:

-  1 => 2: 
   $$
   \forall y \in \mathcal{E}^\bot: y = \sum_{\alpha\in\Lambda} (y,e_\alpha) e_\alpha = \sum 0e_\alpha = 0\Rightarrow \mathcal{E}^\bot = \{0\}
   $$
   即 $\mathcal{E}^\bot$ 完备
-  2 => 3:
   $$
   \begin{aligned}
   \forall x \in H:& y = x-\sum_{\alpha\in\Lambda} (x,e_\alpha) e_\alpha \in H. \\
   &\Rightarrow \forall \alpha\in\Lambda: (y,e_\alpha) = 0 \\
   &\Rightarrow y = 0 \ ; \ \textrm{since } \mathcal{E} \textrm{ is complete}\\
   &\Rightarrow 0=\|y\|^2 =\|x\|^2 - \sum_{\alpha\in\Lambda}|(x,e_\alpha)|^2
   \end{aligned}
   $$
   得证
-  3 => 1
   $$
   \begin{aligned}
   \forall x \in H:& y=x-\sum_{\alpha \in \Lambda} (x,e_\alpha)e_\alpha \in H \\
   &\Rightarrow 0=\|x\|^2-\sum_{\alpha\in\Lambda} |(x,e_\alpha)|^2 = \|y\|^2 \\
   &\Rightarrow (y,y) = 0\\
   &\Rightarrow y = 0 \\
   &\Rightarrow \forall x \in H: x = \sum_{\alpha\in\Lambda} (x,e_\alpha) e_\alpha
   \end{aligned}
   $$
   得证.