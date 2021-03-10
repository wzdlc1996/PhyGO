# Exercise in Chap. 1.1

## 1.1

### Problem

设有集合 $A,B,C,D$, 满足 $A\cup B = C\cup D$, 证明:
1.  令 $A_1 = A\cap C, A_2 = A\cap D$, 则 $A=A_1\cup A_2$
2.  若 $A\cap C = \empty, B\cap D = \empty$, 则 $A=D, B=C$

### Proof

Let the universe be $U = A\cup B =C \cup D$

1.  首先我们证明 $A \subset A_1\cup A_2$. 为此, 考虑 $x\in A$, 由于 $A \cup B = C \cup D \Rightarrow A \subset C\cup D$. 从而 $x\in C \cup D$. 不失一般性令 $x\in C$. 则必有: $x \in C \wedge x\in A \rightarrow x\in A_1 =A\cap C$. 故我们有 $\forall x \in A: x \in A_1 \cup A_2 \Rightarrow A\subset A_1\cup A_2$.

    接下来我们证明 $A_1\cup A_2 \subset A$. 不失一般性考虑 $x\in A_1 = A\cap C$. 从而立即有 $x\in A$ 因为 $A_1 = A\cap C\subset A$. 从而我们有: $A_1\cup A_2 \subset A$.

    综上我们得到: $A_1\cup A_2 = A$

2.  由于 $A\cap C = \empty$, 基于 (1) 中的结论我们有: $A = \empty \cup (A\cap D) = A\cap D$. 因而立即给出 $A = D$. 从 $B \cap D =\empty \Rightarrow B \cap A = \empty$. 故:

    $$A\cup B = C\cup D \Rightarrow A\cup B = A\cup C \Rightarrow B\subset C$$

    我们证明 $C\subset B$. 为此考虑 $x\in C$, 由 $A\cap C =\empty$ 立即给出 $x\notin A=D$. 若 $x\notin B$, 那么我们立即有 $x \notin A\cup B$. 换言之 $x\notin C\cup D$, 这同 $x\in C$ 矛盾. 因此只能有 $x\in B$. 即有: $\forall x\in C: x\in B\Rightarrow C\subset B$

## 1.2

### Problem

设 $A,B,C \subset X$, 求证

$$B= (D\cap A)^C \cap (D^C\cup A)\Leftrightarrow B^C = D$$

### Proof

先来证明必要性:

考虑 $B^C = D$, 故:

$$
\begin{aligned}
(D\cap A)^C \cap (D^C\cup A) &= (B^C \cap A)^C \cap (B\cup A) \\
&= (B\cup A^C) \cap (B\cup A) \\
&= B
\end{aligned}
$$

接下来证明充分性:

$$
\begin{aligned}
B &= (D\cap A)^C \cap (D^C\cup A) \\
&= (D^C \cup A^C) \cap (D^C \cup A) \\
&=D^C
\end{aligned}
$$

这两个证明中使用了如下的性质:

$$
(B \cup A) \cap (B \cup A^C) = B
$$

我们这里做一些细致的讨论:

$$
\begin{aligned}
\forall x \in B : x \in B\cup A \wedge x\in B\cup A^C &\Rightarrow x \in (B\cup A) \cap (B \cup A^C) \\
&\Rightarrow B\subset (B\cup A) \cap (B \cup A^C) \\
\\
\forall x \in (B\cup A) \cap (B \cup A^C) & : x\in B\cup A \wedge x\in B\cup A^C \\
&\Rightarrow x \in B \\
&\textrm{ since }x \textrm{ cannot be in } A^C \textrm{ and } A \\
&\Rightarrow (B\cup A) \cap (B \cup A^C) \subset B 
\end{aligned}
$$

## 1.3

### Problem

设 $A, B$ 是集合, 定义 $A\Delta B = (A-B)\cup (B-A)$ 为二者的对称差. 证明它具有如下性质:

$$
\begin{aligned}
A\Delta B &= B\Delta A \\
A^C\Delta B^C &= A\Delta B \\
A\Delta(B\Delta C) &= (A\Delta B) \Delta C
\end{aligned}
$$

并证明给定集合 $A,B$, 存在唯一的集合 $E$ 使得 $E\Delta A = B$

### Proof

对称性很容易证明. 我们证明剩余两个性质, 以下记全集 $X \supset A, B$

由于

$$
\begin{aligned}
A^C - B^C &= \{x:x\in A^C \wedge x\notin B^C\} \\
&= \{x: x\in A^C \wedge x\in B\} \\
&= \{x: x\notin A \wedge x\in B\}\\
&= B- A
\end{aligned}
$$

故

$$
\begin{aligned}
A^C \Delta B^C &= (A^C- B^C) \cup (B^C - A^C) \\
&= (B- A)\cup (A-B) \\
&= A\Delta B
\end{aligned}
$$

对第三条性质, 由于:

$$
\begin{aligned}
A\Delta B &= (A- B)\cup (B-A) \\
&= (A\cap B^C)\cup (B\cap A^C) \\
&=((A\cap B^C) \cup B) \cap ((A\cap B^C )\cup A^C) \\
&=((A\cup B) \cap (B^C \cup B) ) \cap ( (A \cup A^C) \cap (B^C \cup A^C) ) \\
&= (A\cup B) \cap (A^C \cup B^C) \\
&= A\cup B - A\cap B
\end{aligned} 
$$

从而

$$
\begin{aligned}
A\Delta (B\Delta C) &= A\cup (B\Delta C) - A\cap (B\Delta C) \\
&= (A\cup B\cup C - A^C\cap B\cap C) - ((C^C \cap A\cap B) \cup (B^C \cap A \cap C) ) \\
&= A\cup B\cup C - (A^C \cap B\cap C) \cup (A\cap B^C \cap C) \cup (A\cap B \cap C^C)
\end{aligned}
$$

此对称形式确保了结合律的成立.

我们需要对第二个等号进行一些细致的讨论:

$$
\begin{aligned}
A\cup (B\Delta C) &= A\cup (B\cup C - B\cap C) \\
&= A\cup ((B\cup C)\cap (B\cap C)^C) \\
&= (A\cup B\cup C) \cap (A \cup (B\cap C)^C) \\
&= A\cup B\cup C - (A\cup (B\cap C)^C)^C \\
&=  A\cup B\cup C  - (A^C \cap (B\cap C))
\end{aligned}
$$

以及:

$$
\begin{aligned}
A \cap (B\Delta C) &= A\cap (B\cup C - B\cap C) \\
&= A\cap (B\cup C)\cap (B^C \cup C^C) \\
&= (A\cap (B\cup C)\cap B^C) \cup (A \cap (B\cup C) \cap C^C) \\
&= (A\cap B^C \cap C) \cup (A\cap B\cap C^C)
\end{aligned}
$$

其中我们使用了

$$(A\cup B) \cap A^C =( A\cap A^C) \cup (B\cap A^C) = B\cap A^C$$

的事实.

现在证明任意 $A,B$, 存在唯一集合 $E$ 使得 $E\Delta A = B$

首先证明存在性.

$$
\begin{aligned}
(A\Delta B)\Delta A &= B \Delta (A\Delta A) \\
&= B \Delta (A\cup A - A\cap A) \\
&= B\Delta \empty \\
&= B\cup \empty - B\cap \empty \\
&= B
\end{aligned}
$$

故只需令 $E=A\Delta B$

然后证明唯一性. 

由于:

$$(E\Delta A)\Delta B = B\Delta B = \empty\Rightarrow E\Delta (A\Delta B) = \empty$$

我们考察方程 $x\Delta A = \empty$. 由于:

$$\empty = x\Delta A = x \cup A - x\cap A$$

即 $x\cup A =\empty \vee x\cup A = x\cap A$. 有两种情况, 如果 $A=\empty$, 那么只能有唯一解 $x=\empty$. 否则只能有 $x\cup A = x\cap A$. 由于:

$$x\cap A \subset A \subset x\cup A \subset x\cap A$$

从而得到应当有 $x\cap A = x\cup A = A$. 故只能有 $x = A$. 得证.
