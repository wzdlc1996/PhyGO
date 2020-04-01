# 为什么我们无法在宏观世界看到叠加态?

题目的问题事实上现在还没有一个公认的解答. 在这里, 我们将会分两部分来探讨这个问题, 希望能够对这个问题做出一定的整理.

## 相对态诠释

在 Everett 的最初的[文章](http://home.catv.ne.jp/dd/pub/tra/EverettHugh1957PhDThesis_BarrettComments.pdf)中, 他为了解决 Copenhagen 诠释的一些问题而提出了一个被他称作 **相对态(relative state)** 框架的对量子力学的解释. 这个框架随后被 Bryce DeWitt 及其他人推广成为现在的 **多世界诠释(Many-World Interpretation)** 的对量子力学的诠释.

在 MWI 中, 测量过程不在被解释为波函数的塌缩, 而被认为是系统 \(S\) 和观测者 \(A\) 的相互作用下的酉演化:

$$\ket{\psi_S}\otimes \ket{\psi_A} \rightarrow \sum_i c_i \ket{S_i}\otimes\ket{A_i}$$

其中描述观测者的基 \(\ket{A_i}\) 代表观测者 \(A\) 看到的系统态为 \(S_i\). MWI 认为整个系统的波函数在这个过程中分成了众多分支, 而观察者不可能独立于系统存在, 而作为波函数的一个部分出现. 这些分支被称为不同的世界. 如果以 Schrodinger 的猫为例, 我们能够写出:

$$\ket{cat}\otimes\ket{Observer} \rightarrow \ket{cat:alive}\otimes \ket{find~cat~alive}+\ket{cat:dead}\otimes\ket{find~cat~dead}$$

在打开盒子之前, 猫和观测者处在直积态. 打开盒子后, 这种相互作用带来了两个分支, 其中一个分支猫活着, 观察者看到猫是活得. 另一个分支则相反. 脱离观测者讨论孤立系统的猫是活是死是没有意义的.

在 MWI 中, 测量过程并没有出现波函数的塌缩, 而保持了量子力学的酉演化性质. 它同样能够解释所谓的 [Wigner's Friend](https://en.wikipedia.org/wiki/Wigner%27s_friend) 问题, 因为脱离外部观察者来讨论塌缩发生的时间没有意义. 孤立系统总是和外界处在直积态上.

## Prefered-basis Problem

这个问题的具体描述似乎都没有一个共识. 在这里, 我们用它指代为什么我们没有看到过所谓的 "宏观叠加态". 比如上面的 Schrodinger 猫的问题, 我们总是可以换一组基来写:

$$\begin{aligned}
\ket{cat}\otimes \ket{Observer} \rightarrow (\ket{cat:alive}+\ket{cat:dead})\otimes\ket{find~+~superposition} \\
+ (\ket{cat:alive}-\ket{cat:dead})\otimes\ket{find~-~superposition}
\end{aligned}$$

这个写法并不和 MWI 的框架冲突, 但这并非我们通常看到的现象. 真实世界中我们很少看到猫的生死叠加态. 但事实上, 这并不意味着我们无法看到叠加态, 我们总能写出:

$$\ket{cat:alive}=\frac 1 2 \Big((\ket{cat:alive}+\ket{cat:dead})+(\ket{cat:alive}-\ket{cat:dead})\Big)$$

因此, 我们可能需要回答的是, 为什么我们只能看到 \(\ket{cat:alive}\) 或者 \(\ket{cat:dead}\) 而不是它们的叠加. 而这也正是 Prefered-basis Problem.

这个问题依然是一个极为深刻且基本的问题. 推广来看, 它同样也是在质问我们为什么是使用现在这种形式来感受世界, 使用最自然的坐标基而不是如经典力学中做的那样能够任意选择广义坐标甚至通过正则变换构造出各种不同的坐标形式. 
