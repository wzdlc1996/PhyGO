# Introduction

机器学习的三个层面

1.  应用: cv, nlp, ml for science
2.  算法: 传统统计方法(Leo Bremian), 现代统计方法(深度学习(表示), 强化学习, 因果学习)
3.  理论: 理论计算机, 理论统计 -> 计算机科学, 统计, 人工智能, 数据科学.

机器学习: 统计+优化 
textbook: 
1.  Bishop, Murphy
2.  The Elements of Statistical Learning, 
3.  All of Statistics
4.  Understanding Machine Learning
5.  Foundations of Machine Learning
6.  Computer Age Statistical Inference
7.  Learning Theory from First Principle (*) Francis Bach

# 基本问题

**有监督学习场景** 

其数据集为 $\{(x, y): x \in \mathbb{R}^d\} = X \otimes Y$, 其中 $x$ 一般称为 **input(feature, covariants)**, 通常 $y\in \mathbb{R}$(regression) 或 $y\in\{0, 1\}$(classification). 被称为 **output(labels, response)**. We will use $X, Y$ to denote the random variable and the set without confusion.

学习目标为找到一个映射 $f: X \rightarrow Y$, 为此需要定义一个关于实际output和预测的loss function: 
1.  $p$-norm loss for regression: $l(y, \hat y) =|y - \hat y|^p$
2.  cross entropy loss for classification.

在总体数据上, 我们需要优化的就是关于 $f$ 的泛函 
1.  **Expected risk**: $R[f] = \mathbb{E} l(y, \hat y)$.  
2.  **Empirial risk**: $\hat R[f] = \frac 1 n \sum_{i=1}^n l(y_i, f(x_i))$
3.  **Excess risk**: $R[f] - R^*$ where $R^* =\mathbb{E}_x\Big(\inf_{z\in Y} \mathbb{E}(l(y, z)|x)\Big)$ is the **Bayes risk**. It is the risk of Bayes predictor which minimizes expected risk: $f^*(x') \in \argmin_{z\in Y} \mathbb{E}(l(y,z)|x=x')$. It is not dependent of $f$, thus would not affect the optimization in practice.

_[Theorem]_: The expected risk satisfies
$$
R(f) = \mathbb{E}_x(R(f|X)) = \int R(f|X = x) \mu(dx)
$$
where $R(f|x) = \mathbb{E}(l(y, f(x)) | X = x)$. Let $\tilde{f}$ be the value of $f$ that minimizes conditional risk, i.e.,  
$$
\tilde{f}(x) = \argmin_f R(f|x)
$$
Then $\tilde{f}$ is a Bayes predictor.

_[Lemma]_: (from advanced probability textbook)
$$
R(f_n^*) - R(f^*) \leq 2 \sup_f |R_n(f) - R(f)|
$$

where $f_n^* =\argmin_f R_n(f)$

## Examples

### regression with l2 risk

The loss function is $l(y, z) = (y - z)^2$. 我们来验证 $g(x) = \mathbb{E}(Y|X = x)$ 正是使得expected risk最小的函数. 我们有

$$
\begin{aligned}
\mathbb{E} (Y - f(X))^2 &= \mathbb{E}\Big(Y - g(X) + g(X) - f(X)\Big)^2 \\
& = \mathbb{E}(Y - g(X))^2 + \mathbb{E}(g(X) - f(X))^2 + \mathbb{E}(Y-g(X))(g(X)-f(X)) \\
\end{aligned}
$$

其中第三项可以写为

$$
\begin{aligned}
\mathbb{E}(Y-g(X))(g(X)-f(X)) &=\mathbb{E}\Big\{\mathbb{E}\Big((Y-g(X))(g(X)-f(X)) |X\Big)\Big\} \\
&= \mathbb{E}\Big\{(g(X)-f(X))\mathbb{E}\Big((Y-g(X)) |X\Big) = 0
\end{aligned}
$$

我们使用了 $\mathbb{E}(Y-g(X)|X) = \mathbb{E}(Y|X) - g(X) = 0$. 因而, 从

$$
\begin{aligned}
\mathbb{E} (Y - f(X))^2 
& = \mathbb{E}(Y - g(X))^2 + \mathbb{E}(g(X) - f(X))^2 \\
\end{aligned}
$$

我们立即给出其取最小值应当有 $f^* =g$

### Binary classification with 0/1 loss

分类问题 $Y \in \{0, 1\}$, loss function $l(y,z) = 1_{y\neq z}$. 此时 expected risk 为

$$
\mathbb{E} l(Y, f(X)) = \mathbb{P}(Y\neq f(X))
$$

我们可以证明此时的 Bayes predictor 有如下构造

$$
f^*(x) = \begin{cases}
1 & \mathbb{P}(Y = 1|X = x) \gt 1/2 \\
0 & \mathbb{P}(Y = 1|X = x) \lt 1/2 
\end{cases}
$$

其证明如下:

我们看到这样的 $f^*$ 下有
$$
\begin{aligned}
\mathbb{P}(Y\neq f^*(x)|X = x) &= \begin{cases}
\mathbb{P}(Y\neq 1|X = x) & \mathbb{P}(Y = 1|X=x)\gt 1/ 2 \\
\mathbb{P}(Y\neq 0|X=x) & \mathbb{P}(Y=1|X=x)\lt 1/2
\end{cases} \\
&= \min\{\mathbb{P}(Y=1|X=x) , 1 - \mathbb{P}(Y=1|X=x)\}
\end{aligned}
$$

从而我们有

$$
\begin{aligned}
& \mathbb{P}(Y\neq f(X)|X= x) - \mathbb{P}(Y \neq f^*(X) | X=x) \\
=& 1 - \mathbb{P}(Y = f(x) | X = x) - \mathbb{P}(Y\neq f^*(x) | X= x) \\
=& \max \{\mathbb{P}(Y=1|X=x) , \mathbb{P}(Y=0|X=x)\} - \mathbb{P}(Y = f(x) | X = x) \\
\geq& 0
\end{aligned}
$$

从而:

$$
\begin{aligned}
&\mathbb{P}(Y\neq f(X))  -\mathbb{P}(Y\neq f^*(X)) \\
&= \mathbb{E}\Big(\mathbb{P}(Y\neq f(X)|X= x) - \mathbb{P}(Y \neq f^*(X) | X=x)\Big) \geq 0
\end{aligned}
$$

即证.