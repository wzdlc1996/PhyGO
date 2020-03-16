# 运动方程

## 简介

本篇报告讨论欧氏空间中分析力学里的三个(类)方程, 即Newton方程, Lagrange方程和Hamilton方程之间的联系. 我们的根本目的是为了得到系统在构型空间中的状态(位置, 本次报告中讨论的构型空间依然是欧氏空间, 讨论的系统是质点系统, 同时质点之间的作用是保守的两体作用)对时间的微分方程, 即所谓的运动方程.

## 系统的描述

我们讨论3维欧氏空间中拥有 \(N\) 个质点的质点系统, 质点被编号为 \(i\in\{1,\cdots,N\} = S\). 对于第 \(i\) 个质点, 我们记它的质量为 \(m_i\), 位置为 \(\bm{r}_i\) . 因此整个系统任意时刻 \(t\) 在构型空间中的状态即为 \(\bm{r}(t) = (\bm{r}_1(t),\cdots,\bm{r}_N(t))\).

系统 \(S\) 中的任意两个质点我们假设他们相互的作用被保守力所描述, 换言之对于质点 \(i\) , 来自质点 \(j\) 的作用力 \(\bm{F}_{ji}\) 为:

$$\bm{F}_{ji} = -\frac {\partial U_{ji}(\bm{r}_j,\bm{r}_i)} {\partial \bm{r}_i}$$

势 \(U_{ji}\) 拥有如下性质:

1.  对称性: \(U_{ji}(\bm{r}_j, \bm{r}_i)\) = \(U_{ij}(\bm{r}_i,\bm{r}_j)\)
2.  Newton第三定律: \(\bm{F}_{ji} = -\bm{F}_{ij}\)

从这两个条件我们可以对 \(U\) 的形式进行简化:

$$\bm{F}_{ji}= -\bm{F}_{ij}\Rightarrow \partial_1U_{ji}(\bm{r}_j,\bm{r}_i) = -\partial_1U_{ij}(\bm{r}_i,\bm{r}_j)=-\partial_2 U_{ji}(\bm{r}_j,\bm{r}_i)$$

从而我们有: \(\partial_{\bm{r}_j}U_{ji}(\bm{r}_j,\bm{r}_i) + \partial_{\bm{r}_i}U_{ji}(\bm{r}_j,\bm{r}_i)=0\) , 考察变量替换: \(\bm{x}_\pm = \bm{r}_j\pm\bm{r}_i\), 我们很容易能够证明: \(\partial_{\bm{x}_+}U_{ji} = 0\). 换言之, \(U_{ji}\) 应当只是两个质点坐标之差的函数:

$$U_{ji}(\bm{r}_j,\bm{r}_i) = U_{ji}(\bm{r}_j-\bm{r}_i)$$

如上是我们将会讨论的系统的描述. 我们的目的是为了得到一组完备的微分方程, 使得我们能够从合适的初始条件积分得到之后每一时刻系统的位置状态. 亦即, 函数 \(\bm{r}(t)\) 所满足的微分方程.

## 用不同的方法得到运动方程

### Newton 方程

Newton方程是指对于任意一个质点, 它的运动的加速度乘它的质量总是等于作用在它上面的所有外力, 数学上来说即:

$$m \frac {\td^2} {\td t^2} \bm{r}(t) = \bm{F}$$

将Newton方程直接应用在我们的质点系统的每一个质点上, 这里当然使用到了作用力的叠加原理, 即一个质点上的合作用力等于各个作用力的矢量和. 我们得到共 \(N\) 个(矢量)二阶微分方程组:

$$m_i \frac {\td^2} {\td t^2} \bm{r}_i(t) = - \frac {\partial} {\partial \bm{r}_i}\sum_{j\in S\wedge j\neq i} U_{ji}(\bm{r}_j, \bm{r}_i)=- \frac {\partial} {\partial \bm{r}_i}\sum_{j\in S\wedge j\neq i}U_{ji}(\bm{r}_j-\bm{r}_i) \ ; \ i\in S$$

写为分量的话共有 \(3N\) 个独立方程, 未知函数为 \(\bm{r}(t)\) 的 \(3N\) 个, 因此我们写出了系统的运动方程

### Lagrange 方程

Lagrange方程通过使用Lagrangian:

$$L(\bm{r}, \flo{\bm{r}}, t) = \frac 1 2 \sum_{i\in S} m_i \flo{\bm{r}}_i^2 - \frac 1 2\sum_{i\neq j} U_{ji}(\bm{r}_j-\bm{r}_i)$$

连同Lagrange方程来得到运动方程:

$$\frac {\td } {\td t} \frac {\partial L} {\partial \flo{\bm{r}}_i} - \frac {\partial L} {\partial \bm{r}_i} = 0 \ ；\ i\in S$$

我们演算如下:

$$\begin{aligned}
\frac {\td} {\td t}\frac {\partial L} {\partial \flo{\bm{r}}_i} &= \frac {\td } {\td t} m_i \flo{\bm{r}}_i = m_i \frac {\td^2 \bm{r}_i} {\td t^2} \\
\frac {\partial L} {\partial \bm{r}_i} &= - \frac 1 2 \frac {\partial} {\partial \bm{r}_i}\sum_{j,k\in S \wedge j\neq k} U_{jk}(\bm{r}_j-\bm{r}_k) \\
&= -\frac 1 2 \sum_{j,k\in S \wedge j\neq k} \Big(\delta_{ji}\frac {\partial} {\partial \bm{r}_j} U_{jk}(\bm{r}_j-\bm{r}_k)+ \delta_{ki}\frac {\partial} {\partial \bm{r}_k}U_{jk}(\bm{r}_j-\bm{r}_k)\Big) \\
&= -\frac 1 2 \sum_{j,k\in S \wedge j\neq k} \Big(\delta_{ji}\frac {\partial} {\partial \bm{r}_j} U_{kj}(\bm{r}_k-\bm{r}_j)+ \delta_{ki}\frac {\partial} {\partial \bm{r}_k}U_{jk}(\bm{r}_j-\bm{r}_k)\Big) \\
&=-\frac 1 2 \sum_{k\in S\wedge k\neq i}\frac {\partial } {\partial \bm{r}_i} U_{ki}(\bm{r}_k-\bm{r}_i) - \frac 1 2 \sum_{j\in S \wedge j\neq i}\frac {\partial } {\partial \bm{r}_i} U_{ji}(\bm{r}_j-\bm{r}_i) \\
&= - \frac {\partial} {\partial \bm{r}_i}\sum_{j\in S \wedge j\neq i}U_{ji}(\bm{r}_j-\bm{r}_i)
\end{aligned}$$

因此 Lagrange 方程直接给出的微分方程是:

$$m_i \frac {\td^2} {\td t^2} \bm{r}_i (t) = -\frac {\partial} {\partial \bm{r}_i}\sum_{j\in S \wedge j\neq i} U_{ji}(\bm{r}_j-\bm{r}_i) \ ; \ i\in S$$

完全相同于Newton方程

### Hamilton 方程

Hamilton 方程通过使用 Hamiltonian:

$$H(\bm{r},\bm{p},t) = \frac 1 2 \sum_{i\in S}\frac {\bm{p}_i^2} {2m_i} + \frac 1 2 \sum_{i\neq j} U_{ji}(\bm{r}_j-\bm{r}_i)$$

连同正则方程来得到运动方程:

$$\frac {\td \bm{p}_i} {\td t} = -\frac {\partial H} {\partial \bm{r}_i} \ ; \ \frac {\td \bm{r}_i} {\td t} = \frac {\partial H} {\partial \bm{p}_i} \ ; \ i\in S$$

同前面的两类不同, 正则方程直接给出 \(2N\) 个一阶方程. 我们演算如下:

$$\begin{aligned}
\frac {\partial H} {\partial \bm{r}_i} &=\frac 1 2 \frac {\partial} {\partial \bm{r}_i} \sum_{i\neq j} U_{ji}(\bm{r}_j-\bm{r}_i) = \frac {\partial } {\partial \bm{r}_i}\sum_{j\in S \wedge j\neq i} U_{ji}(\bm{r}_j-\bm{r}_i) \\
\frac {\partial H} {\partial \bm{p}_i} &= \frac {\bm{p}_i} {2m_i}
\end{aligned}$$

因此正则方程直接给出的微分方程(组)是:

$$\frac {\td \bm{p}_i} {\td t} = -\frac {\partial } {\partial \bm{r}_i}\sum_{j\in S \wedge j\neq i} U_{ji}(\bm{r}_j-\bm{r}_i) \ ; \ \frac {\td \bm{r}_i} {\td t} = \frac {\bm{p}_i} {2m_i} \ ; \ i\in S$$

对第二个方程两边取 \(t\) 的导数代入第一个方程从而消去 \(\bm{p}_i\) , 我们有:

$$m_i \frac {\td^2} {\td t^2} \bm{r}_i(t) = -\frac {\partial } {\partial \bm{r}_i}\sum_{j\in S \wedge j\neq i} U_{ji}(\bm{r}_j-\bm{r}_i) \ ; \ i \in S$$

完全相同于Newton方程

## Hamilton方程和Lagrange方程的等价性

存在如下定理:

对于Lagrangian: \(L(\bm{r},\flo{\bm{r}},t)\) , 在假设我们能够施行它上的对 \(\flo{\bm{r}}\) 的 Legendre 变换(即假设 \(L\) 对 \(\flo{\bm{r}}\) 是凸的), 我们将得到函数:

$$H(\bm{r},\bm{p},t) = \sum_{i\in S}\bm{p}_i\cdot \flo{\bm{r}}_i - L(\bm{r},\flo{\bm{r}},t)$$

其中我们要求 \(\flo{\bm{r}}\) 的取值满足:

$$\bm{p} = \frac {\partial L} {\partial \flo{\bm{r}}} (\bm{r},\flo{\bm{r}},t)$$

我们将要证明的是, 以函数 \(H(\bm{r},\bm{p},t)\) 为 Hamiltonian 的正则方程将等价于 Lagrangian 的 Lagrange 方程. 我们需要计算如下几个出现在正则方程中的偏导数, 为了方便我们使用 \(\flo{\bm{r}} = \flo{\bm{r}}(\bm{r},\bm{p},t)\) 作为来自于上面对 \(\bm{p}\) 的要求的 \(\flo{\bm{r}}\) 取值.

$$\begin{aligned}
\frac {\partial H} {\partial \bm{r}_i} &= \sum_{j\in S} \bm{p}_j \cdot \frac {\partial \flo{\bm{r}}_j} {\partial \bm{r}_i} - \frac {\partial L} {\partial \bm{r}_i} - \sum_{j\in S}\frac {\partial L} {\partial \flo{\bm{r}}_j} \cdot \frac {\partial \flo{\bm{r}}_j} {\partial \bm{r}_i}\\
&= - \frac {\partial L} {\partial \bm{r}_i} \\
\\
\frac {\partial H} {\partial \bm{p}_i} &= \sum_{j\in S} \delta_{ji}\flo{\bm{r}}_j + \bm{p}_j \cdot \frac {\partial \flo{\bm{r}}_j} {\partial \bm{p}_i} - \sum_{j\in S} \frac {\partial L} {\partial \flo{\bm{r}}_j} \cdot \frac {\partial \flo{\bm{r}}_j} {\partial \bm{p}_i} \\
&= \flo{\bm{r}}_i
\end{aligned}$$

因此我们得到的正则方程将是如下形式:

$$\frac {\td \bm{p}_i} {\td t} = \frac {\partial L} {\partial \bm{r}_i} \ ; \ \frac {\td \bm{r}_i} {\td t} = \flo{\bm{r}}_i \ ; \ i\in S$$

注意这里仍然有 \(\bm{p} = \partial_{\flo{\bm{r}}} L(\bm{r},\flo{\bm{r}},t)\) 的关系. 将它代入第一个方程以消去 \(\bm{p}\) 我们得到:

$$\frac {\td } {\td t}\frac {\partial L} {\partial \flo{\bm{r}}_i} - \frac {\partial L} {\partial \bm{r}_i} = 0 \ ; \ i\in S$$

这正是Lagrange方程.
