# Note 

## Introduction

_[Definition]_: Essential concepts

1.  $X$: 输入元素所在的空间
2.  $Y$: 输出元素所在的空间
3.  $K(\cdot, p)$: 含参数 $p$ 的算子(系统)
4.  $P$: 参数空间

问题的分类如下:

1.  **正问题(forward problem)**: 已知 $p\in P$, 对 $x\in X$ 计算输出 $y=K(x, p) \in Y$
2.  **反问题(inverse problem)**: 已知 $p\in P, y\in Y$, 找到 $x\in X$ 使得 $y= K(x,p)$ 成立
3.  **系统辨识(system identification)**: 已知 $x\in X, y\in Y$, 找到 $p\in P$ 使得 $y=K(x,p)$ 成立.

_[Note]_: 反问题的一个主要特点: 测量数据中的少量噪声会导致求解得到的物理量产生很大误差, 即<mark>求解过程是不稳定的</mark>. 这也是它的一个主要困难. 目前数学中已经拥有处理这样问题的理论和方法: 正则化理论.

## Examples of Inverse Problem

### 地质勘探问题

简化的一维模型: 地表下深度为 $h$ 的平行直线上异常质量分布为 $\rho(x)$, 且 $\textrm{supp} \rho(x) = \{x:\rho(x)\neq 0\} = \Omega \subset \mathbb{R}$. 问题描述为: 根据地表测量的重力 $f_v(x)$ 确定密度 $\rho$ 及 $\Omega$:

$$f_v(x) = G h \int_\Omega \frac {\rho(x')} {[(x-x')^2 + h^2]^{3/2}} \td x'$$

正问题即从右到左, 反问题(重构问题)即从左到右. 多数反问题有着这样的共同特性, 要求我们求解如下形式的 **Fredholm** 积分方程:

$$f(x) = \int k(x,x') g(x')\td x'$$

### 地形航测问题

飞机飞行中通过测量感受到均质山丘的引力 $f(s)$ 来确定山丘形状. 一维问题中的山丘形状如果为 $y = \phi(x)$, 那么有:

$$f(s) = \int_0^1 \td x \int_0^{\phi(x)}\td y \ G \rho / r^2 $$

这事实上要求求解一个 非线性的 Fredholm 方程:

$$f(x) = \int k(x, x', \phi(x')) \td x'$$

### X-ray 层析(Tomography)

设 $x-y$ 平面上有一个物体对 X-ray 的吸收系数为 $f(x,y)$. **CT(computed tomography)** 要研究如何通过入射方向自由的光吸收信息恢复出来物体的形状. 直线的参数化为:

$$
\begin{cases}
& x(u) = s \cos \delta - u \sin \delta \\
& y(u) = s \sin \delta + u \cos \delta
\end{cases}
$$

其中 $s$ 为原点到直线的距离, $\delta$ 为直线法线的方向角度(法向同 $Ox$ 轴的夹角).

对沿着直线的光吸收可以写为:

$$
\td I(u) = -\gamma f(x(u), y(u))\td u \Rightarrow \log I(u) = -\gamma \int_{u_0}^u f(x(u), y(u))\td u
$$

如果 $f$ 拥有紧支集, 那么我们有带参数的直线下的吸收由如下变换确定:

$$(Rf)(s, \delta) = \int_{\mathbb{R}} f(s \cos \delta - u \sin \delta, s\sin \delta + u \cos \delta)\td u$$

该变换也被称为 **Radon transformation**

根据一个函数的 Radon transformation 确定其原函数就是 X-ray CT 的核心问题. 