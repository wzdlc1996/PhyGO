# Problems, at 22-04-13

其他问题同 `problems_01/` 中的相同. 额外添加如下一个博弈论问题


考虑A,B两个玩家, 以及 $L$ (面试中 $L=10$) 个红包, 其金额为 $x_i = 2^i \ ; \ i=0,\cdots,L-1$. 现在两人同时获得其中的两个红包且红包相邻, 但他们互相不知道对方的比自己更大还是更小. 此时两个玩家被允许 **同时** 给出决策交换或者不交换, 如果两个人都选择交换, 那么两人互换红包, 否则游戏结束

我们考虑这个博弈的Nash均衡. 一般的, 获得红包的结果有两种可能, 两个人的红包金额为 $E_1: x_A = x \ ; \ x_B = 2x$ 或者 $E_2: x_A = x \ ; \ x_B = x/2$. 以下我们分别讨论这两种情况. 考察两人提出换的概率分别为 $p_A(x_A), p_B(x_B)$. 那么各自的期望回报为:

$$
\begin{aligned}
\mathbb{E}(u_A|x_A=x) &= \sum_{x_B} \mathbb{P}(x_B| x_A=x) \Big(x_B p_A(x_A)p_B(x_B) + x (1 -p_A(x_A)p_B(x_B))\Big) \\
&= \Big(2 p_{A,0} p_{B,1} + 1 - p_{A,0} p_{B,1}\Big) \\
&\indent + \Big(2^{L-1} p_{A,L-1} p_{B,L-2} + 2^{L-2}(1 - p_{A,L-1} p_{B,L-2})\Big) \\
&\indent + \frac 1 2 \sum_{i=1}^{L-2} p_{A, i} \Big(p_{B,i-1} (2^{i-1}-2^i) + p_{B,i+1} (2^{i+1}-2^i)\Big) + 2^i
\end{aligned}
$$

从而:

$$
\begin{aligned}
p_{A}[p_B] &= \arg\max_{p_A} \mathbb{E}(u_A|x_A) \\
\Rightarrow & p_{A,i}[p_B] = \begin{cases}
1 & i = 0\textrm{ or } L-1 \\
1 &p_{B,i-1} (2^{i-1}-2^i) + p_{B,i+1} (2^{i+1}-2^i) \gt 0 \\
0 & p_{B,i-1} (2^{i-1}-2^i) + p_{B,i+1} (2^{i+1}-2^i) \leq 0 
\end{cases}\\
\Rightarrow & p_{A,i}[p_B] = \begin{cases}
1 & i = 0\textrm{ or } L-1 \\
1 & -p_{B,i-1} + 2p_{B,i+1} \gt 0 \\
0 & -p_{B,i-1} + 2p_{B,i+1} \leq 0 
\end{cases}
\end{aligned}
$$

注意到对称性, 这个解函数事实上无关于 $A$. 因而它只确定了关于 $p_B$ 的函数 $p: [0,1]^{\otimes L} \rightarrow [0,1]^{\otimes L}$. 而均衡解出现在满足方程:

$$
\begin{aligned}
p_A &= p[p_B] \\
p_B &= p[p_A]
\end{aligned}
$$

我们立即可以看到一个解: $p_{A,i} = p_{B,i} = 1$. 即两人一定会互换. 对于较小的 $L$, 我们可以通过穷举的办法来查找其他均衡解. 通过实验我们很容易看到事实上只有这一个均衡解.