# Exercise in Chap. 1.2

## 1.1

### Problem

设映射 $f:X\rightarrow Y, A\subset X, B\subset Y$. 判断下面等式的真性

1.  $f^{-1} (Y-B) = f^{-1}(Y) - f^{-1}(B)$
2.  $f(X-A) = f(X) - f(A)$

### Proof 

1.  有:

    $$
    \begin{aligned}
    f^{-1}(Y-B) &= \{x: f(x) \in Y \wedge f(x) \notin B\} \\
    &= \{x: f(x) \in Y\} - \{x: f(x)\in B\}\\
    &=f^{-1}(Y) - f^{-1}(B)
    \end{aligned}
    $$

2.  为否, 一个反例为: $f:x\rightarrow x^2$, $X=[-1,1], A=[-1,0]$, 而 $Y=[0,1], B=[0,1)$. 我们有:

    $$
    \begin{aligned}
    f(X-A) &= (0, 1] \\
    f(X) - f(A) &= [0,1] - [0,1] =\empty
    \end{aligned}
    $$

## 1.2

### Problem

设有集合 $A,B,C$, 证明:
1.  $A-B\sim B-A\Rightarrow A\sim B$
2.  $A\subset B \wedge A\sim A\cup C\Rightarrow B\sim B\cup C$

### Proof

1.  我们有
    
    $$
    \begin{aligned}
    A - B \sim B- A &\Rightarrow A- (A\cap B) \sim B - (A\cap B) \\
    &\Rightarrow (A-A\cap B )\cup (A\cap B) \sim (B - (A\cap B)) \cup (A\cap B) \\
    &\Rightarrow A\sim B
    \end{aligned}
    $$

    其中第二行的逻辑使用到两个不相交的等势集合的并也等势, 只需要注意到可以简单的组合两个双射的图.

2.  若 $B-A \cap C = \empty$, 则命题是平凡的. 因为此时 $B-A \cap (A\cup C) = \empty$, 只需要构造 $B-A$ 上的恒同映射然后同 $A\sim A\cup C$ 的取并即可. 因而如果我们解决了 $B-A \subset C$ 的情形, 那么一般的情形也就解决了. 因为我们总可以将 $B-(A\cup C)$ 的部分取恒同映射. 

    那么考虑 $B-A \subset C$ , 换言之我们有 $A\subset B \subset A\cup C$, 从而: $|A|\leq |B|\leq |A\cup C| = |A|$

    从而我们立即给出 $|A|=|B|\Rightarrow A\sim B$

## 1.3 

### Problem

证明:

$$(\limsup A_n)^C = \liminf A_n^C \ ; \ (\liminf A_n)^C = \limsup A_n^C$$

### Proof

证明可以使用我们在 Chap 1.1 中给出的集合上下极限的等价描述:

$$
\limsup A_n = \bigcap_{n=1}^{\infty}\bigcup_{l=n}^{\infty} A_l
$$

## 1.6

### Problem

如果:

$$A_{2n-1} = A, A_{2n } = B$$

计算序列集合的上下极限.

### Solution

$$
\begin{aligned}
\limsup A_n &= \bigcap_{n=1}^{\infty}\bigcup_{l=n}^{\infty} A_l\\
&=\bigcap_{n=1}^{\infty} A\cup B \\
&= A\cup B \\
\\
\liminf A_n &= \bigcup_{n=1}^{\infty} \bigcap_{l=n}^{\infty} A_l \\
&= A\cap B
\end{aligned}
$$

## 1.7

### Problem

证明:

$$
f: A\rightarrow B \textrm{ is surjection} \Leftrightarrow \forall E \subset B, f(f^{-1}(E)) = E
$$

### Proof

首先证明充分性. 

如果 $f$ 是满射, 那么: $\forall x \in B: \exist y \in A \rightarrow f(y) = x$ 从而: $\forall E\subset B$

$$
\begin{aligned}
f(f^{-1}(E)) &= f(\{x: f(x) \in E\} ) \\
&= f(\bigcup_{y\in E}\{x: f(x) =y\}) \\
&= \bigcup_{y\in E} f(\{x: f(x) = y\}) \\
&= \bigcup_{y\in E} \{y\}  \\
&= E
\end{aligned}
$$

然后证明必要性.

不妨设 $E=\{x\}$ 只含 $B$ 中的一个元素. 因而我们立即发现这样的集合的逆总是存在. 故 $f$ 是个满射

## 1.8 

### Problem

证明映射 $f:X\rightarrow Y$ 是双射的充分必要条件是 $f(X) = Y \wedge (\forall A, B \subset X: f(A\cap B) = f(A) \cap f(B))$

### Proof

首先证明必要性

由于 $f$ 是双射, 故必然有 (f 是满射) $f(X) = Y$. 而由于它同时是单射, $\forall A, B\subset X$

$$
\begin{aligned}
f(A) \cap f(B) &= \{x: x\in f(A) \wedge x\in f(B) \} \\
&= \{x: f^{-1}(x) \in A \wedge f^{-1}(x) \in B\} \\
&=\{x: f^{-1}(x) \in A\cap B\} \\
&= f(A\cap B)
\end{aligned}
$$

然后证明充分性.

首先由 $f(X) = Y$ 可以看到它一定是满射. 我们只需证明单射性质. 即证明 $\forall x\neq y \in X: f(x) \neq f(y)$. 

不妨假设存在相易元素 $x, y\in X,  x\neq y$. 则:

$$
f(\{x\})\cap f(\{y\}) = f(\{x , y\}) \neq f(\{x\}\cap \{y\}) = f(\empty)
$$

矛盾, 即证. 

## 1.10

### Problem

证明 $\mathbb{R}$ 上的任意不相交的开区间族是有限集或可列集

### Proof

考虑双射 $f(x) = \tan k x$ 能够使实数域同一个开区间等势. 因此 $\mathbb{R}$ 上的一个不交开区间族同 $(0,1)$ 上的一个不交开区间族等势. 我们考虑 $(0,1)$ 上的不交开区间族, 由于只需要证明无限的开区间族是可列的, 我们考虑满足这样条件的无限集开区间族 $A$

考虑 $A$ 中区间的左端点集合 $A_l$ 和右端点集合 $A_r$. 不难看到 $|A|=|A_l| = |A_r|, A = A_l\cup A_r$. 因而这两个集合也必然是无限集. 我们构造从 $A_l$ 到 $\mathbb{Z}$ 的双射. 令左端点到它对应区间的右端点的映射为 $i:A_l \rightarrow A_r$. 固定 $x_0\in A_l$, 规定

$$
\begin{aligned}
x_n &= \inf (A_l \cap [i(x_{n-1}),+\infty)), n\geq 1 \\
x_{n-1} &= \sup(A_l\cap (-\infty, i^{-1}(x_n)]) , n\leq 0
\end{aligned}
$$

从不相交条件我们能够证明, 任意给 $x_i, x_{i+1}$, 有 $(x_i,x_{i+1}) \cap A_l = \empty$ 因而我们构造了一个从 $\mathbb{Z}$ 到 $A_l$ 的满射: $x: \mathbb{Z}\ni z \mapsto x_z \in A_l$. 同样按照上面的定义可以看到它同样是个单射, 因为上面的递推公式是单调的. 因而即证



## 1.12

### Problem

设 $X$ 是一个无穷集合, $|X| = \alpha$, $B$ 是 $X$ 上的所有双射 $f:X\rightarrow X$ 的集合, 求 $|B|$

### Solution

我们来证明 $|B| = 2^\alpha$, 

首先所有双射的集合是所有映射集合的真子集, 从而:  $|B|\leq |X^X| = |X|^{|X|}$

我们也可以证明 $X$ 的幂集 $2^X \sim R \subset B$. 只需要注意到我们建立映射

$$S: B\ni f\mapsto \{x\in X: f(x)\neq x\}\in 2^X$$

显然我们有: $|B|\geq 2^{|X|}$. 因而我们有:

$$2^{|X|} \leq |B|\leq |X|^{|X|} = 2^{|X|}$$

这是无限集的性质, 可以这样考虑:

$$B \sim \{\{(x, f(x)) : x\in X\} : f \in B\} \subset 2^{X \times X} \sim 2^X$$

Thus $|B|\leq 2^{|X|}$

这个结论事实上等价于选择公理, 参考 [For every infinite $S$
, $|S|=|S\times S|$
implies the Axiom of choice](https://math.stackexchange.com/questions/56466/for-every-infinite-s-s-s-times-s-implies-the-axiom-of-choice)