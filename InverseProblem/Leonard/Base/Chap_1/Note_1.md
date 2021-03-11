# Note 

## Introduction

_[Definition]_: Essential concepts

1.  $X$: 输入元素所在的空间
2.  $Y$: 输出元素所在的空间
3.  $K(\cdot, p)$: 含参数 $p$ 的算子(系统)
4.  $P$: 参数空间

问题的分类如下:

1.  **正问题(forward problem)**: 已知 $p\in P$, 对 $x\in X$ 计算输出 $y=K(x, p) \in Y$
2.  **反问题(inverse problem)**: 已知 $p\in P, y\in Y$, 找到 $x\in X$ 使得 $y= K(x,p)$ 成立
3.  **系统辨识(system identification)**: 已知 $x\in X, y\in Y$, 找到 $p\in P$ 使得 $y=K(x,p)$ 成立.