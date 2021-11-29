# 音类集合和新黎曼理论(Neo-Riemannian Theory)

## 音类(Pitch class)集合

> 传统调性音乐尽管基于12平均律, 但事实上仍然以7音阶为主, 伴以半音升降. (三度叠置音程的功能性和弦)
> The preface of Harmonic Materials of Modern Music

**音类集合(pitch class set)**: 音类空间($\mathscr{PC}\sim \mathbb{Z}_{12}$)的子集, 简称 pc 集(pc set). 包含 $n$ 个音类的 pc集有时也被称作一个 n-和弦 (n-chord)

比如对应大三和弦的 $\{C,E,G\}$.

音类集合vs传统和弦: 音类集合的元素是音类, 而传统和弦由音级构成.

### 抽象层次

pitch: 乐音体系中的元素
pitch class: 乐音体系根据八度等价关系构成的等价类
pitch-class set: 音类的集合
set class: 音类集合按照移调和倒影变换群的轨道构成的等价类

pc集是无序集合, 为了方便标识, 通常根据紧凑原则规定pc集的标准序(normal order)

可以证明: 移调和倒影的复合会把 $\{C,E,G\}$ 变成12个小三和弦对应的pc集中的某一个.

换言之, 所有大三和弦和小三和弦组成的集合上, 群 (移调和倒影) 作用把该集合映为该集合.

等价关系: 群轨道. 定义所有音类集合的集合 $2^{\mathscr{PC}}$上的 等价关系为根据 群(移调和倒影) 的群轨道定义的等价:

$$
\forall x, y \in 2^{\mathscr{PC}} , x \sim y \Leftrightarrow \exist g \in G(T, I), x = g(y). 
$$

在该定义下, 24个大小三和弦是互相等价的.

**稳定化子(stabilizer)**: 给定集合元素, 群中保持其不变的子群成为其稳定化子.

群轨道的长度: $|G| / |G_\alpha|$ 群大小除以稳定化子群的大小.

### 音类集合表

按照一定方法在每个等价类中选择一个pc集作为代表, 就得到了 **音类集合表(the list of pitch-class sets)** 集合类代表的标准序成为该集合类的 **原型(prime form)**. 

如对于大小三和弦的原型为 $\{C, \flat E, G\}$

### 福特名称

艾伦·福特给每个集合类定义了名称, 形如 k-x 或者 k-xx, k是集合类中每个集合中包含的pc集的大小(移调和倒影都不会改变音类集合的大小.), x和xx表示序号

### 音类距离

对于任意两个音类, 它们之间的 **距离** 定义为音类圆周上从 X到 Y的最少音类数

$$
X, Y\in\mathbb{Z}_{12}\rightarrow d(X,Y) = \min(|Y-X|, 12 - |Y-X|)
$$

对于pc集, 可以为它定义一个距离向量:

$$
x\in 2^{\mathscr{PC}}\rightarrow \mathbb{R}^{6} \ni D(x)_i = |\{(X,Y)\in x\otimes x: X\neq Y, d(X,Y) = i\}|.
$$

即x中距离等于指标的不同对的对数. 距离向量是pc集的一个重要参数, 他给出了pc集中所有音类对之间的距离, 描述了一个pc集中全部的音程含量.

共同音定理:

$$
\forall x \in 2^{\mathscr{PC}}, D(x)_i = d_i \rightarrow |x \cap T^k x| = \begin{cases}
d_k & 1\leq k \leq 5 \\
2d_k & k = 6
\end{cases}
$$

补集的距离向量

$$
x \in 2^{\mathscr{PC}}\rightarrow D(x)_i = \begin{cases}
|x| - |x^C| + D(x^C)_i & 1\leq i \leq 5\\
\frac 1 2 (|x| - |x^C|) + D(x^C)_i & i = 6
\end{cases}
$$

### 全音程和弦

距离向量为 $(1,1,1,1,1,1)$ 的 n-和弦 称为 **全音程和弦**

pc集包含6种不同的距离对, 从而 $C_n^2 = 6 \Rightarrow n = 4$. 这种和弦并非传统和弦. 在(T, I) 作用下, 只有两类互不等价的全音程和弦. 命名为 4-Z29 和 4-Z15

## 音阶

从音类集合来看, **音阶** 也是一个pc集

-  5元pc集 $\sharp\{F,G,A,C,D\}$ 对应一个五声音阶
-  C自然大调音阶对应一个7元pc集, 它在音类圆周上存在一个对称轴, 因此 $(T,I)$ 不会产生新的自然大调音阶

**五度圆周**: 将音类按照五度音程排成圆周. (调关系: 在五度圆周上重合越多, 两个调的关系越近)

# 音乐变换理论