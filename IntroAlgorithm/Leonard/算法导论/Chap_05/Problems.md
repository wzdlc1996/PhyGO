# Problems in Chap. 05

## 概率计数

利用一个 $b$ 位的计数器(二进制), 通常最大数只能表示到 $2^b -1$. 我们接下来介绍 R. Morris 的一种概率计数法, 使得其可表示到更大的数值, 代价是一定精度损失. 

> 对 $i=0,1,\cdots, 2^b-1$, 令计数器值 $i$ 表示 $n_i$ 的计数, 其中 $n_i$ 构成了一个非负的递增序列. 假设计数器初值为 $0$, 表示计数 $n_0=0$. `increment` 计算单元工作在一个计数器上, 它以概率的方式包含值 $i$. 如果 $i=2^b-1$, 则它报告溢出错误. 否则, `increment` 以概率 $1/ (n_{i+1}-n_i)$ 把计数器增加 $1$, 而以概率 $1 - 1/(n_{i+1}-n_i)$ 保持其不变. 

对所有的 $i\geq 0$, 若选择 $n_i=i$, 则计数器就是一个普通的计数器. 但如果选择其他增加得更快的函数, 则会出现一些有趣的情形. 

### a

证明在执行 $n$ 次 `increment` 方法后, 计数器表示的数期望值正好是 $n$

考虑完成第 $k$ 次 `increment` 方法后, 计数器的值为 $X_i$. 不难看到 $\mathbb{P}(X_0=0) = 1$. 按照 `increment` 方法的规则, 我们有:

$$
X_{k+1} |_{X_k = i} = \begin{cases}
i+1 & \mathbb{P} = 1 / (n_{i+1} - n_i) \\
i & \mathbb{P} = 1- 1/(n_{i+1}-n_i)
\end{cases}
$$

从而, 我们有:

$$
\begin{aligned}
\mathbb{E}(X_{k+1}) &= \mathbb{E}_ i\Big(\mathbb{E}(X_{k+1} | X_k = i)\Big) \\
&= \mathbb{E}_i\Big(\frac {i+1} {n_{i+1}-n_i} + i(1 - \frac 1 {n_{i+1}-n_i})\Big) \\
&= \mathbb{E} \Big(\frac {1} {n_{X_k+1}-n_{X_k}} + X_k\Big)
\end{aligned}
$$

而其概率分布

$$
\begin{aligned}
\mathbb{P}(X_{k+1} = l) &= \sum_{s=0}^{\infty} \mathbb{P}(X_{k+1} = l|X_{k} = s)\mathbb{P}(X_k = s) \\
&= \frac {1} {n_{l} - n_{l-1}} \mathbb{P}(X_k = l-1) + (1-\frac 1 {n_{l+1} - n_{l}}) \mathbb{P}(X_k = l)
\end{aligned}
$$

考虑到计数事实上是计数器值的函数: $i\mapsto n_i$, 我们有:

$$
\begin{aligned}
\mathbb{E}(n_{X_{k+1}}) &= \mathbb{E}_i \Big(\frac {n_{i+1}} {n_{i+1}-n_i} + n_i(1 - \frac 1 {n_{i+1}-n_i})\Big) \\
&= \mathbb{E}_i\Big(n_i + 1\Big) \\
&= \mathbb{E}(n_{X_k}) + 1
\end{aligned}
$$

不难证得, $\mathbb{E}(n_{X_{k}}) = k$. 

### b

分析计数器表示的计数的方差依赖于 $n_i$ 序列. 考虑一个简单情形, 计算 $n_i=100i$ 的方差. 

不难有

$$
\begin{aligned}
\mathbb{E}(n_{X_{k+1}}^2) &= \mathbb{E}_i\Big(\frac {n_{i+1}^2} {n_{i+1} - n_i} + n_i^2 (1-\frac 1 {n_{i+1}-n_i})\Big) \\
&= \mathbb{E}(n_{X_k}^2) + \mathbb{E}(n_{X_{k}+1} + n_{X_k}) \\
&= \mathbb{E}(n_{X_k}^2) + k + \mathbb{E}(n_{X_k+1})
\end{aligned} \\
\Rightarrow
\textrm{Var} (n_{X_{k+1}}) = \mathbb{E}(n_{X_{k+1}}^2) - (\mathbb{E}(n_{X_{k+1}}))^2 =\textrm{Var} (n_{X_k}) + \mathbb{E}(n_{X_k+1}) - k -1
$$

从 $\mathbb{E} (n_0^2) = 0\Rightarrow \textrm{Var} (n_0^2) = 0$ 出发, 我们有

$$
\textrm{Var}(n_{X_k}) = \sum_{l=0}^{k-1} \mathbb{E}(n_{X_k+1}) - k - 1
$$

对于线性的 $n_i = ci$, 我们有: $\mathbb{E}(n_{X_k+1}) = \mathbb{E}(n_{X_k}+c) = k+c$, 从而有

$$
\textrm{Var} (n_{X_k}) = \sum_{l=0}^{k-1} c-1 = (c-1)k
$$

从而, 如果我们容忍一定的误差, 那么计数器计数增长可以显著慢于我们所要表示的数 ($n_i$ 随着 $i$ (计数器储存的值) 很快的情况). 

## 查找无序数组

考虑如下随机策略, 随机挑选 $A$ 中的一个下标 $i$, 如果 $A_i = x$, 则终止, 否则继续挑选下一个随机下标. 

### a

写出此过程的代码, 并且确保在 $A$ 中所有下标都被挑选过时, 算法终止

```python {.line-numbers}
def randomSearch(array: list, target: int) -> int:
    cap = 0
    while True:
        if cap == len(array):
            return -1
        index = randInt(0, len(arr_copy)) # Return a random integer in [0, len)
        if isinstance(array[index], int):
            if array[index] == target:
                return index
            else:
                array[index] = (target, 1)
                cap += 1
```

为了实现检查过所有元素就停止并且不使用复杂度为 $O(n)$ 的 `copy` 方法[python wiki/time complexity](https://wiki.python.org/moin/TimeComplexity), 我们选择修改传入列表的元素值. 我们假设了传入列表的元素为整数. 如果最终没有找到, 则方法会返回值 `-1`, 否则将返回对应的下标. 

### b

假设搜索目标存在于数组中, 计算 `randomSearch` 结束前必须挑选的数组下标的期望个数. 

换言之, 我们关心 `randomSearch` 中第3行开始的循环体的期望运行次数. 

考虑终止前循环的个数为随机变量 $X$, 数组长度为 $N$, 存在 $k$ 个符合条件的元素


1.  如果没有 4-5 和 7-12 行的终止机制
    那么我们有如下的递推关系(来自于每个循环之间都是独立随机产生下标.)

    $$
    \mathbb{P}(X= n+1) = \frac k {N} (1-\mathbb{P}(X=n)) \ ; \ \mathbb{P}(X = 1) = k/ N
    $$

    从而我们有 $\mathbb{P}(X= n) = kN^{-1} (1 - kN^{-1})^{n-1}$. 故期望运行次数:

    $$
    \mathbb{E}(X) = \sum_{n=1}^{\infty} \frac {nk} N (1- \frac k N)^{n-1} = \frac k N \Big(\frac {1-kN^{-1}} {(1-(1-kN^{-1}))^2}\Big) = \frac N k -1
    $$

2.  考虑该停止机制
    考虑在第 $n$ 个循环结束时, 变量 `cap` 的值为 $c_n$, 它代表已经被检查过的元素的个数. 从而:

    $$
    \begin{aligned}
    \mathbb{P}(X = n+1|c_n =N) &= 1\\
    \mathbb{P}(c_n = r+1| c_{n-1} = r) &= \max\{0, \frac {N-k-r}{N}\} \\
    \mathbb{P}(c_n=r| c_{n-1} = r) &= 1- \mathbb{P}(c_n=r+1|c_{n-1} =r) \\
    \mathbb{P}(c_0 = 0) = 1
    \end{aligned}
    $$

如果 $k=0$, 即原数组中不存在所找的元素. 则