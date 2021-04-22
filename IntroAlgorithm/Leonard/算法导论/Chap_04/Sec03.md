# 如何求解递归式

在本章的接下来的部分, 原书讨论了求解递归式的方法. 这部分的数学相对比较初等, 因此这里整合在一起并且加入一些对比和评论. 

## 代入法

代入法的核心思想是猜测解的形式, 并使用数学归纳法来进行证明或者猜出解中的某些参数从而得到解决. 比如如下的问题:

$$
T(n) = 2 T(n/2) + n
$$

我们可以猜测 $T(n)=O(n\log n)$, 然后进行如下推理, 假设 $T(m) = O(m\log m)$ 对所有 $m\lt n$ 成立, 那么:

$$
\begin{aligned}
T(n) &= 2T(n/2) + n \\
&= 2O(\frac n 2 \log (n/2)) + n \\
&= O(n \log n) + O(n) \\
&= O(n \log n)
\end{aligned}
$$

得证. 其边界条件 (如果这样取, $n\log n |_{n=1} = 0$), 可以通过略为修改定义为 $T(1) = O(1), T(n\gt 1) = O(n\log n)$ 实现. 

## 递归树方法

递归树方法的实质事实上就是反复应用递归式, 将其转化为某种求和来得到结论. 比如上个部分我们计算的矩阵乘法的分治法的递归方程.

## 主方法

主定理:

令 $a\geq 1, b\gt 1$ 是常数, 则递归式

$$
T(n) = a T(n/b) + f(n)
$$

的解有如下渐近界

1.  若 $\exists \epsilon\gt 0\rightarrow f(n)=O(n^{\log_b a-\epsilon})$ 那么 $T(n) = \Theta(n^{\log_b a})$
2.  若 $f(n) = \Theta(n^{\log_b a})$, 那么 $T(n) = \Theta(n^{\log_b a} \log n)$
3.  若 $\exists \epsilon\gt 0 \rightarrow f(n) = \Omega(n^{\log_b a + \epsilon})$, 且对某个常数 $c\lt 1$ 和所有足够大的 $n$ 有 $a f(n/b) \leq cf(n)$, 那么 $T(n) = \Theta(f(n))$

上面的结论可以推广到 $n/b$ 是向上取整或向下取整的情况. 