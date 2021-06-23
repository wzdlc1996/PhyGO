# Exercise in Chap. 5.3

## 6

### Problem

设 $(\alpha_{ij})_{i,j=1}^\infty$ 是无穷矩阵, $\alpha_{ij} \geq 0$. 且存在 $\beta,\gamma \gt 0, p_i\gt 0$ 使得

$$
\sum_{i=1}^\infty \alpha_{ij} p_i \leq \beta p_j \  ; \ \sum_{j=1}^\infty \alpha_{ij} p_j \leq \gamma p_i.
$$

证明存在 $l^2(\mathbb{N})$ 上的算子 $A$. 使得 $(A e_j, e_i) = \alpha_{ij}$, 并且 $\|A\|^2 \leq \beta \gamma$

### Solution

$A$ 的构造显然由矩阵 $\alpha_{ij}$ 即可得到, 我们需要证明的就是它把 $l^2(\mathbb{N})$ 的元素同样映为其中的元素. 为此, 我们有:

$$
(A x, e_j) = \sum_{i=1}^\infty (A (x,e_i)e_i, e_j) = \sum_{i=1}^\infty (x,e_i)^* \alpha_{ij}. 
$$

从而有

$$
\|A x\|^2 = \sum_j |\sum_{i} (x,e_i)^* \alpha_{ij}|^2\leq \sum_{ij} |(x,e_i)|^2 |\alpha_{ij}|^2 = \sum_j 
$$