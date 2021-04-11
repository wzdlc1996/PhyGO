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

对于特别的一类 **可分** Hilbert空间, 即其拥有 **可数的稠密子集**, 则成立如下的关于其上正交集的定理

_[Theorem]_: Hilbert 空间 $H$ 是可分的, 等价于, 它有至多可数的标准正交基 $\mathcal{E}$. 若 $|\mathcal{E}|= N \lt \infty$, 则它于 $\mathbb{K}^N$ 同构, 若 $N=\infty$, 则与 $l^2$ (平方可和序列空间) 同构.

_[Proof]_: 
1.  必要性
    
    设 $\{x_n\}_{n=1}^{\infty}$ 是 $H$ 的可数稠密子集, 那么其中必存在一个极大线性无关子集 $\{y_n\}_{n=1}^N$, 其中 $N\lt \infty$ 或者 $N=\infty$, 使得

    $$
    \textrm{span} \{y_n\} = \textrm{span} \{x_n\}
    $$

    等号右边基于稠密性应当正为 $H$, 否则我们将能够找到另一个线性无关方向, 利用这个方向我们总能够找到同 $\{x_n\}$ 存在有限距离的点, 使得与稠密性矛盾. 

    对这样找到的集合使用 Gram-Schmidt 正交化过程便得到了一组标准正交基的构造. 

2.  充分性
    考虑标准正交基 $\mathcal{E}=\{e_n\}_{n=1}^N$, 其中 $N$ 可以是有限也可以是无穷. 则集合

    $$
    \{x=\sum_{i=1}^N a_n e_n \in H: \textrm{Re} a_n, \textrm{Im}a_n \in \mathbb{Q}\}
    $$

    正是 $H$ 中的稠密可数子集, 从而 $H$ 是可分的.

同构性的证明, 有限维情形是平凡的, 而无限维情形只需要注意到 Parseval 等式 $\|x\|^2 = \sum_{n} |(x,e_n)|^2$, 即可看到. 

## Riesz 表示定理

Hilbert 空间 $H$ 上的线性泛函被定义一类函数: $f:H\rightarrow \mathbb{K}$, 且满足:

$$
\forall \alpha,\beta \in \mathbb{K}: f(\alpha x+\beta y) = \alpha f(x)+\beta f(y)
$$

如果当 $x_n\rightarrow x$ 时有 $f(x_n)\rightarrow f(x)$, 则称其在点 $x$ 处连续. 

对 $H$ 上的一个线性泛函 $f$, 下列命题等价:
1.  $f$ 是连续的
2.  $f$ 在任意点连续
3.  $f$ 在 $x=0$ 处连续
4.  $\exists c\gt 0: \forall x\in H: |f(x)| \leq c \|x\|$

证明 1 => 2 => 3 是显然的, 我们来证明 3 => 1: 设序列 $x_n\rightarrow x$, 则 $x_n-x \rightarrow 0$. 因而根据 3, 我们立即有 $0 = f(0) =\lim_{n\rightarrow \infty} f(x_n-x) = \lim f(x_n)-f(x)$. 即证

证明 4 => 3 是容易的, 因为 $f(0) = 0\times f(0) = 0$, 而在 $0$ 附近总有 $f(x_n) = \leq c\|x_n\|\rightarrow 0$, 从而得证连续性. 我们证明 3 => 4: 从连续性给出: 

$$
\forall \epsilon \gt 0: \exists \delta \gt 0 \text{ s.t. } \|x\|\lt \delta \Rightarrow |f(x)| \lt \epsilon
$$

从而我们有:

$$
\forall x \in H: |f((\delta - s)x / \|x\|)| =\frac {\delta - s} {\|x\|} |f(x)| \lt \epsilon \Rightarrow |f(x)|\lt \frac {\epsilon} {\delta(\epsilon) - s} \|x\|
$$

其中 $\delta \gt s\gt 0$, 而 $\epsilon,\delta$ 对为是的连续性满足的正实数对. 因而总能找到正实数 $c$ 使得 $|f(x)|\leq c\|x\|$ 成立.

_[Definition]_ : 设 $f$ 是 Hilbert 空间上的线性泛函, 若存在常数 $c\gt 0$ 使的:

$$
\forall x\in H: |f(x)|\leq c\|x\|
$$

则称 $f$ 是 $H$ 上的有界线性泛函, 并将 $\|f\|:=\sup\{|f(x)| : \|x\|\leq 1\|$ 称为 $f$ 的模.

_[Theorem] (Riesz表示定理)_ : 设 $f$ 是 Hilbert 空间 $H$ 上的有界线性泛函, 则存在唯一的 $x_f \in H$ 使得:

$$
\forall x \in H: f(x) = (x,x_f)
$$

且 $\|f\|=\|x_f\|$. 于是由 $f$ 到 $x_f$ 给出了 $H^*$ ($H$上所有连续泛函的集合) 到 $H$ 的一个等距同构.

证明如下

令 $M=\ker f = \{x: f(x) = 0\}$. 由于 $f$ 的连续性, 任何 $M$ 中的收敛序列 $\{x_n\}$ 都有: $x_n\rightarrow x\Rightarrow f(x_n) \rightarrow f(x) =0 \Rightarrow x\in M$. 因而 $M$ 是一个闭集, 更进一步的, 可以证明它还是一个子空间. 当 $f$ 非零时, $M\neq H$, 从而我们有 $M^\bot \neq \{0\}$. 因此我们可以找到 $x_0\in M^\bot$ 使得 $f(x_0) = 1$. 则:

$$
\forall x \in H: f(x) = \alpha \Rightarrow f(x-\alpha x_0) = 0\Rightarrow x-\alpha x_0 \in M
$$

从而我们有

$$
0 = (x-f(x)x_0, x_0) = (x,x_0) - f(x) \|x_0\|^2
$$

故可取 $x_f = x_0/\|x_0\|^2$, 从而存在性得证. 我们还可以证明唯一性, 如果有另一 $x_f'$ 满足条件, 那么 $\forall x\in H: (x,x_f) = (x,x_f') \Rightarrow (x,x_f-x_f')=0$. 则可以取 $x=x_f-x_f'\in H$ 立即得到 $\|x_f-x_f'\|=0\Rightarrow x_f=x_f'$. 故唯一性得证.

而 $\|f\|=\|x_f\|$ 是 Cauchy-Schwartz 不等式的直接结果, 不再赘述.