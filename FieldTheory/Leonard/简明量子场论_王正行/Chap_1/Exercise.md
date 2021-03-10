# Exercise in Chap. 1

## 1.1

### Problem

试表明: $\partial_\mu x^\nu = g_{\mu}^{\indent \nu}$, $\partial_\mu x_\nu = g_{\mu\nu}$, $\partial^\mu x_\nu = g^\mu_{\indent \nu}, \partial^\mu x^\nu = g^{\mu\nu}$


### Solution

从第一个等式出发, 由于:

$$\partial_{\mu} x^\nu = \frac {\partial} {\partial x^\mu} x^\nu = \delta_\mu^\nu = g_{\mu}^{\indent \nu} $$

然后通过 $g$ 的指标升降公式和 $g$ 的常数性(同 $\partial_\mu$) 对易. 即证

## 1.2

### Problem

试计算 $\partial^\mu e^{\frac 1 2 a x^2 + b x}$ 和 $\partial_\mu \partial_\nu e^{\frac 1 2  a x^2 + b x}$, 其中 $a$ 为常标量, $b^\mu$ 为4-vector

### Solution

$$\begin{aligned}
\partial^\mu \exp\Big(\frac 1 2 a x^2 + b x\Big) &= g^{\mu\nu} \partial_\nu\exp\Big(\frac 1 2 a x_\alpha x^\alpha + b_\alpha x^\alpha\Big) \\
&= g^{\mu\nu}\Big(\frac 1 2 a x_\alpha \delta_\nu^\alpha + \frac 1 2 a g_{\nu\alpha} x^\alpha + b_\alpha \delta_\nu^\alpha\Big)\exp\Big(\frac 1 2 a x^2 + b x\Big) \\
&=\Big(a x^\mu + b^\mu\Big)\exp\Big(\frac 1 2 a x^2 + b x\Big)
\end{aligned}$$

And

$$\begin{aligned}
\partial_\mu\partial_\nu \exp\Big(\frac 1 2 a x^2 + b x\Big) &= \partial_\mu \Big\{(ax_\nu + b_\nu)\exp\Big(\frac 1 2 a x^2 + b x\Big) \Big\} \\
&=g_{\mu\nu}\exp\Big(\frac 1 2 a x^2 + b x\Big) \\
&\indent + (ax_\nu + b_\nu)(ax_\mu+b_\mu)\exp\Big(\frac 1 2 a x^2 + b x\Big)
\end{aligned}$$

## 1.3

### Problem

证明微分算符 $\partial_\mu = \partial/\partial x^\mu$ 是四维协变矢量, $\partial^\mu$ 是四维逆变矢量, $\partial_\mu \partial^\mu$ 是四维标量.

### Solution

我们事实上只需要证明 $\partial_\mu$ 是4-协变矢量. 如下, 考察Lorentz变换 $\Lambda: x\mapsto x'= \Lambda x$, 即 $(x')^\mu = \Lambda^\mu_{\indent \nu} x^\nu$. 由于 Lorentz 变换保持伪欧度轨 $g_{\mu\nu} \Lambda^\mu_{\indent \alpha} \Lambda^\nu_{\indent \beta} = g_{\alpha\beta}$, 则:

$$g_{\nu\beta} x^\nu = g_{\mu\alpha}\Lambda^\mu_{\indent \nu}\Lambda^\alpha_{\indent \beta} x^\nu = g_{\mu\alpha} \Lambda^\alpha_{\indent \beta} (x')^\mu = \Lambda_{\mu \beta} (x')^\mu$$

两边乘 $g_{\beta}^{\indent \alpha}$ 并对 $\beta$ 缩并给出

$$x^\nu g_{\nu\beta}g_\beta^{\indent \alpha} = \Lambda_{\mu\beta} g_\beta^{\indent \alpha} (x')^\mu \Rightarrow x^\alpha = (x')^\mu\Lambda_{\mu}^{\indent \alpha}$$

因而:

$$\begin{aligned}
\partial_{\mu'} f &= \frac {\partial f} {\partial (x')^{\mu}} \\
&=\frac {\partial x^\nu} {\partial (x')^\mu} \partial_\nu f\\
&=\Lambda_{\mu}^{\indent \nu} \partial_\nu f
\end{aligned}$$

对任何函数 $f$ 成立, 换言之我们有:

$$\partial_{\mu'} = \Lambda_{\mu}^{\indent \nu} \partial_\nu$$

即 $\partial_\mu$ 在坐标变换下如一个协变矢量. 即证.