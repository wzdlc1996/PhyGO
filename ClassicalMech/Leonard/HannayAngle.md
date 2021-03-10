# Hannay Angle

**Hannay Angle** 是量子力学的 **Berry Phase** 在经典力学中的实现. 它在 Berry 1984 的[文章](https://royalsocietypublishing.org/doi/abs/10.1098/rspa.1984.0023)发表后, 由 J.H. Hannay 在他 1985 年的[文章](https://iopscience.iop.org/article/10.1088/0305-4470/18/2/011)中指出. 本文中我们将重点讨论经典力学中的 Hannay angle.

## 绝热不变量

这一部分我们将参考 Landau 的力学的第49节, 那里 Landau 称它为 "浸渐不变量".

考虑一个一维不含时 Hamilton 系统的封闭周期轨道的绝热演化, 系统的 Hamiltonian 中存在一个缓变(绝热)的参数 \(\lambda\) , 这个参数是含时的, 但它的变化相比于系统的周期是十分缓慢的:

$$T \frac {\td \lambda} {\td t} \ll \lambda$$

其中 \(T\) 为当 \(\lambda\) 为一常数时系统封闭轨道的周期. 我们来讨论这个过程中的(近似)不变量. 系统的 Hamiltonian 为 \(H = H(q,p;\lambda)\). 完整的运动方程被写为: (考虑到 \(\lambda\) 是时间的函数):

$$\begin{aligned}
\frac {\td q} {\td t} &= \frac {\partial H} {\partial p} (q, p, \lambda(t)) \\
\frac {\td p} {\td t} &= - \frac {\partial H} {\partial q} (q,p,\lambda(t))
\end{aligned}$$

这使得能量 \(E= H(q(t),p(t),\lambda(t))\) 自身作为动力学变量, 沿着运动轨迹有:

$$\frac {\td E} {\td t} = \frac {\partial H} {\partial q} \frac {\td q} {\td t} +\frac {\partial H} {\partial p} \frac {\td p} {\td t} + \frac {\partial H} {\partial t} = \frac {\partial H} {\partial \lambda} \frac {\td \lambda} {\td t}$$

如果我们对等号两边取快变量 \(q,p\) 的平均, 那么由于慢变量 \(\lambda\) 的变化速度 \(\frac {\td \lambda} {\td t}\) 同样是缓变的, 平均仅对 \(H\) 的导数进行:

$$\overline{\frac {\td E} {\td t}} = \frac {\td \lambda} {\td t}\overline {\frac {\partial H} {\partial \lambda}} = \frac {\td \lambda} {\td t} \frac 1 T \int_0^T \frac {\partial H} {\partial \lambda} (q(t;\lambda),p(t;\lambda),\lambda) \td t$$

由于快变量的缘故, 我们这里的时间平均事实上是沿着 \(\lambda\) 为常数的路径计算的. 这个路径的周期即为:

$$T = \oint \frac {\td q} {\flo{q}} = \oint \frac {\td q} {\partial H/\partial p}$$

类似的我们也可以使用这个策略改写上面对 \(H\) 偏导数的积分:

$$\overline {\frac {\td E} {\td t}} = \frac {\td \lambda} {\td t} \frac {\oint \frac {\partial_\lambda H (q, p, \lambda)} {\partial_p H(q,p,\lambda)} \td q} {\oint \frac {\td q} {\partial_p H(q,p,\lambda)}}$$

我们来分析等号右边的若干积分. 注意到积分的路径事实上是满足不含时正则方程:

$$\begin{aligned}
\frac {\partial q} {\partial t} (t, \lambda) = \frac {\partial H} {\partial p} (q,p,\lambda) \ ; \ \frac {\partial p} {\partial t}(t,\lambda) = -\frac {\partial H} {\partial q}(q,p,\lambda)
\end{aligned}$$

因此存在能量守恒:

$$H(q(t,\lambda),p(t,\lambda),\lambda) = E$$

这个式子定义了以 \(q\) 为变量的隐函数. 通常我们认为变量是 \(t,\lambda, E\), 但同样我们也可以使用 \(q\) 而代替 \(t\) 的地位, 从而为我们对上面的 \(q\) 的积分带来方便. 这时动量将成为: \(p = p(q,E,\lambda)\). 从而对上式两边取 \(\lambda\) 的导数我们给出:

$$\frac {\partial H} {\partial p} (q, p(q,E,\lambda),\lambda) \frac {\partial p} {\partial \lambda}(q,E,\lambda) + \frac {\partial H} {\partial \lambda}(q,p(q,E,\lambda),\lambda) = 0$$

而同时, 两边取 \(E\) 的偏导数:

$$\frac {\partial H} {\partial p} (q, p(q,E,\lambda),\lambda) \frac {\partial p} {\partial E}(q,E,\lambda) = 1$$

利用这几个关系, 我们可以进一步改写上面的能量导数的快变量平均:

$$\overline {\frac {\td E} {\td t}} = -\frac {\td \lambda} {\td t} \frac {\oint \frac {\partial p} {\partial \lambda}(q,E,\lambda)\td q} {\oint \frac {\partial p} {\partial E}(q,E,\lambda) \td q}$$

整理我们给出:

$$\oint \Big(\frac {\partial p} {\partial E} \overline {\frac {\td E} {\td t}} + \frac {\partial p} {\partial \lambda} \frac {\td \lambda} {\td t}\Big)\td q = 0$$

需要注意到 \(\overline{\frac {\td E} {\td t}}\) 是无关快变量的运动周期的, 因此它可以自由地写在积分号内. 这个式子事实上可以解释为:

$$\overline {\frac {\td I} {\td t}} = 0$$

其中:

$$I = \frac 1 {2\pi} \oint p \td q$$

为沿着确定能量 \(E\) 和固定缓变参数 \(\lambda\) 的一个运动周期的积分. 这个结论的意义正是, 在控制参量 \(\lambda\) 变化的足够缓慢时(绝热), 量 \(I\) 在控制参量变化的时间尺度上时不变的.

## 经典力学中的Berry Phase: Hannay Angle

### 作用-角变量

接下来我们仿照基于绝热定理来推导经典力学中 Berry Phase 的类比. 在量子力学中, 绝热定理预测在 Hamiltonian 中的参数缓慢变化时, 量子态在各个能级上的占据数是不变的, 但相位信息或者简并的 Hamiltonian 的特征子空间中的叠加系数存在变化. 在经典力学中, 我们已经看到了绝热不变量 \(I\) 是不变的, 因此几何相位将会出现在力学系统状态的另一个部分中. 为此我们先来讨论力学系统的状态除去 \(I\) 的信息.

绝热不变量 \(I\) 的计算, 由给定参数 \(\lambda\) 时的拥有确定能量 \(E\) 的周期运动 \(q,p\) 计算, 计算方式为 \(I = \frac 1 {2\pi} \oint p \td q\), 这个积分的结果正比于相空间周期轨道所包围的面积. 这意味着, \(I\) 只依赖于相空间中的封闭曲线的形状, 因此我们还需要一个变量 \(\phi\) 来确定给定时刻相点在曲线上的位置. 进而用 \(I\) 确定力学系统在哪个周期轨道, 同时用 \(\phi\) 确定力学系统在这条轨道上的位置.

现在我们考虑 \((I,\phi)\) 已经给出定义, 因此它同原本的系统状态 \((q,p)\) 应当是一一的:

$$\begin{cases}
I = I(q,p) &\\
\phi  = \phi(q,p)&
\end{cases} \ ; \
\begin{cases}
q = q(I,\phi)& \\
p = p(I,\phi)&
\end{cases}
$$

我们假设它们之间的关系由一个正则变换确定, 一个特殊的性质在于, \(I\) 事实上应当是守恒的, 因此这种正则变换的形式必定需要依赖于 Hamiltonian 本身. 同时 \(I\) 的守恒性导致了 \(\phi\) 的运动方程必定具有简单的形式: \(\flo{\phi} = \text{Const}\) . 从而 **这个正则变换的存在等价于力学系统是可积的**. 这事实上在我们现在讨论的一维不含时系统中总是成立的, 但普遍的来说并不一定. 这组正则坐标: \((I,\phi)\) 被称为 **作用-角变量**

下面我们考虑在参数 \(\lambda\) 缓慢变化时系统的运动. 在任意一个给定 \(\lambda\) 处, 都可以构造出作用-角变量的正则变换, 一般的, 变换的形式也依赖于 \(\lambda\) , 即:

$$\begin{cases}
I = I(q,p,\lambda) & \\
\phi = \phi(q,p,\lambda) &
\end{cases} \ ; \ K(I,\phi,\lambda) = H\Big(q(I,\phi,\lambda),p(I,\phi,\lambda),\lambda\Big)$$

在 \(\lambda\) 不变时, 成立正则方程: \(\flo{I} = -\partial K/\partial\phi = 0 \ ; \ \flo{\phi} = \partial K/\partial I\). 这意味着函数 \(K\) 事实上并不显含 \(\phi\), 因此我们接下来简记为 \(K(I,\lambda) = H(q(I,\phi,\lambda),p(I,\phi,\lambda),\lambda)\). 绝热情形我们已经看到, \(I\) 在绝热演化中保持不变, 现在我们考虑 \(\phi\) 的变化:

$$\frac {\td \phi} {\td t} = \frac {\partial \phi} {\partial q} \frac {\td q} {\td t} + \frac {\partial \phi} {\partial p} \frac {\td p} {\td t} + \frac {\partial \phi} {\partial \lambda} \frac {\td \lambda} {\td t} = \frac {\partial \phi} {\partial q} \frac {\partial H} {\partial p} -\frac {\partial \phi} {\partial p}\frac {\partial H} {\partial q} + \frac {\partial \phi} {\partial \lambda} \frac {\td \lambda} {\td t}$$

注意到作用-角变量的定义, 在 \(\lambda\) 给定时成立:

$$\frac {\partial K} {\partial I} = \flo{\phi}\Big|_{\td \lambda = 0} = \frac {\partial \phi} {\partial q} \frac {\partial H} {\partial p} - \frac {\partial \phi} {\partial p} \frac {\partial H} {\partial q} $$
