# 约化相空间读书报告

本篇读书报告主要参考 Arnold 的"经典力学的数学方法"的附录5: 具有对称性的动力系统

## 李群在辛流形上的作用

考虑辛流形 \((M^{2n},\omega^2)\) 和它上面的辛微分同胚群 \(G\) : 群 \(G\) 中的元素是 \(M^{2n}\) 上的微分同胚, 并且在拉回的意义上保持着它的辛形式 \(\omega^2\), 即:

$$\forall g \in G, \forall x \in M^{2n}, \xi,\eta \in TM^{2n}_x, \omega^2(\xi,\eta) = \omega^2(g_* \xi, g_* \eta)$$

其中 \(g_*\) 为映射 \(g\) 的微分, 它将点 \(x\) 处的切空间 \(TM^{2n}_x\) 映向 \(g(x)\) 处的切空间 \(TM^{2n}_{gx}\). 而其定义可以直观地通过 \(g\) 对过 \(x\) 点的路径的作用得到: \(g_*\) 对路径在 \(x\) 点的切矢量的像正是该路径在 \(g\) 下的像在 \(g(x)\) 点的切矢量:

$$\forall v \in TM^{2n}_x, g_* v = \frac {\td } {\td t} g\circ x(t)\Big|_{t=0} \ ; \ \text{where } v = \frac {\td } {\td t} x(t)\Big|_{t=0}$$

因而 \(G\) 的元素都是保持辛构造的, 换言之, 任意 \(G\) 的单参数子群将定义一个辛流形上的相流. 我们自然期待这个相流应当被一个哈密顿函数来描述:

$$\frac {\td } {\td t} g^t x \Big|_{t=0}= I \td H(x)$$

其中 \(I : T^*M^{2n} \rightarrow TM^{2n}\) 在标准坐标 (\(\omega^2 = \td q \wedge \td p\)) 下有着矩阵元:

$$I = \begin{bmatrix}\bm{0} & \bm{E} \\ -\bm{E} & \bm{0} \end{bmatrix}$$

所谓的李群的泊松作用也正是在这个基础上定义的:

> 一个连通李群 \(G\) 在辛流形 \((M^{2n},\omega^2)\) 上的作用被称为 **泊松作用**, 如果它的每个单参数子群都拥有一个单值的哈密顿函数, 而且选取得线性依赖于李代数的元, 并使交换子的哈密顿函数等于哈密顿函数的泊松括弧:
>
> $$H_{[a,b]} = (H_a,H_b)$$

我们考虑定义中提到的线性性. 上面已经看到如何将单参数子群的生成元同哈密顿函数联系起来, 那么我们总可以找到一组李代数的基 \(\{X_i\}\) 使得任意 \(G\) 的单参数子群总能够写为:

$$G \supset \{g^t = \exp(t \sum_i a_i X_i) : t\in \mathbb{R}\} = G_g$$

进而按照上面将 \(G_g\) 所定义之相流同它的哈密顿函数联系起来的式子可以让我们看到(注意哈密顿函数允许一个自由的可加常数, 因此我们将能够选择这个常数使得线性性成立):

$$H_{\sum_i a_i X_i} = \sum_i a_i H_{X_i}$$

而泊松括弧同李代数之间的关系同样也是合理的要求. 从而泊松作用事实上联系起来了三个对象: 辛流形上的李群的李代数, 辛流形上的矢量场, 矢量场的哈密顿函数. 其中哈密顿函数连同泊松括弧事实上实现了李群的李代数的一个同态.

## 构型空间上微分同胚的泊松作用

为了更好地理解泊松作用, 我们考虑构型空间 \(V\) 上的真实的力学系统. 设 \(G\) 是在 \(V\) 上作用的微分同胚群, 而力学系统的辛流形正是 \(V\) 的余切丛: \(M= T^* V\), 我们使用使得它上面的自然辛构造为标准形式的坐标, 即: \(\omega^2 = \td p \wedge \td q\). \(G\) 中的元素在 \(M\) 上的作用被自然定义为:

$$g \in G, x=(q,p)\in M\Rightarrow gx = (gq, g^* p) \in M$$

其中 \(g^*:T^*V_{q} \rightarrow T^*V_{gq}\) 的定义类似于 \(g\) 的微分, 但它联系的是余切空间: 它正是 \(g_*\) 的对偶. 我们可以检查这样定义的作用是 \(M\) 上的辛作用: 注意到 \(\omega^2 = \td \omega^1\) 其中 \(\omega^1 = p\td q\) 是 \(T^*V\) 上的典则辛形式. 而 \(g\) 的作用有:

$$(\xi, \eta)\in TM_{(q,p)} \Rightarrow (g^*\omega^1)((\xi,\eta)) = g^* p \cdot g_*\xi = p\cdot \xi = \omega^1((\xi,\eta))$$

其中倒数第二个等号事实上正是 \(g_*\) 之对偶的定义. 因此我们定义的由构型空间上微分同胚诱导得到的在余切丛上的作用是辛作用. 接下来为了方便起见我们仍称 \(T^*V\) 上这样定义的辛作用组成的李群为 \(G\).

考虑 \(G\) 的单参数子群 \(G_g = \{g^t = e^{t a}: t\in \mathbb{R}\}\), 其中 \(a\) 是其生成元. 按我们上面的分析它定义了一个 \(M\) 上的相流. 它对应的哈密顿函数事实上正是:

$$H_a(x) = \omega^1 \Big(\frac {\td } {\td t} g^t x \Big|_{t=0}\Big) \ ; \ x\in M$$

我们可以来检查这一点: 注意我们已经假设了使用标准坐标, 这使得 \(\omega^1 = p\td q\). 考虑上面定义的哈密顿函数在点 \(x\) 处之微分(注意 \(\omega^1\) 对 \(\td q\) 是线性的):

$$\begin{aligned}
\td H_a(x) &= p \td \Big( \frac {\td } {\td t} g^t q\Big|_{t=0}\Big) + \td p \cdot \Big(\frac {\td } {\td t} g^t q\Big|_{t=0}\Big) \\
&= p \cdot \Big(\frac {\td } {\td t}g_*^t \td q\Big|_{t=0}\Big) + \td p \cdot \Big(\frac {\td } {\td t} g^t q\Big|_{t=0}\Big) \\
&= \frac {\td } {\td t}(p\cdot g_*^t \td q) \Big|_{t=0} +\td p \cdot \Big(\frac {\td } {\td t} g^t q\Big|_{t=0}\Big) \\
&= \frac {\td } {\td t} (g^{*-t} p)\Big|_{t=0} \cdot \td q+ \td p \cdot \Big(\frac {\td } {\td t} g^t q\Big|_{t=0}\Big) \\
&= - \frac {\td } {\td t} (g^{*t} p)\Big|_{t=0} \cdot \td q+ \td p \cdot \Big(\frac {\td } {\td t} g^t q\Big|_{t=0}\Big) \\
\Rightarrow I\td H_a(x) &= (\frac {\td } {\td t} g^t q\Big|_{t=0}, \frac {\td } {\td t} (g^{*t} p)\Big|_{t=0}) = \frac {\td } {\td t} g^t x\Big|_{t=0}
\end{aligned}$$

即 \(H_a(x)\) 确为此相流的哈密顿函数. 证明中我们使用了 \(g^t\) 保微分形式 \(p\td q\) 的性质. 我们可以进一步看李群的李代数的交换子同哈密顿函数的泊松括弧的同态关系, 只需注意到生成元 \(a,b\) 的交换子生成的单参数子群事实上正是(设 \(\frac {\td } {\td t}\phi(e^{at} x)\Big|_{t=0}=(L_a\phi)(x)\)):

$$\begin{aligned}
H_{[a,b]}(x) &= \omega^1 \Big(\frac {\td } {\td t} e^{[a,b]t} x\Big|_{t=0}\Big) \\
&= \omega^1 \Big((L_aL_b-L_bL_a) x\Big) \\
&= p\cdot \frac {\td } {\td t} (e^{-bt})_* L_a e^{bt} x \Big|_{t=0} \\
&=\frac {\td } {\td t} (e^{bt})^* p \cdot L_a e^{bt}x \Big|_{t=0} \\
&= \frac {\td } { \td t} H_a(e^{bt}x) \Big|_{t=0} \\
&= (H_a,H_b)(x)
\end{aligned}$$

证明中我们使用了 \(e^{bt}\) 在辛流形上的作用保 \(\omega^1\)(第四个等号). 其中的第三个等号事实上是 Baker-Campbell-Hausdorff 公式的应用. 我们这里的证明说明了从构型空间上的微分同胚定义的在辛流形上的作用(辛化)总是泊松作用.

## 矩与诺特定理

群 \(G\) 在辛流形 \((M^{2n},\omega^2)\) 上的泊松作用事实上确定了从 \(M^{2n}\) 到 \(G\) 的李代数 \(\mathfrak{g}\) 的对偶空间 \(\mathfrak{g}^*\) 上的映射: 在 \(M^{2n}\) 上任一点 \(x\in M^{2n}\), \(G\) 的泊松作用为它的李代数的每个元素 \(a\in \mathfrak{g}\) 确定了一个线性依赖于它的哈密顿函数 \(H_a(x)\), 这个映射:

$$P : M^{2n} \rightarrow \mathfrak{g}^* \Rightarrow \forall x \in M^{2n}, a\in \mathfrak{g}, P(x): a \mapsto H_a(x)$$

关于矩的重要定理如下所述:

> 在矩映射 \(P\) 下, 连通李群的泊松作用变成 \(G\) 在其李代数之对偶空间 \(\mathfrak{g}^*\) 上的余伴随作用:
> $$\forall g \in G \Rightarrow \text{Ad}_{g^{-1}}^* = P\circ g \circ P^{-1}$$

以及系理:

> 若哈密顿函数 \(H: M^{2n}\rightarrow \mathbb{R}\) 在辛流形上的群 \(G\) 的泊松作用下不变, 那么这是矩 \(P\) 是以 \(H\) 为哈密顿函数的方程组的首次积分.

系理的成立是显然的, 由于给定李代数的元素 \(a\), 矩映射 \(P\) 在辛流形上各点的值正是李群泊松作用带来的哈密顿相流 \(H_a(x)\). 注意到李群保持哈密顿函数不变, 因此 \(H\) 同 \(H_a\) 总是可交换的, 换言之他们的泊松括弧总等于0. 从而 \(H_a\) 是运动方程的首次积分. 换言之, 矩映射 \(P\) 总是运动方程的首次积分.

诺特定理指出, 如果辛流形上的哈密顿函数 \(H: M\rightarrow \mathbb{R}\) 在一个由函数 \(F\) 作为哈密顿函数确定的相流下不变, 那么 \(F\) 是 \(H\) 所确定的典则运动方程的首次积分. 这里在矩映射下我们再次看到了诺特定理的表述. 事实上这个系理告诉我们, 只要找到了矩映射, 那么对所有使得哈密顿函数 \(H\) 不变的单参数子群(有李代数中的各个元素确定), 它们由诺特定理确定的首次积分正是这些李代数元素在辛流形上各点矩映射的值 \(P(M)\) 的像. 换言之, **矩映射的各个分量应当给出独立的首次积分**

这里我们使用矩映射的观点来重新讨论角动量守恒. 角动量守恒来自于空间转动不变性, 亦即泊松作用于辛流形 \(M\) 上的李群是三维正交群 \(SO(3)\) 的辛化, 记作 \(G\). 其中 \(M=T^* \mathbb{R}^3\). 考虑 \(G\) 中元素的作用, 在 \(M\) 的坐标分量上正是 \(SO(3)\) 中的转动 \(\bm{R}\), 而在动量分量上则是 \(\bm{R}^*\). 由于 \(M\) 的特别的结构, 事实上 \(G\) 中元素的作用正是:

$$SO(3)\ni \bm{R}\mapsto g \in G \Rightarrow \forall x = (\bm{q},\bm{p})\in M=T^*\mathbb{R}^3 , gx = (\bm{R}\bm{q},\bm{R}\bm{p})$$

因此 \(G\) 事实上同构于 \(SO(3)\). 它的李代数同样同构于 \(\mathfrak{so}(3)\), 其生成元的一组基的三维表示正是矩阵:

$$(\bm{J}_i)_{jk} = -\epsilon_{ijk}$$

相应于此生成元的单参数子群描述的是以 \(i=1,2,3\) 轴的角速度为 \(1\) 的转动:

$$\frac {\td} {\td t} g_i^tx \Big|_{t=0} = (\bm{e}_i\times \bm{q}, \bm{e}_i \times \bm{p}) = (\frac {\partial} {\partial \bm{p}}, - \frac {\partial} {\partial \bm{q}}) (\sum_{jk}\epsilon_{ijk} q^j p^k) \equiv I \td H_i(x)$$

即 \(H_i(x) = \sum_{jk} \epsilon_{ijk} q^j p^k\). 从而我们有矩映射:

$$\forall x = (\bm{q},\bm{p})\in T^*\mathbb{R}^3 \Rightarrow P(x) : \sum_{i=1}^3 a_i \bm{J}_i \mapsto \sum_{i=1}^3 a_i H_i(x)$$

矩映射的独立的三个分量对应了现在的三个独立的首次积分, 即:

$$H_1 = q^2p^3 - q^3 p^2 , H_2 = q^3p^1-q^1p^3 , H_3 = q^1 p^2 - q^2 p^1$$

正是角动量的三个分量式.

## 化约相空间的构造

在首次积分存在时, 相空间中系统的运动总是被约束在首次积分的等值集的交集上. 对这个问题的研究诞生了化约相空间的概念.

上面我们已经展示, 拥有对称性的力学系统的由对称性确定的首次积分将由矩映射确定. 因而在满足一定的条件时, 矩映射的等值集为一流形:

$$p \in \mathfrak{g}^*, M_p = \{x\in M: P(x) = p\}\subset M$$

而作用于 \(M\) 上的李群 \(G\) 拥有子群 \(G_p\) 使得 \(M_p\) 为其不变流形, 只需要 \(G_p\) 的元素的余伴随作用 \(\text{Ad}_{g^{-1}}^*\) 保持 \(p\) 不变, 则根据前面的关于矩映射的定理, 这些元素总是将 \(M_p\) 映为 \(M_p\).

在 \(G_p\) 的作用下, 我们可以将 \(M_p\) 的元素按照群作用定义等价关系:

$$\forall x ,y \in M_p, x\sim y \Leftrightarrow \exists g \in G_p , x = g y$$

按照这个等价关系我们可以将 \(M_p\) 分为若干等价类, 而化约相空间正是 \(M_p\) 按照这等价类作商得到的.

> 为使得这个求商的操作是有意义的, 我们需要额外引入一些假设. 如 Arnold 书中给出的一组假设:
> 1.  \(p\) 为正则值, 从而 \(M_p\) 为一流形.
> 2.  不变子群 \(G_p\) 是紧致的.
> 3.  \(G_p\) 的元素在 \(M_p\) 上的作用没有不动点.

我们将展示化约相空间拥有着自然的辛结构. 为此我们先来考虑化约相空间的一些特性.

记化约相空间为 \(F_p = M_p/\sim = \{S_x = G_p x : x \in M_p\}\). 不难看到, 按照这个定义我们事实上有一个映射: \(\pi: M_p\rightarrow F_p\). 它将 \(M_p\) 中的点映到它的等价类, 而它的微分则是 \(TM_p\) 到 \(TF_p\) 的投影: 直观理解可以想像 \(M_p\) 上一点 \(x\) 处的切矢量, 如果该切矢量同 \(G_p\) 确定的流相容那么这个切矢量在投影 \(\td \pi\) 的作用下应当为零. 只有那些不相容的切矢量, 即从 \(x\) 指向它附近的一个同它不等价的点的切矢量在 \(\td \pi\) 的作用下不为零. 而这些不为零切矢量投影事实上就组成了 \(F_p\) 的切空间. 在这样的切空间构造下我们有约化相空间 \(F_p\) 的切矢量的斜数量积的计算方式:

在同一点 \(f\in F_p\) 切于 \(F_p\) 的切矢量 \(\xi, \eta\) 的斜数量积的值的计算如下:

1.  找到 \(x\in M_p\) , 它的等价类为 \(f\).
2.  在 \(x\) 处的切空间 \(T(M_p)_x\) 中找到两个切矢量 \(\xi', \eta'\), 使得它们在投影 \(\td \pi\) 的作用下得到 \(\xi, \eta\).
3.  切矢量的 \(\xi, \eta\) 的斜数量积定义为:

    $$[\xi,\eta]_p = [\xi', \eta']$$

而让这个斜数量积成为 \(F_p\) 上的辛构造是由如下定理保证的:

> 上面定义的斜数量积即不依赖于代表点 \(x\) 的选择也不依赖于代表他们的切矢量 \(\xi',\eta'\in T(M_p)_x\) 的选择. 因此上面的斜数量积定义成为 \(F_p\) 上的辛构造.

我们简单证明这个定理:

先考虑同代表矢量 \(\xi',\eta'\) 的选择的无关性. 事实上, 如果要求 \(\xi',\eta'\) 在 \(\td \pi\) 下的投影给出确定的切矢量 \(\xi, \eta\), 那么它们的选择的自由度将仅在沿着 \(G_p\) 所确定的流这个方向. 换言之, 我们有:

$$\forall v \in T(G_p x)_x \Rightarrow \td \pi v = 0$$

从而如果 \(\xi' \in T(M_p)_x\) 而 \(\td \pi \xi' =\xi \in T(F_p)_f\). 那么对任意的 \(T(G_p x)_x\) 的点 \(v\), 我们有 \(\td \pi (\xi' + v ) = \xi\). 而且这样选择的 \(v\) 将是唯一的可能方法, 即如果 \(\xi', \xi''\) 在投影 \(\td \pi\) 下的像相同, 那么它们之间只能相差 \(T(G_p x)_x\) 中的元素. 由于定义, \(M_p= P^{-1}(p)\) 是矩的等值集, 因此 \(T(M_p)_x\) 的元素应当同由矩 \(P\) 的各个分量定义的首次积分作为哈密顿函数的流斜正交(方才能保证这些分量不变), 而 \(G_p\) 由矩映射诱导出的余伴随作用保持矩映射的值 \(p\) 不变, 从而 \(T(G_p x)_x\) 中的元素应当都是矩映射 \(P\) 不变的方向. 因此 \(T(M_p)_x\) 和 \(T(G_p x)_x\) 应当彼此斜正交. 换言之:

$$\forall v \in T(G_p)_x, \xi',\eta'\in T(M_p)_x \Rightarrow [\xi'+v,\eta'] = [\xi',\eta'] + [v,\eta'] = [\xi',\eta']$$

因此我们证明了, 上面定义的斜数量积 \([\cdot,\cdot]_p\) 同算法中找到的代表矢量的选择无关. 接下来证明它同代表点 \(x\) 无关. 我们事实上需要证明这个斜数量积在 \(G_p\) 流下不变. 而这由其辛作用以及 \(M_p\) 的不变性保证.

为了证明这个斜数量积为一辛构造, 我们还需要验证它的非退化性和封闭性. 如果 \([\cdot,\cdot]_p\) 是退化的, 那么必定有一非零元素 \(\xi\) 属于 \(T(F_p)\) 并使得一切 \(T(F_p)\) 中的元素同它斜正交. 按照上面讨论的代表矢量的自由度, \(\xi\) 应当有一个非零的代表矢量(否则 \(\xi\) 不可能非零) \(\xi'\), 它使得任意 \(T(M_p)\) 中的元素同它斜正交, 而这同 \([\cdot,\cdot]\) 非退化矛盾. 另一方面, 封闭性能够从它由 \(M\) 上的闭形式诱导出的关系看出. 综上, 我们证明了 \(F_p\) 上存在一个自然的辛构造.

## 一些力学系统的化约相空间

### 谐振子

一维系统的相空间是二维的, 设它有着哈密顿量:

$$H = \frac 1 2 (p^2+q^2)$$

保持 \(H\) 不变的李群的泊松作用事实上是二维平面的转动即 \(SO(2)\). 而此时的矩映射正是 \(H\) 本身(即相点距离原点的距离. 而它的等值集合(非零)为一系列同心圆周, 但每个等值集合在 \(SO(2)\) 下自成一个等价类, 从而商集只有一个元素. 这种退化的情况让化约相空间中只有一个点.

而如果考察 \(n\) 维谐振子, 等值集合为一族同心球面 \(S^{2n-1}\). 仍然选择子群 \(SO(2) = U(1)\), 那么化约相空间将不再为退化, 而是:

$$S^{2n-1} / U(1) = \mathbb{CP}^{n-1}$$

### 二维中心力场

二维中心力场系统有着 \(SO(2)\) 对称性, 对应的矩是角动量 \(M^3 = q^1p^2- q^2p^1\). 它的辛化为四维辛流形上的同时对 \(\bm{q}\) 和 \(\bm{p}\) 的二维转动.

此时矩的等值面为一组三维流形. 因此化约相空间的维数应当为 \(2\). 这意味着化约相空间上的动力系统维数比原始力学系统要更低.
