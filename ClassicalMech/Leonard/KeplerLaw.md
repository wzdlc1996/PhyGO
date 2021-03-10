# 天体运动读书报告

## 问题的提出

天体运动的最简单模型是一个两体问题, 两个物体相距很远, 因此可以被看作 **质点** , 在 **万有引力** 作用下开始运动. 考虑两个天体的质量分别为 \(M, m\), 位置矢量分别为 \(\bm{r}_1, \bm{r}_2\) . 那么系统的运动方程可以写为:

$$\begin{aligned}
M \frac {\td^2} {\td t^2} \bm{r}_1 &= -G\frac {M m} {|\bm{r}_1-\bm{r}_2|^{3}}(\bm{r}_1 - \bm{r}_2) \\
m \frac {\td^2} {\td t^2} \bm{r}_2 &= -G \frac {M m} {|\bm{r}_1 -\bm{r}_2|^3} (\bm{r}_2- \bm{r}_1)
\end{aligned}$$

为了简化问题, 我们使用两个天体的 **相对坐标** \(\bm{R}\) 和 **质心坐标** \(\bm{r}\) :

$$\begin{cases}
\bm{R} &= \frac {M \bm{r}_1 + m \bm{r}_2} {M+m} \\
\bm{r} &= \bm{r}_2 - \bm{r}_1
\end{cases} \ ; \
\begin{cases}
\bm{r}_1 &= \bm{R} - \frac {m} {m+M} \bm{r} \\
\bm{r}_2 &= \bm{R} + \frac {M} {m+M} \bm{r}
\end{cases}$$

代入坐标变换, 运动方程成为:

$$\begin{aligned}
\frac {\td^2 } {\td t^2}\bm{R} &= 0 \\
\frac {\td^2} {\td t^2} \bm{r} &= -G \frac {M+m} {|\bm{r}|^3} \bm{r}
\end{aligned}$$

从而原本的两体问题的相对坐标的运动方程成为了一个单体问题. (事实上, 对于一般的相互作用, 我们都可以做相似的处理. 利用 Newton 第三定律得到相对坐标的运动方程总是 \(\mu \overset{\cdot\cdot}{\bm{r}} = \bm{F}\) , 其中 \(\mu = m_1m_2/(m_1+m_2)\) 通常被称为 **约化质量** )

因此在接下来的问题中, 我们只考虑在 **有心力场** :

$$\bm{F}(\bm{r}) = - \frac {Am} {|\bm{r}|^3} \bm{r}$$

中质量为 \(m\) 的质点的运动, 换言之, 运动方程:

$$
\begin{equation}
m \frac {\td^2} {\td t^2} \bm{r} = - \frac {mA} {|\bm{r}|^3} \bm{r} \equiv \bm{F}(\bm{r})
\end{equation}$$

的解.

## 守恒量分析

Newton 力学中最重要的一个概念是守恒量. 确定了若干守恒量可以将二阶的运动方程重新整理为若干个一阶方程, 从而方便求解. 在这一部分, 我们将主要讨论给定运动方程中的守恒量.

### 角动量

对于质点, **角动量** 定义为: \(\bm{L} = \bm{r} \times \bm{p} = m \bm{r} \times \frac {\td} {\td t} \bm{r}\) . 角动量的运动方程为:

$$\frac {\td } {\td t} \bm{L} = m \Big(\frac {\td \bm{r}} {\td t} \times \frac {\td \bm{r}} {\td t} + \bm{r}\times \frac {\td^2 \bm{r}} {\td t^2}\Big) = 0$$

注意到 \(\bm{r}\) 的二阶导数依运动方程为中心力场作用, 因此它同 \(\bm{r}\) 的矢量积为 \(0\) . 从而角动量 \(\bm{L}\) 对时间的导数为 \(0\), 这意味着它是一个守恒量. 因此我们有:

$$\bm{r} \times \frac {\td \bm{r}} {\td t} = \bm{X} = \frac 1 m \bm{L}$$

为一常矢量.

### 能量

中心力场 \(\bm{F}(\bm{r}) = - Am \bm{r} / |\bm{r}|^3\) 是保守力场, 这意味着我们能够找到标量函数 \(U(\bm{r})\) 使得 \(\bm{F}(\bm{r}) = -\nabla U(\bm{r})\). 我们在这里给出它的形式:

$$U(\bm{r}) = - \frac {Am} {|\bm{r}|}$$

它的梯度很容易计算来验证它的确诱导出中心力场的形式. 下面我们证明标量函数:

$$E = \frac 1 2 m \Big(\frac {\td \bm{r}} {\td t}\Big)^2 + U(\bm{r})$$

是一个守恒量:

$$\begin{aligned}
\frac {\td E} {\td t} &= m \frac {\td \bm{r}} {\td t}\cdot \frac {\td^2 \bm{r}} {\td t^2} + \nabla U(\bm{r}) \cdot \frac {\td \bm{r}} {\td t} \\
&= \frac {\td \bm{r}} {\td t}\cdot \Big(m \frac {\td^2 \bm{r}} {\td t^2} - \bm{F}(\bm{r})\Big) = 0
\end{aligned}$$

得证. 接下来我们有:

$$\frac 1 2 \Big(\frac {\td \bm{r}} {\td t}\Big)^2 - \frac {A} {|\bm{r}|} = Y \equiv E/m$$

### Runge-Lenz 矢量

**Runge-Lenz 矢量** 是仅对平方反比中心力场守恒的一个特殊的守恒量, 它定义为:

$$\bm{V}_{RL} = \bm{p} \times \bm{L} - \frac {m^2 A} {|\bm{r}|} {\bm{r}}$$

我们来证明它在给定的中心力场 \(\bm{F}(\bm{r}) = -A m \bm{r} / |\bm{r}|^3\) 下是守恒的:

$$\begin{aligned}
\frac {\td \bm{V}_{RL}} {\td t} &= \frac {\td \bm{p}} {\td t}\times \bm{L} + \bm{p} \times \frac {\td \bm{L}} {\td t} - \frac {m^2 A} {|\bm{r}|^2}\Big(|\bm{r}|\frac {\td \bm{r}} {\td t} - \frac {\td |\bm{r}|} {\td t} \bm{r}\Big) \\
&= -\frac {mA} {|\bm{r}|^3} \bm{r} \times \bm{L} - \frac {m^2A} {|\bm{r}|} \frac {\td \bm{r}} {\td t} + \frac {m^2A} {|\bm{r}|^2} \frac {\td |\bm{r}|} {\td t} \bm{r}
\end{aligned}$$

注意其中我们使用了 \(\td \bm{L}/\td t = 0\). 而对于 \(|\bm{r}|\) 的导数我们使用如下等式:

$$2 |\bm{r}| \frac {\td } {\td t}|\bm{r}| = \frac {\td } {\td t} |\bm{r}|^2 = \frac {\td } {\td t} (\bm{r}\cdot \bm{r}) = 2\bm{r}\cdot \frac {\td \bm{r}} {\td t} $$

而对于 \(\bm{r}\) 和 \(\bm{L}\) 的矢量积, 我们有矢量公式: \(\bm{A}\times (\bm{B}\times \bm{C}) = (\bm{A}\cdot \bm{C})\bm{B} - (\bm{A}\cdot \bm{B})\bm{C}\), 从而有:

$$\begin{aligned}
\frac {\td \bm{V}_{RL}} {\td t} &= - \frac {m A} {|\bm{r}|^3} \Big((\bm{r}\cdot \bm{p})\bm{r} - |\bm{r}|^2 \bm{p}\Big) - \frac {mA} {|\bm{r}|} \bm{p} + \frac {m A} {|\bm{r}|^3} (\bm{r}\cdot \bm{p})\bm{r} \\
&=\frac {mA} {|\bm{r}|^3} |\bm{r}|^2 \bm{p} - \frac {mA} {|\bm{r}|}\bm{p} =0
\end{aligned}$$

即证守恒性. 接下来, 我们有:

$$\frac {\td \bm{r}} {\td t} \times(\bm{r}\times \frac {\td \bm{r}} {\td t}) - \frac A {|\bm{r}|} \bm{r} = \bm{Z}$$

## 运动方程的解

将两个守恒量整理如下:

$$\begin{aligned}
\bm{X} &= \bm{r}\times \frac {\td \bm{r}} {\td t} \\
Y &= \frac 1 2 \Big(\frac {\td \bm{r}} {\td t}\Big)^2 - \frac A {|\bm{r}|} \\
\bm{Z} &= \frac {\td \bm{r}} {\td t} \times \bm{X} - \frac A {|\bm{r}|} \bm{r}
\end{aligned}$$

运动方程是关于 \(\bm{r}\) 的三个分量的二阶微分方程, 因此方程的解拥有 \(6\) 个独立的待定参数需要由运动的初始条件决定. 我们这里使用关于 \(\bm{X}\) 和 \(\bm{Z}\) 的两个方程.

### 轨道方程

首先考虑在关于 \(\bm{X}\) 的方程两边对 \(\bm{r}\) 做内积, 这将得到:

$$\bm{X}\cdot \bm{r} = \Big(\bm{r}\times \frac {\td \bm{r}} {\td t}\Big)\cdot \bm{r} = 0$$

注意到 \(\bm{X}\) 是一个常矢量, 因此这个方程意味着质点的位置矢量总是在一个平面上, 换言之, 质点运动在一个平面轨道上. 再在关于 \(\bm{Z}\) 的方程两边同时作 \(\bm{r}\) 的内积:

$$\begin{aligned}
\bm{Z}\cdot \bm{r} &= \Big(\frac {\td \bm{r}} {\td t} \times \bm{X}\Big) \cdot \bm{r} - A |\bm{r}| \\
&= \Big(\bm{r}\times \frac {\td \bm{r}} {\td t}\Big) \cdot \bm{X} - A |\bm{r}| \\
&= |\bm{X}|^2 - A |\bm{r}|
\end{aligned}$$

令 \(|\bm{Z}| = Z \ ; \ |\bm{r}| = r \ ; \ |\bm{X}| = X\), 考虑矢量 \(\bm{r}\) 和矢量 \(\bm{Z}\) 的夹角为 \(\theta\), 则:

$$Z r \cos \theta = X^2 - A r \Rightarrow \frac 1 r = \frac {Z \cos\theta+A} {X^2}$$

根据 \(Z\) 和 \(A\) 的比值, 质点的运动轨道将呈现为不同的圆锥曲线. 这里我们假定了 \(X\neq 0\) 的条件, 如果 \(X=0\) , 则轨道为: \(\cos\theta = \text{Const}\). 意味着这是一条直线.

### 运动的时间依赖

轨道方程只是运动学方程消除掉时间 \(t\) 的结果, 为了给出具体的运动学方程: \(r(t), \theta(t)\), 我们需要一个坐标系. 首先讨论守恒矢量 \(\bm{Z}, \bm{X}\) 的关系:

$$\bm{Z}\cdot \bm{X} = -\frac A {|\bm{r}|}\bm{r}\cdot \Big(\bm{r}\times \frac {\td \bm{r}} {\td t}\Big) = 0$$

这意味着矢量 \(\bm{Z}\) 和矢量 \(\bm{X}\) 总是垂直的. 考虑以力场中心为原点, 根据 \(\bm{Z}\) 为 \(Ox\) 轴, \(\bm{X}\) 为 \(Oz\) 轴得到:

$$\begin{aligned}
\bm{Z} &= Z(1,0,0) \\
\bm{X} &= X(0,0,1) \\
\bm{X}\times \bm{Z} &= ZX (0,1,0)
\end{aligned}$$

注意到我们已经证明得到 \(\bm{r}(t) \cdot \bm{X} = 0\), 我们有: \(\bm{r}=r(\cos\theta, \sin\theta, 0)\), 从而我们有:

$$\begin{aligned}
X &= r\cos\theta \frac {\td (r \sin\theta)} {\td t} - r\sin\theta \frac {\td (r \cos\theta)} {\td t} \\
Z &= X \frac {\td (r\sin\theta)} {\td t} - A \cos\theta \\
0 &= -X \frac {\td (r\cos\theta)} {\td t} - A \sin\theta
\end{aligned}$$

考虑第三个方程:

$$\begin{aligned}
0 &= X \frac {\td r} {\td t} \cos\theta - X r \frac {\td \theta} {\td t}\sin\theta + A \sin\theta \\
&= X \frac {\td r} {\td \theta} \frac {\td \theta} {\td t} \cos\theta - X r \frac {\td \theta} {\td t}\sin\theta + A \sin\theta \\
&= X r \frac {Z\sin\theta} {A+Z\cos\theta} \frac {\td \theta} {\td t} \cos\theta - X r \frac {\td \theta} {\td t}\sin\theta + A \sin\theta \\
&= Xr \frac {\td \theta} {\td t} \frac {A\sin\theta} {A+Z\cos\theta} + A \sin\theta
\end{aligned}$$

假设 \(A\neq 0\) 以及 \(\theta\) 并不总是 \(0\) 或者 \(\pi\), 这个情况只能出现在直线轨道中. 基于这些假设我们得到了 \(\theta\) 的运动方程:

$$\frac {\td \theta} {\td t} = - \frac {(A+Z\cos\theta)^2} {X^3}\Rightarrow t-t_0 = -\int_{\theta_0}^{\theta} \frac {X^3 \td \theta} {(A+Z\cos\theta)^2}$$

配合轨道方程原则上我们能够给出完整的运动方程.

## Kepler 天体运行定律

从我们现有的对运动方程的理解, 我们能够推导出 Kepler 的三个天体运行定律:

### 第一定律

    所有行星绕太阳的轨道都是椭圆，太阳在椭圆的一个焦点上。

我们考察中心力场中的封闭轨道, 而这正是由轨道方程:

$$\frac 1 r = \frac {Z \cos \theta + A} {X^2}$$

决定, 封闭同时不坠入力心的轨道正是椭圆, 而力心则是椭圆的焦点. 联系到前面对两体运动的分析, 我们确定了 Kepler 的第一个定律.

### 第二定律

    行星和太阳的连线在相等的时间间隔内扫过相等的面积。

我们考察质点和力心的连线在微小时间间隔 \(\td t\) 内扫过的面积, 它近似为一个微小三角形, 因此面积可以通过矢量积的模来长度来计算:

$$\td S = |\bm{r} \times \td \bm{r}| = X \td t$$

由于 \(\bm{X}\) 的守恒特性, 我们有: \(\td S/ \td t = \text{Const}\) , 这意味着单位时间间隔内扫过的面积总是一个常数, 因此我们确定了 Kepler 的第二个定律.

### 第三定律

    所有行星绕太阳一周的恒星时间的平方与它们轨道长半轴的立方成比例

考虑由轨道方程确定的椭圆: \(\frac 1 r = \frac {1} {a(1-e^2)} (e \cos\theta + 1)\), 其中 \(e = Z/A\) 为椭圆的离心率, 而 \(a=\frac {X^2} {A(1-e^2)}\) 为椭圆的半长轴长. 因此由第二定律:

$$T = \frac {S} {X} = \frac {\pi a^2 \sqrt{1-e^2}} {X}$$

计算 \(\bm{Z}\) 的模我们有(注意到, \(\bm{r}\) 和 \(\bm{X}\) 总是垂直的):

$$\begin{aligned}
Z^2 &= \bm{Z}\cdot \bm{Z} = \Big|\frac {\td \bm{r}} {\td t} \times \bm{X}\Big|^2 + A^2 -\frac {2A} {|\bm{r}|} \bm{r}\cdot \Big(\frac {\td \bm{r}} {\td t} \times \bm{X}\Big) \\
&=\Big(\frac {\td \bm{r}} {\td t}\Big)^2 X^2 + A^2 - \frac {2A} {|\bm{r}|} \bm{X}\cdot \Big(\bm{r}\times \frac {\td \bm{r}} {\td t}\Big) \\
&=2(Y + A/|\bm{r}|) X^2 + A^2 - \frac {2A X^2} {|\bm{r}|} \\
&=2Y X^2 + A^2
\end{aligned}$$

我们使用了 \(Y = \frac {1} 2 \Big(\frac {\td \bm{r}} {\td t}\Big)^2 - \frac {A} {|\bm{r}|}\) 同样是个守恒量. 从而, 我们有:

$$\begin{aligned}
T^2 &=\pi^2 \frac {a^4} {X^2} \Big(1 - \frac {2YX^2+A^2} {A^2}\Big) \\
&=- \pi^2 \frac {2a^4 Y} {A^2}
\end{aligned}$$

考虑质点运行在椭圆靠近焦点的顶点附近时, 我们有 \(\td \bm{r} /\td t \cdot \bm{r} = 0\), 以及 \(r = a-ae\), 考虑守恒量 \(X,Y\), 有:

$$\begin{aligned}
X &= (1-e)a\cdot v\\
Y &= \frac 1 2 v^2 - \frac {A} {a(1-e)}
\end{aligned}$$

从而有:

$$\begin{aligned}
Y &= \frac 1 2 \frac {X^2} {(1-e)^2 a^2} - \frac {A} {a(1-e)} \\
&= \frac 1 2 \frac {X^2} {(1-e)^2} \Big(\frac {A(1-e^2)} {X^2}\Big)^2 - \frac {A} {1-e} \frac {A (1-e^2)} {X^2} \\
&= -\frac {1 } 2 \frac {A^2} {X^2} (1-e^2) \\
&= - \frac {A} {2a}
\end{aligned}$$

从而我们最终有:

$$T^2 = \pi^2 \frac {a^3} {A} \propto a^3$$

故我们得到了 Kepler 的第三定律
