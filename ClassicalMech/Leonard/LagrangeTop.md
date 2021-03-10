# Lagrange 陀螺读书报告

## 问题的提出

Lagrange 陀螺是一类特殊的定点刚体运动问题, 刚体本身在对于定点 \(O\) 的惯量椭球是一个旋转椭球体, 即三个主轴 \(\bm{e}_i \ ; \ i=1,2,3\) 的前两个 \(\bm{e}_1,\bm{e}_2\) 上椭球的半长轴场是相同的, 在第三个轴上与之前相异. 而刚体的质心在 \(\bm{e}_3\) 轴上. 我们将讨论 Lagrange 陀螺在均匀重力场下的定点运动, 这种运动广泛出现在真实世界的陀螺运动的情形中.

我们以定点 \(O\) 为坐标原点建立起固定于地面的坐标系 \(S\sim \{\bm{e}_x, \bm{e}_y, \bm{e}_z\}\). 而以主轴 \(\bm{e}_i\) 建立起来同刚体相对静止的随动坐标系 \(S'\). 刚体的构型空间即能够唯一确定 \(S'\) 的参数集合. 考虑刚体的质心高度为 \(h\) , 那么这个系统拥有 Lagrange 量:

$$L = T - mg h = \frac 1 2 I_1 (\omega_1^2 + \omega_2^2) + \frac 1 2 I_3 \omega_3^2 -mgh$$

我们使用了 \(I_1=I_2\) 的条件, 同时 \(\omega_i\) 是角动量矢量在 \(S'\) 中的分量.

## 刚体运动的描述

为了描述刚体的运动, 我们需要一个能够唯一确定 \(S'\) 的参数集合. 事实上, 由于 \(S'\) 和 \(S\) 之间仅相差一个转动变换, 因此它一定能够同 \(O(3)\) 的一个子集之间建立起一一映射 (事实上, 在 \(S,S'\) 拥有相同定向的情形下, 这个子集正是 \(SO(3)\)). 因此我们需要找到 \(SO(3)\) 的一种参数化. 这里我们使用 Euler 角参数:

$$\bm{e}_{1,2,3} = \hat R(\phi,\psi,\theta) \bm{e}_{x,y,z}$$

\(\hat R\) 是沟通 \(S\) 和 \(S'\) 的参数化的转动算子, 它有着矩阵表示(同样也是 Euler 角参数的定义):

$$\begin{aligned}[]
[\bm{e}_1, \bm{e}_2, \bm{e}_3] &= [\bm{e}_x, \bm{e}_y, \bm{e}_z]\bm{R}(\phi,\psi,\theta)\\
&\equiv [\bm{e}_x, \bm{e}_y, \bm{e}_z]
\begin{bmatrix}
\cos\phi & -\sin\phi & 0 \\
\sin\phi & \cos\phi & 0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos\theta & -\sin\theta \\
0 & \sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix}
\cos\psi & -\sin\psi & 0 \\
\sin\psi & \cos\psi & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{aligned}$$

使用这个矩阵表示我们可以完成将 \(S\) 中的矢量和它在 \(S'\) 中的分量联系起来:

$$\bm{a} = [\bm{e}_1,\bm{e}_2,\bm{e}_3]\begin{bmatrix}a_1\\a_2\\a_3\end{bmatrix}=[\bm{e}_x,\bm{e}_y,\bm{e}_z]\begin{bmatrix}a_x\\a_y\\a_z\end{bmatrix}\Rightarrow \begin{bmatrix}a_1\\a_2\\a_3\end{bmatrix} = \bm{R}(\phi,\psi,\theta)^{-1}\begin{bmatrix}a_x\\a_y\\a_z\end{bmatrix}$$

事实上, Euler 角参数化的定义并非处处都是好的. 在 \(\theta=0\) 时, 转动被 \(\psi+\phi\) 的值唯一确定, 这意味着在 \(\theta=0,\pi\) 时的转动矩阵和参数并非一一对应. 但这里我们并不深入讨论这个问题, 而更多地来研究刚体运动的行为.

## 刚体运动的 Lagrangian

我们需要将系统的 Lagrangian (在第一小节中书写的形式) 使用 Euler 角参数和它们的时间导数(即切空间中的量)来表达. 对于重力的位能, 只需要给出质心和定点 \(O\) 的距离(注意这个距离受约束是固定的) \(l\), 即可写出 \(h=l\cos\theta\). 问题在于角速度矢量的分量. 对于刚体上一点 \(\bm{a}'\) (指矢量在 \(S'\) 中的分量, 它是 \(\mathbb{R}^3\) 的元素, 一个列矢量) , 由于 \(S'\) 同刚体相对静止, 它是不含时的. 而在 \(S\) 中它为 \(\bm{a}\), 其时间依赖完全在变换矩阵 \(\bm{R}\) 中, 因此我们可以立即写出:

$$\bm{v} = \frac {\td \bm{a}} {\td t} = \Big\{\Big(\flo{\phi}\frac {\partial} {\partial \phi}+\flo{\psi}\frac {\partial} {\partial \psi}+\flo{\theta}\frac {\partial} {\partial \theta}\Big)\bm{R}(\phi,\psi,\theta)\Big\}\bm{R}(\phi,\psi,\theta)^{-1}\bm{a}\equiv \bm{\omega}\times \bm{a}$$

其中我们使用了如下性质(注意到 \(\bm{R}\) 作为正交矩阵满足 \(\bm{R}^{-1} = \bm{R}^T\)):

$$\Big(\frac {\td \bm{R}} {\td t}\bm{R}^{-1}\Big)^T = (\bm{R}^{-1})^T\frac {\td \bm{R}^T} {\td t} = \frac {\td} {\td t} (\bm{R}^{-1}\bm{R})^T - \frac {\td (\bm{R}^{-1})^T} {\td t} \bm{R}^T = -\frac {\td \bm{R}} {\td t} \bm{R}^{-1}$$

作为 \(3\times 3\) 的反对称矩阵, 我们总能够将之写为

$$\frac {\td \bm{R}} {\td t} \bm{R}^{-1} = \begin{bmatrix}0 & -\omega_z & \omega_y \\ \omega_z & 0 & -\omega_x \\ -\omega_y & \omega_x & 0\end{bmatrix}$$

从而其作用效果同 \(\bm{\omega} = (\omega_x,\omega_y,\omega_z)^T\) 与矢量的矢量积结果相同. 我们来看这角动量矢量在 \(S'\) 中的分量, 自然它是 \(\bm{\omega'}=\bm{R}^{-1}\bm{\omega}\), 我们来看它对应的反对称矩阵的具体形式. 注意到:

$$\bm{\Omega}\equiv\begin{bmatrix}0 & -\omega_z & \omega_y \\ \omega_z & 0 & -\omega_x \\ -\omega_y & \omega_x & 0\end{bmatrix} = - [\bm{J}_1, \bm{J}_2,\bm{J}_3]\begin{bmatrix} \omega_x\\ \omega_y \\ \omega_z\end{bmatrix}$$

其中矩阵 \((\bm{J}_i)_{jk} =\epsilon_{ijk}\) , 则:

$$\bm{\Omega}' \equiv -[\bm{J}_1,\bm{J}_2,\bm{J}_3] \bm{\omega'} = - \sum_{k,l} \bm{J}_k(\bm{R}^{-1})_{kl}\omega_l$$

注意到保定向的正交矩阵同时能够保持矢量积不变, 成立: \(\bm{A}\bm{x}\times \bm{A}\bm{y} = \bm{A}(\bm{x}\times \bm{y})\) (其证明可以通过考虑它和任意矢量的三重积, 并注意到 \([\bm{A}\bm{x},\bm{A}\bm{y},\bm{A}\bm{z}] =\text{det}\bm{A} \ [\bm{x},\bm{y},\bm{z}]\)), 这个性质写为分量形式为(对重复指标求和):

$$\epsilon_{ipq}A_{pj}A_{qk} = A_{il}\epsilon_{ljk}$$

因而我们有:

$$\sum_k\bm{J}_k (\bm{R}^{-1})_{kl} = \bm{R}^T \bm{J}_l \bm{R}$$

从而:

$$\bm{\Omega}' = \bm{R}^T \bm{\Omega} \bm{R} = \bm{R}^{-1} \frac {\td \bm{R}} {\td t}$$

由于在 Euler 角参数下, 矩阵 \(\bm{R}\) 的形式十分简单:

$$\bm{R}(\phi,\psi,\theta) = \bm{R}_3(\phi)\bm{R}_1(\theta)\bm{R}_3(\psi)$$

我们立即写出:

$$\begin{aligned}
\bm{\Omega'} &= \bm{R}_3(\psi)^T \bm{R}_1(\theta)^T \bm{R}_3(\phi)^T \frac {\td \bm{R}_3} {\td \phi}(\phi)\bm{R}_1(\theta)\bm{R}_3(\psi)\flo{\phi}+\bm{R}_3(\psi)^T \bm{R}_1(\theta)^T \frac {\td \bm{R}_1} {\td \theta}(\theta)\bm{R}_3(\psi)\flo{\theta}\\
&\indent +\bm{R}_3(\psi)^T\frac {\td \bm{R}_3} {\td \psi}(\psi)\flo{\psi} \\
&=
\begin{bmatrix}
0 & -\cos\theta & \cos\psi \sin\theta \\
\cos\theta & 0 & -\sin\psi \sin\theta \\
-\cos\psi \sin\theta & \sin\psi\sin\theta & 0
\end{bmatrix}\flo{\phi} +
\begin{bmatrix}
0 & 0 & -\sin\psi  \\
0 & 0 & -\cos\psi \\
\sin\psi & \cos\psi & 0
\end{bmatrix}\flo{\theta} \\
&\indent +
\begin{bmatrix}
0 & -1 & 0  \\
1 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}\flo{\psi}
\end{aligned}$$

从而我们有:

$$(\omega_1,\omega_2,\omega_3)^T =
\begin{bmatrix}
\sin\psi \sin\theta \flo{\phi} +\cos\psi \flo{\theta} \\
\cos\psi \sin\theta \flo{\phi} - \sin\psi \flo{\theta} \\
\cos\theta \flo{\phi} + \flo{\psi}
\end{bmatrix}$$

最终, 我们写出了系统的 Lagrangian:

$$L = \frac 1 2 I_1\big(\flo{\theta}^2+\sin^2\theta \flo{\phi}^2\big) + \frac 1 2 I_3 (\flo{\psi}+\cos\theta \flo{\phi})^2 - mgl \cos\theta$$

## 刚体运动的讨论

### 守恒律分析

同一般陀螺不同, Lagrange 陀螺由于旋转对称性, 角度 \(\psi\) 成为了循环坐标. 因此它比起一般陀螺将多出一个守恒量. 它连带 \(\phi\) 作为循环坐标对应的守恒量和 \(L\) 不含时对应的能量守恒一起构成了 \(3\) 个独立(事实上并不总是独立的)守恒量.

对于两个循环坐标我们有同其共轭的广义动量守恒:

$$\begin{aligned}
P_\psi &= \frac {\partial L} {\partial \flo{\psi}} = I_3(\flo{\psi}+\cos\theta\flo{\phi}) \\
P_{\phi} &= \frac {\partial L} {\partial \flo{\phi}} = I_1 \sin^2\theta \flo{\phi} + I_3(\flo{\psi}+\cos\theta \flo{\phi})\cos\theta
\end{aligned}$$

稍微整理我们有:

$$\begin{bmatrix}
P_\psi \\ P_\phi\end{bmatrix} =
\begin{bmatrix}
I_3  & I_3 \cos\theta \\
I_3 \cos\theta & I_1\sin^2\theta + I_3 \cos^2\theta
\end{bmatrix}
\begin{bmatrix} \flo{\psi} \\ \flo{\phi} \end{bmatrix}$$

其中系数矩阵的行列式值为 \(I_1I_3\sin^2\theta\) . 在 \(\theta\neq 0,\pi\) 时我们能够用 \(P_\psi, P_\phi\) 表示出 \(\flo{\psi},\flo{\phi}\). 换言之, 当 \(\theta\neq 0,\pi\) 时我们拥有三个独立的守恒量.

### 定轴旋转

当 \(\theta\equiv 0,\pi\) 时, 刚体做定轴转动. 这时 \(P_\psi, P_\phi\) 并不是独立的. 但这事实上是由于 Euler 角的定义. 在这个情况下同构型空间一一对应的参数化事实上是 \(\psi\pm\phi\), 对应着刚体绕 \(\theta=0,\pi\) 的轴转动的角位移. 根据守恒律我们有:

$$I_3\frac {\td } {\td t} (\psi\pm \phi) = P_\psi \pm P_\phi = \text{Const}$$

换言之, 这个时候刚体做匀速的定轴转动

### 一般情况 Lagrange 陀螺的运动

考虑 \(\theta\) 并不恒为 \(0,\pi\) 的情形. 这时我们可以写出使用 \(P_\phi, P_\psi\) 表示的 \(\flo{\phi}, \flo{\psi}\), 系统等价于一个一维系统, 其对应的能量函数为:

$$E = \frac {I_1} 2 \flo{\theta}^2 + \frac {(P_\phi - P_\psi\cos\theta)^2} {2I_1 \sin^2 \theta} + \frac {P_\psi^2} {2I_3} + mgl \cos\theta$$

略去常数将不影响系统的运动, 我们有这个力学系统的由三个守恒量(初次积分)导出的动力学方程:

$$\begin{aligned}
\flo{u}^2 &=(\alpha-\beta u)(1-u^2)-(a-b u)^2 \equiv f(u) \\
\flo{\phi} &= \frac {a-b u} {1-u^2} \\
\flo{\psi} &= \frac {P_\psi} {I_3} - u \frac {a-b u} {1-u^2}
\end{aligned}$$

其中 \(u=\cos\theta , a=P_\phi/I_1, b=P_\psi/I_1 , \alpha= 2(E-P_\psi^2/2I_3)/I_1, \beta = 2mgl/I_1\). 可以看到, \(\theta\) 的运动同其他两个角度独立, 只要能够积出 \(u\) 的一阶微分方程, 其他两个角度自然得到确定, 进而确定整个运动.

对 \(\theta\) 的讨论事实上正是函数 \(f(u)\) 的行为的讨论. \(u\) 的运动等同于一个在势场 \(V(u)=-f(u)\) 中的能量为0的一维粒子. 它只能在 \(V(u)\leq 0\) 确定的范围内做周期运动(注意 \(u\in[-1,1]\)). 由于 \(V(\pm 1)\gt 0\) , 因此上面的参数需要在区间 \([-1,1]\) 上令 \(V(u)\) 有两个零点(由于 \(V(u\rightarrow +\infty)\lt 0\), 因此它在 \((1,+\infty)\) 上还有一个零点.). 从而, \(\theta\) 的这种在有限区间内的周期运动被称为 **章动**.

对 \(\phi\) 的讨论事实上由函数 \(\frac {a-bu} {1-u^2}\) 确定, 这个函数是陀螺瞬时的在 \(\phi\) 上的角速度. 它事实上是陀螺绕着过 \(O\) 点平行于 \(\bm{e}_z\) 的轴的转动. 这种转动被称为 **进动**

对 \(\psi\) 的讨论类似于 \(\phi\) , 但它对应于陀螺绕着过 \(O\) 点平行于 \(\bm{e}_3\) 的随刚体运动的轴的转动, 这种转动事实上正是刚体绕自身对称轴的转动, 可以称为 **旋转**
