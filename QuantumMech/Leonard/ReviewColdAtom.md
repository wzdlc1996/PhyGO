# 量子模拟与冷原子技术

## 摘要

从量子力学在19世纪20年代建立以来, 对其理论的讨论和认识的深化就从来没有停止过. 而同时, 对量子理论的实验检验同样一直在发展. 由于量子力学理论框架内蕴的指数爆炸问题, 人们一直在致力于找到一种完善的可控的方法来对任意的量子系统进行可操作的实验研究. 传统的电子体系作为最早量子论试图解决的对象由于其过于微观且可控性较差在这个层面上反而并不是最优的. 随着19世纪80年代以来的激光技术的飞速发展, 激光作用下的原子体系渐渐进入了人们的视线, 并作为接近于完美的研究工具活跃在量子信息, 量子动力学, 统计力学等学科的前沿. 本文我们将讨论冷原子技术的理论基础, 并主要讨论它在量子模拟领域的应用.

## 量子模拟

对量子力学的计算领域的研究首先认识到量子力学理论框架内蕴的巨大问题: 指数爆炸(1). 我们可以从一个简单情况来认识这一现象. 考虑一个由 \(N\) 个 \(1/2\) 自旋组成的系统, 而这个系统的动力学演化由 Schrodinger 方程描述:

$$\ti \hbar \frac {\td } {\td t} \ket{\psi(t)} = \hat H \ket{\psi(t)}$$

如果我们想要计算出它任意时刻的演化, 我们需要将离散化时间的态矢量 \(\ket{\psi(t_i)}\) 和 Hamiltonian 做编码. 最直接的编码手段是将其在直积态 \(\ket{1,0,\cdots}\) 上投影的概率幅与矩阵元作为向量存储. 如果我们需要考察 \(m\) 个时间点(这通常是一个确定的数值), 那么整个系统我们的存储消耗由这些时间点的态矢量和 Hamiltonian 的复数元素决定:

$$\text{Memory Cost} = 2\times\text{Precision Cost}\times(2^N m + 2^N \times 2^N) \sim \mathcal{O}(4^N)$$

这种指数增长的资源消耗不仅出现在存储上, 运算的消耗是相当量级的. 而且这种现象也不止发生在自旋系统, 事实上, 对于任意的系统, 如果它的构型空间消耗的资源量级为 \(N\) (这同样是这个系统的经典力学模拟的消耗), 那么它的量子力学模拟的消耗通常随着 \(N\) 呈指数增长的 (只有在某些特殊体系我们能够使用对称性等手段对资源消耗进行简化).

我们可以做一个简单的数量上的计算, 对于 \(N=40\) 的情况, 这个规模仍然属于较小的量子系统, 上面估计的存储消耗将是 \(4^{40} \sim 10^{24}\) , 这个数值已经远远超过了地球上沙子的个数(\(\sim 10^{18}\)) (2), 因此模拟这个系统已经远远超出了任何地球上可以制造的经典计算机的能力范围. 当然, 实际的物理系统中的 Hamiltonian 由于对称性和局域性等限制并不会带来如此巨大的消耗, 这个数值事实上是消耗的上界.

为了解决这个问题, 在1982年 Feynman 首次提出了使用一个量子系统来实现量子模拟的设想(3). 这个设想后来被发展为量子计算机的理论. 简而言之, 量子模拟的方法论可以分为四步:

1.  建立目标系统和模拟器(Simulator)之间的映射, 量子态和力学量算符
2.  制备初态
3.  实现量子演化
4.  测量和信息提取

初态的制备和最后的测量与信息提取事实上仍然是相当困难的, 但本文中并不会过多地涉及这部分的问题. 而基于映射和量子演化的实现的不同, 量子模拟可以大致分为两类: 数字法和模拟法(Digit and Analog). 前者试图通过使用一定数量的量子门来逼近任意量子演化算符, 而后者则相对直接, 试图通过构造出同目标系统类似的量子系统的时间演化. 由于普遍地将任意酉算符 \(\hat U\) 分解为量子门的乘积仍然是个未解决的问题, 而模拟法同目标系统的高度一致性, 后者某种意义上是一种更 "好" 的实现量子模拟的办法.

实现模拟法的量子模拟我们需要找到一类我们能够相当好地控制的体系. 一般的从实际体系出发我们并不能构造出任意的演化, 但好在物理研究的需求通常来说并没有数学广泛, 我们关注的总是所谓物理上许可的系统, 因此从实际体系出发能够建立的演化已经相当好地满足了我们的需求. 时至今日, 人们能够很好控制的体系已经有很多: 原子-分子, 离子, 超导线路, 光子体系等. 本文中我们将讨论光晶格中的冷原子体系. 这个体系能够很好地实现一类格点模型, 并且模型中的包括相互作用在内的参数是可调的, 这为这种技术带来了蓬勃旺盛的生命力.

## 冷原子技术

### 中性原子和经典光场的作用

在偶极近似下, 中性原子在外光场中的 Hamiltonian 可以写为:

$$H = \frac {\bm{p}^2} {2m} + H_{\text{internal}} - \bm{\mu} \cdot \bm{E}(\bm{x},t) \cos \omega t$$

其中光场 \(\bm{E}(\bm{x},t)\) 在原子尺度和时间尺度 \(1/\omega\) 上是缓变的. 作为一个粗糙的讨论(5), 我们这样考察光场的影响: 光场的存在将为中性原子诱导出极矩, 这个的最低阶近似是线性于 \(\bm{E}\) 的:

$$\bm{\mu} = \bm{A} \bm{E}(\bm{x},t) \cos \omega t$$

在光场带来的原子内部能级跃迁可以忽略时, 光场带来的原子能量变化事实上可以写为:

$$\Delta H(\bm{x},t) \propto \sum_{i,j=x,y,z} A_{ij} E^i(\bm{x},t)E^j(\bm{x},t)$$

这使得单中性原子在光场中的有效 Hamiltonian 可以写为:

$$H = \frac {\bm{p}^2} {2m} + V_{\text{opt}}(\bm{x},t)$$

其中 \(V_{\text{opt}} \propto \sum_{i,j} A_{ij} E^i(\bm{x},t)E^j(\bm{x},t)\). 这意味着利用光场我们可以相当自由地构造三维势场, 而其中的原子则呈现出势场中的运动. 在极低温时, 一方面量子行为变得重要, 另一方面光场势 \(V_{\text{opt}}\) 的影响变得显著, 使得我们能够在这样的体系中构建起一大类供研究的量子系统.

上面我们对光场中原子的运动的讨论是相当粗糙的, 但它给我们的光场势是光场的二次项这一点事实上是正确的. 更严格的讨论可以参考(6, 7)

### 光晶格中的相互作用原子气体与 Hubbard Model

这一部分, 我们将讨论光晶格中有着一类相互作用的原子气体是如何同格点模型联系起来的. 主要数学细节参考的是(7).

一般的, 光场中低密度, 低温情况下的微弱相互作用气体可以使用点相互作用的 Hamiltonian 描述:

$$\hat H = \int \td^3 \bm{x} \ \hat \psi^\dagger(\bm{x}) \Big(-\frac {\hbar^2 \nabla^2} {2m} + V_{\text{opt}}(\bm{x})\Big)\hat \psi(\bm{x}) + \frac g 2 \int \td^3 \bm{x} \ \hat \psi^\dagger(\bm{x})\hat \psi^\dagger(\bm{x})\hat \psi(\bm{x})\hat \psi(\bm{x})$$

其中 \(V_{\text{opt}}(\bm{x})\) 是光场势. 对于周期性的光晶格, 我们总能够找到一组在实空间局域的 Wannier 函数, 它们组成了一组完备的单粒子基:

$$w_n(\bm{x}-\bm{R}) \propto \sum_{\bm{k}, m} e^{-\ti \bm{k}\cdot \bm{R}} U_{nm}(\bm{k}) u_{m, \bm{k}}(\bm{x})$$

其中 \(U_{mn}\) 是一个自由的使多个能带混合的酉算符, 同时满足条件: \(U_{nm}(\bm{k}+\bm{G}) = U_{nm}(\bm{k})\). 从而我们总可以将场算符写为:

$$\hat \psi(\bm{x}) = \sum_{\bm{R}}\sum_n w_n(\bm{x} - \bm{R})\hat b_{n,\bm{R}}$$

其中 \(\bm{R}=n_1 \bm{a}_1 + n_2 \bm{a}_2+n_3 \bm{a}_3\) 是晶格位置. 从而我们可以得到基于 \(\hat b_{n,\bm{R}}\) 的 Hamiltonian:

$$\hat H = \sum_{n,n'}\sum_{\bm{R},\bm{R'}} \Big\{\int \td^3 \bm{x} \ w_n^*(\bm{x}-\bm{R})\Big(-\frac {\hbar^2 \nabla^2} {2m} + V_{\text{opt}}(\bm{x})\Big)w_{n'}(\bm{x}-\bm{R'})\Big\} \hat b_{n',\bm{R'}}^\dagger \hat b_{n,\bm{R}} \\
+ \sum_{n,n';m,m'}\sum_{\bm{R}_1,\bm{R}_1';\bm{R}_2,\bm{R}_2'} \frac g 2\Big\{\int \td^3 \bm{x} \ w_{n}^*(\bm{x}-\bm{R}_1)w_{m}^*(\bm{x}-\bm{R}_2)w_{m'}(\bm{x}-\bm{R}_2')w_{n'}(\bm{x}-\bm{R_1'})\Big\}b_{n,\bm{R}_1}^\dagger b_{m,\bm{R}_2}^\dagger \hat b_{m',\bm{R}_2'} \hat b_{n',\bm{R}_1'}$$

一个简单情形是我们的原子只在一条能带上运动(极低温), 而 Wannier 函数局域性非常好使得上面的积分只有几项非零(由于 Wannier 函数中存在一个酉变换的自由度, 因此通常我们会试图去找到最局域的 Wannier 函数, 这项工作已经有着一个开源软件做了一定贡献, 而且仍然在发展中 (8,9) ). 在这个近似下 Hamiltonian 简化为:

$$\hat H = \sum_i \epsilon_i \hat b_i^\dagger \hat b_i + \sum_{<i,j>} J_{ij} \hat b_i^\dagger \hat b_j + \frac U 2 \sum_i \hat b_i^\dagger \hat b_i^\dagger \hat b_i\hat b_i$$

其中:

$$\begin{aligned}
J_{ij} &= \int \td^3 \bm{x} \ w_0^*(\bm{x}-\bm{R}_i)\Big(-\frac {\hbar^2 \nabla^2} {2m} + V_{\text{opt}}(\bm{x})\Big) w_0(\bm{x}-\bm{R}_j) \\
\epsilon_i &= \int \td^3 \bm{x} \ w_0^*(\bm{x}-\bm{R}_i)\Big(-\frac {\hbar^2 \nabla^2} {2m} + V_{\text{opt}}(\bm{x})\Big) w_0(\bm{x}-\bm{R}_i) \\
U &= g\int \td^3 \bm{x} \ |w_0(\bm{x}-\bm{R})|^4
\end{aligned}$$

在光场为周期势场时, \(\epsilon_i\) 事实上和格点位置无关, \(J_{ij}\) 仅和近邻格点的配置(晶格几何形状)有关而于位置无关. 但更普遍的情况中我们会为系统加入在晶格尺度上缓变的额外势从而引入并非常数的 \(\epsilon_i\). 根据我们设计系统时使用的原子, 算符 \(\hat b_i\) 之间服从对易或者反对易关系. 这使得我们构造出了对 Boson 或者 Fermion 的格点模型. 通过调节光晶格的形状和晶格深度, 我们能够调节格点模型的几何以及相互作用 \(U\) 和晶格之间的 hopping (即动能项) \(J\) 和 on-site 能量 \(\epsilon_i\).

在完成了 Hubbard 模型的构造之后, 我们就可以基于此实现更广泛的系统. 如自旋系统作为格点模型的一种极限情况等.

## 总结

我们讨论了如何从光晶格构造一类广泛的量子系统: Hubbard Model. 使用这种技术我们能够有效地进行量子模拟的研究, 并且在进一步的应用中实现量子算法, 构造量子计算机等. 

## 参考文献

1.  Georgescu, I. M., Ashhab, S., & Nori, F. (2014). Quantum simulation. Reviews of Modern Physics, 86(1), 153–185. https://doi.org/10.1103/RevModPhys.86.153
2.  https://www.quora.com/How-many-grains-of-sand-are-there-on-Earth-and-how-many-stars-are-there-in-the-universe
3.  Feynman, R. P. (1982). Simulating physics with computers. International Journal of Theoretical Physics, 21(6–7), 467–488. https://doi.org/10.1007/BF02650179
4.  https://en.wikipedia.org/wiki/Rotating_wave_approximation
5.  Lewenstein, M., Sanpera, A., Ahufinger, V., Damski, B., Sen, A., & Sen, U. (2007). Ultracold atomic gases in optical lattices: Mimicking condensed matter physics and beyond. Advances in Physics, 56(2), 243–379. https://doi.org/10.1080/00018730701223200
5.  Kobe, D. H. (1983). Gauge invariant derivation of the AC Stark shift. Journal of Physics B: Atomic and Molecular Physics, 16(7), 1159–1169. https://doi.org/10.1088/0022-3700/16/7/008
6.  Haas, M., Jentschura, U. D., & Keitel, C. H. (2006). Comparison of classical and second quantized description of the dynamic Stark shift. American Journal of Physics, 74(1), 77–81. https://doi.org/10.1119/1.2140742
7.  Walters, R., Cotugno, G., Johnson, T. H., Clark, S. R., & Jaksch, D. (2013). Ab initio derivation of Hubbard models for cold atoms in optical lattices. Physical Review A - Atomic, Molecular, and Optical Physics, 87(4), 1–13. https://doi.org/10.1103/PhysRevA.87.043613
8.  Mostofi, A. A., Yates, J. R., Lee, Y. S., Souza, I., Vanderbilt, D., & Marzari, N. (2008). wannier90: A tool for obtaining maximally-localised Wannier functions. Computer Physics Communications, 178(9), 685–699. https://doi.org/10.1016/j.cpc.2007.11.016
9.  Mostofi, A. A., Yates, J. R., Lee, Y. S., Souza, I., Vanderbilt, D., & Marzari, N. (2008). wannier90: A tool for obtaining maximally-localised Wannier functions. Computer Physics Communications, 178(9), 685–699. https://doi.org/10.1016/j.cpc.2007.11.016
