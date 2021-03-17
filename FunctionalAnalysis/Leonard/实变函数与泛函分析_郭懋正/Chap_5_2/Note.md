# Note for Chap. 5.2

Hilbert 空间被定义为:

考虑$\mathbb{K}\in \{\mathbb{R},\mathbb{C}\}$ 上的线性空间 $X$, 且装备有内积 $(\cdot,\cdot): X\times X\rightarrow \mathbb{K}$, 使得
1.  $(ax+by,z) = a(x,z) + b(y,z)$
2.  $(z, ax+by) = a^*(z,x) + b^ *(z,y)$
3.  $(x,x)\geq 0, (x,x)=0\Leftrightarrow x=0$
4.  $(x,y) = (y,x)^*$

如果通过内积定义的距离 $\rho(x, y) = \|x-y\|\equiv (x-y,x-y)$ 使得 $(X,\rho)$ 是一个 **完备度量空间**, 那么就称此空间为一个 **Hilbert 空间**