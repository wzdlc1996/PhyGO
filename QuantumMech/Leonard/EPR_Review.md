# EPR文章相关讨论

## 简介

我们将在这里讨论 Einstein 在 1935 年的著名文章: [Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?](https://journals.aps.org/pr/abstract/10.1103/PhysRev.47.777). 从某种程度上我们可以将这篇文章看作是 **量子纠缠(Quantum Entanglement)** 概念被人们注意到并且重点研究的开端.

## EPR 文章的逻辑

首先我们在这里重新将EPR文章的逻辑整理如下. 作者(指 EPR 文章的三位作者, 同样指 EPR 的提出者)在文章中做了如下的定义:

> ..., without in any way disturbing a system, we can predict with certainty(i.e., with probability equal to unity) the value of a physical quantity, then there exists an element of physical reality corresponding to this physical quantity

**物理实在** : 物理实在可以被描述为一组变量, 这组变量可以再不影响系统状态的同时被唯一确定

同时作者在文章中声明了所谓一个物理理论是完备的的必要条件:

> ... the term complete, the following requirement for a complete theory seems to be a necessary one: every element of the physical reality must have a counterpart in the physical theory

亦即, 如果一个物理理论是 **完备的** , 那么所有物理实在应当在理论中有对应的描述.

接下来, 作者考虑了量子力学中的一类拥有两个子系统组成的系统, 我们使用 Dirac 符号来描述作者的思想实验. 系统 \(S\) 的状态 \(\ket{\Psi}\) 总是可以写为两个子系统 \(A, B\) 上态的直积的线性组合. 我们考虑使用 \(A\) 上的算符 \(\hat P_A\) 的一组本征态 \(\{\ket{p_i}\}\) 来展开:

$$\ket{\Psi} = \sum_i c_i \ket{p_i} \ket{\psi_i}$$

同样, 我们也可以将之写为另一种方式, 即按照 \(A\) 上的算符 \(\hat Q_A\) 的一组本征态: \(\{\ket{q_i}\}\) 来展开:

$$\ket{\Psi} = \sum_i d_i \ket{q_i} \ket{\phi_i}$$

作者指出, 一旦 \(A, B\) 被分开的足够远使得两者之间不会有相互作用的情况下, 通过合适的构造能够让 \(\{\ket{\psi_i}\}\) 和 \(\{\ket{\phi_i}\}\) 分别是两个不对易算符的本征态, 文章中为:

$$\begin{aligned}
\Big(\bra{x_A}\otimes\bra{x_B}\Big)\ket{\Psi}
&= \Big(\bra{x_A}\otimes\bra{x_B}\Big)\sum_p \ket{p_A=p}\otimes\ket{p_B=-p} \\
&=\Big(\bra{x_A}\otimes\bra{x_B}\Big)\sum_x \ket{x_A= x}\otimes\ket{x_B = x}\\
&\sim \int_{-\infty}^{\infty} e^{\ti (x_A-x_B) p /\hbar}\td p
\end{aligned}$$

其中\(x_\alpha, p_\alpha \ ; \ \alpha=A,B\) 分别为两个子系统的坐标和动量.

换言之, 针对 \(A\) 分别测量 \(\hat P_A,\hat Q_A\) , 我们就可以在不影响 \(B\) (由于无相互作用, 或在一定时间内作用尚未造成作用(类空间隔, 这个修改的观点是由 Bohm 在1951年提出的. [参见Wiki](https://en.wikipedia.org/wiki/EPR_paradox#Einstein's_own_argument))) 的条件下得到 \(B\) 上一对不对易算符的测量值. 这意味着两个不对易算符对应的变量应当都是物理实在.

如果量子力学的波函数描述 (或者说 Copenhagen 诠释) 是完备的, 那么子系 \(B\) 的坐标和动量无法同时为物理实在, 由于波函数仅是坐标或者动量的函数. 因此, 在如下的条件下:

1.  当两个系统相距足够远(类空间隔)的情况下, 对其中一个系统的测量不会影响到另一个系统
2.  量子力学的基本假设, 如有关波函数, 测量, 和力学量算符等

我们有如下两个结论:

1.  一对不对易算符 **可以同时** 对应物理实在 (这里的同时应解释为)
2.  量子力学的波函数描述是 **完备的** \(\Rightarrow\) 一对不对易算符 **不能同时** 对应物理实在

这两个结论立即导出:

量子力学的波函数描述 (或者说 Copenhagen 诠释) 是不完备的.

## 量子纠缠

接下来我们沿用 Bohm 的修改的观点来看, EPR 给出了一种量子力学系统的可能性, 在这个系统里对一个部分的测量似乎可以瞬间影响到另一个部分, 不论两部分相距多远. 这种 "鬼魅般的超距作用(spooky action at distance, by Einstein)" 被看作是量子纠缠.

在量子力学的框架内, 导致量子纠缠的根本原因事实上是量子力学的基本假设之一: 态叠加原理. 而将纠缠表现出来的是对波函数的诠释. 纠缠机制并非是某种作用, 因为它并不能被真正的写作一个局域的 Hamiltonian.

当我们按照 EPR 的方式来讨论纠缠时, 对于一个纠缠态 (定义在两个双态系统 \(A+B\) 的直积 Hilbert 空间 \(\mathcal{H}_A\otimes \mathcal{H}_B\) 上): \(\ket{1}\ket{0}-\ket{0}\ket{1}\) , 对于系统 \(A\) 的测量的描述由算符:

$$\hat P = \hat P_A \otimes \hat I$$

来描述, 其中 \(\hat P_A\) 是定义在 \(\mathcal{H}_A\) 由测量的力学量的本征态确定的投影算符. 这里它是 \(\ket{1}\bra{1}\) 或者 \(\ket{0}\bra{0}\) . 如果我们测量到态 \(\ket{1}\bra{1}\) 的话, 测量后的末态将会是

$$\ket{1}\bra{1}\otimes \hat I \Big(\ket{1}\ket{0}-\ket{0}\ket{1}\Big) = \ket{1}\ket{0}$$

我们使用的算符并没有体现出来 \(A,B\) 系统的相互作用, 测量瞬间 \(B\) 系统信息的丢失 (这里的所谓信息丢失事实上是由于 **塌缩假设(Collapse Postulate)**, 如果我们在多世界理论的框架下看的话, 这个过程仍然是酉的, 而且没有任何信息丢失了) 事实上完全来自于算符 \(\hat P\) 是线性作用在系统的量子态上的. 这意味着量子力学的线性结构直接导致了纠缠行为的存在. 从这里的讨论, 我们可以肯定的是, EPR 论证非完备性的两个前提并不都是成立的. 事实上, 在量子力学的基本假设下我们的确看到了, 对其中一个系统的测量影响到了另一个系统. 但这种影响是和通常我们讨论的相互作用完全不同的. 通常相互作用由系统的 Hamiltonian 来描述: 我们称算符未描述两体 \(A, B\) 的相互作用, 如果它在两体各自的 Hilbert 子空间的至少一个上是单位算符. 对于这样的两体 Hamiltonian:

$$\hat H = \hat H_A \otimes \hat I_B + \hat I_A \otimes \hat H_B$$

描述的演化, 我们能够证明它不能影响 \(A + B\) 系统上的纠缠, 包括纠缠的产生或者说是消失. 事实上, 更加普遍的系统可能是多体的, 我们的 Hamiltonian 中有着诸如 "近邻" 相互作用的项, 如开边界 XXZ model:

$$\hat H = \sum_{i=1}^{N-1} J_1 (\sigma_i^x \sigma_{i+1}^x + \sigma_i^y\sigma_{i+1}^y)+ J_2 \sigma_i^z\sigma_{i+1}^z$$

在这类系统中, Hamiltonian 可能并没有描述相互 "远离" (这里我们事实上没有先验的空间概念, 所谓远离是相对 Hamiltonian 而言的) 的两个 sites 之间的作用, 如第 1 个和第 N 个 site. 由于相互作用的传递机制, 尽管没有直接的相互作用项, 但纠缠依然可能会产生. 但这种纠缠也不会瞬时产生, 根据 Hamiltonian 的配置这里存在一个类似 Lieb-Robinson bound 的概念.

## 结论

我们分析了 EPR 文章的逻辑, 指出了其中论证的非局域性的问题所在, 同时也提出了对这个问题的看法: 量子纠缠事实上并非一个非局域作用.
