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
    -  excess risk 通常会用来考察通过优化empirical risk得到的$f_n$ 同理想的 $f$ 的差距, 并且给出bound. 即
       $$
       R_{excess} = R[f_n^*] - R^* \ ; \ f_n^* = \argmin_{f} \hat R[f]
       $$

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

在真实案例中, 我们无法给出 $\mathbb{P}(Y=1|X=x) = g(x)$, 而只能通过数据集样本给出一个它的估计. 并从这个估计按同样的规则给出 $f$ 的估计 $\hat f$. 能够证明 $f$和 $\hat f$ 的差距会被 $g$ 和 $\hat g$ 的差距控制. 

$$
\begin{aligned}
\indent &R[\hat f | X = x] - R[f^* | X =x] = \mathbb{P}(Y \neq \hat f(X)|X=x) - \mathbb{P}(Y \neq f(X) | X = x) \\
&= 1_{f(x) = 1} g(x) + 1_{f(x) = 0} (1-g(x)) - 1_{\hat f(x)  =1}  g(x) - 1_{\hat f(x) = 0}(1 -  g(x)) \\
&= 1_{f(x)=1}(g(x) - \hat g(x)) + 1_{f(x) = 0} (\hat g(x) - g(x)) + 1_{\hat f(x) = 1}(\hat g(x) - g(x)) + 1_{\hat f(x) = 0} ( g(x) -\hat g(x)) \\
&\indent + 1_{f(x) = 1} \hat g(x) + 1_{f(x) = 0}(1-\hat g(x)) - 1_{\hat f(x) = 1} \hat g(x) - 1_{\hat f(x) = 0} (1 - \hat g(x)) \\
&\leq 2 |g(x) - \hat g(x)| + \max \{\hat g(x), 1-\hat g(x)\}
\end{aligned}
$$

## 困难

找到函数 $f$ 是困难的:
1.  形式可能很复杂: 神经网络原则上能够拟合任何非线性函数
2.  数据量很少, empirical risk的估计很差
3.  Curse of Dimensionality: 在分类问题上, 维数越高可能会带来更好的性能
    -  核心思想: 把curse变成bless of dimensionality
4.  潜在假设: 训练数据和测试数据是同源的. 如果失去该假设将会更加困难
5.  The craterion. 度量准则很难选择

# 一致性

算法 $\mathcal{A}$ 将一组数据集 (随机变量的一组样本) 映为一个 predictor. 算法的一致性就是指它应当无关分布地在risk上逼近最优. (consistent in expectation). 数学地讲

$$
\textrm{Algorithm}: \mathcal{A}: D_n \mapsto f_n = \mathcal{A}(D_n) \\
\mathbb{E}\Big(R[\mathcal{A}(D_n)] \Big) - R^* \rightarrow_{n\rightarrow \infty} 0
$$

在 $\mathbb{E}\Big(R[\mathcal{A}(D_n)] \Big) - R^*$ 随 $n$ 收敛的不同行为上我们也可以定义区分强弱的 consistency, 比如著名的 **PAC(Probably approximately correct) learning** 就是指这种差距依概率收敛:

$$
\mathbb{P}\Big(R[\mathcal{A}(D_n)] - R^* \leq \epsilon \Big) \geq 1 - \delta
$$

PAC consistency 代表着对任意 $\epsilon\gt 0$ 满足上面不等式的 $\delta_n$  将会随着 $n\rightarrow \infty$ 趋于0

# 收敛率

**minimax risk**. 考虑数据源的所有可能分布$\mathcal{P}$, 这样 minimax risk 是指excess risk对分布的上界对算法的下界:

$$
\textrm{minimax risk} = \inf_{\mathcal{A}} \sup_{p \in \mathcal{P}} \mathbb{E}\Big(R_p (\mathcal{A} (D_{n,p}))\Big) - R_p^*
$$

# 寻找Predictor的方法

## 线性回归

为什么讨论线性回归:
1.  足够简单, 但覆盖了learning theory的绝大部分. 比如bias-variance trade-off
2.  使用非线性方法(如kernel method)可以推广到非线性预测

linear regression 是一个参数化方法, 它的预测器为

$$
f(x;\theta) = \phi(x)^T \theta
$$

其中向量 $\phi(x) \in\mathbb{R}^d$ 通常被称为 **feature vector**. 通常的algorithm使用带有regularization的最小二乘法

$$
R[f] \equiv R(\theta) = \frac 1 n \sum_i (y_i - f(x_i;\theta))^2 + \lambda \Omega(\theta)
$$

如L2-reg (rigid regression) $\Omega(\theta) = \|\theta\|^2$

## k-NN

# Curse of Dimensionality

考虑 $X_1,\cdots, X_n$ iid 的 $\mathbb{R}^d$ 随机向量, 均匀分布于 $[0,1]^d$

考虑范数

$$
D= \mathbb{E} \min_{i=1,\cdots,n} \|X - X_i\|_{\infty}
$$

其中 $\|x\|_{\infty} = \max_{l=1,\cdots, d} |x^l|$

$$
\begin{aligned}
D &= \int_0^{\infty} \td t\  \mathbb{P}(\min_i \|X - X_i\|_{\infty} \geq t) \\
&= \int_0^{\infty} \td t\ 1 -  \mathbb{P}(\min_i \|X - X_i\|_{\infty} \lt t) \\
&\geq \int_0^{s} \td t\ 1 -  n (2t)^d \lt t) \\
&\sim \frac d {1+d} \frac 1 {n^{1/d}}
\end{aligned}
$$

其中 $s$ 使得被积函数为正. 

当 $d$ 很大时, $D$ 将总会很大, 从而使得在高维空间中找到合理的临近点估计是困难的

# Bias-Variance Trade-off

考虑 $g_n$ 为一个估计, 那么

$$
\begin{aligned}
\mathbb{E}(|g_n - g|^2) &= \mathbb{E}(|g_n - \mathbb{E} g_n|^2) + \mathbb{E}(|\mathbb{E} g_n - g|^2)
\end{aligned}
$$

可以看到第一项是 $g_n$ 的方差, 第二项则是它的bias. 交叉项为零可以通过条件期望证明, 注意 $g_n$ 是依赖于数据样本的. 

$$
\mathbb{E}(g_n - \mathbb{E}g_n)(\mathbb{E}g_n - g) = \mathbb{E}\Big(\mathbb{E}\Big((g_n - \mathbb{E}g_n)(\mathbb{E}g_n - g)| \textrm{sample}\Big)\Big) = 0
$$

# No Free Lunch

考虑 0-1 分类问题, $\mathcal{P}$ 为 $X\otimes \{0, 1\}$ 上的所有概率分布, 那么对于固定的 $n$ 和algorithm $\mathcal{A}$ , 有

$$
\sup_\mathcal{P} \mathbb{E}\Big(R[\mathcal{A}(D_n)] \Big) -R^* \geq 1/2
$$

该定理的意义在于: 找不到一个算法让所有分布都能获得最好表现 (excess risk 为0)

证明: 核心在于构造一个满足不等式的分布 $\mathcal{P}$

考虑 $x \in X = \{1,\cdots,k\}$ ($k\gg n$) 是一个离散的, 均匀分布的变量. $p_i = \mathbb{P}(x = i) = 1/k$. 而数据集服从分布 $(x, y) \in X \otimes \{0, 1\}$ 被一个向量 $b = (b_1,\cdots, b_k), b_i \in\{0, 1\}$ 参数化:

$$
y = b_x
$$

此时, 最优的分类器带来的risk应为 $R^* = 0$. (因为x, y之间存在一个一一对应关系).

令 $S_n(b) = \mathbb{E} (R[\hat f_n])$, 我们来考虑 $\sup_b S_n(b)$, 找到这个最大值界的技巧: 随机化 $b$ 从而给出 $\sup_b S(b) \geq \mathbb{E}_b S(b)$ :

$$
\begin{aligned}
\mathbb{E}_b S(b) &= \mathbb{P}_{b\sim B}(\hat f_n(X) \neq B_X) \\
&= \mathbb{E}_{x_1,\cdots,x_n}\Big(\mathbb{P}(\hat f_n(x) \neq B_x|x_1,\cdots, x_n)\Big) \\
&\geq \mathbb{E}\Big(\mathbb{P}(\hat f_n(x) \notin B_x \wedge x \neq \{x_1,\cdots,x_n\}|x_1,\cdots, x_n)\Big) \\
&= \mathbb{E}\Big(\frac 1 2 \mathbb{P}(x\notin \{x_1,\cdots,x_n\}|x_1,\cdots,x_n)\Big) \\
&= \frac 1 2 \mathbb{P}(x\notin \{x_1,\cdots,x_n\})
\end{aligned}
$$

其中由于 $\mathbb{P}(\hat f_n(x) \neq b_x|x\notin\{x_1,\cdots,x_n\}, x_1,\cdots,x_n) = 1/2$, 这是因为 label 均匀分布在0,1之间, 而数据 $x$ 没有被观察到过. 我们要求 $b$ 的各个分量服从 Bernoulli 分布. 进而

$$
\frac 1 2\mathbb{P}(x\notin \{x_1,\cdots,x_n\}) = \frac 1 2 \mathbb{E}_x (\mathbb{P}(x_1 \neq x, x_2\neq x, \cdots, x_n\neq x| x)) \\
= \frac 1 2 \mathbb{E}_x (\prod_{i=1}^n\mathbb{P}(x_i \neq x| x)) = \frac 1 2 (1-1/k)^n
$$

从而对于给定 $n$, 我们令 $k\rightarrow \infty$ 即可.

推广:

对任意的递降序列 $a_n$ 收敛到0, 满足 $a_0 \leq 1/ 16$, 那么对任意一个algorithm, 存在一个分布使得

$$
\mathbb{E}(R_p [\mathcal{A}(D_n)]) - R^* \geq a_n
$$