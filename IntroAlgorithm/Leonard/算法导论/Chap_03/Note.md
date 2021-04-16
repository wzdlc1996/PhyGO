# 函数的增长

## 渐进记号

以下是一些常用渐进记号的定义

1.  **$\Theta$ 记号(渐进紧确界)**, 一个非负函数 $g(n)$ (下同)的 $\Theta$ 记号定义为:

    $$
    \Theta(g(n)) = \{f(n): \exists c_1,c_2,n_0\gt 0, \forall n \geq n_0 \rightarrow 0\leq c_1 g(n) \leq f(n) \leq c_2g(n)\}
    $$

2.  **$O$ 记号(渐进上界)**, 定义为

    $$
    O(g(n)) = \{f(n): \exists c, n_0\gt 0, \forall n \geq n_0\rightarrow 0\leq f(n) \leq c g(n)\}
    $$

3.  **$o$ 记号(非渐进紧确上界)**, 定义为

    $$
    o(g(n)) = \{f(n):  \forall c\gt 0, \exists n_0\gt 0 \rightarrow \forall n \geq n_0, 0\leq f(n)\lt cg(n) \}
    $$

4.  **$\omega$ 记号**, 定义为

    $$
    f(n) \in \omega(g(n)) \Leftrightarrow g(n)\in o(f(n))
    $$

4.  **$\Omega$ 记号(渐进下界)**, 定义为

    $$
    \Omega(g(n)) = \{f(n): \exists c, n_0\gt 0, \forall n \geq n_0\rightarrow 0\leq c g(n)\leq f(n) \}
    $$

