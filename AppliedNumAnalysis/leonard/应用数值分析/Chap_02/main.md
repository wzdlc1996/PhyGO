# 单变量求导

对于单变量函数 $f(x)$, 我们使用Taylor展开

$$
f(x+\Delta x) = f(x) + f'(x) \Delta x + \frac 1 2 f''(x) \Delta x^2 + \mathcal{O}(\Delta x^3)
$$

这给出了对其导数的带有一阶误差的表达式:

$$
f'(x) = \frac {f(x+\Delta x) - f(x)} {\Delta x} + \mathcal{O}(\Delta x)
$$