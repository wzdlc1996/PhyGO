# Problems in Chap. 06

## Young Tableau (Young 氏矩阵)

在一个 $m\times n$ 的 **Young Tableau (Young 氏矩阵)** 中, 每一行的数据都是从左到右排序的, 而每一列都是从上到下排序. 其中存在一些值为 $\infty$ 的项, 表示不存在的元素. 因此它可以用来存储 $r\leq mn$ 个有限的数. 

## a

给出一个包含元素 $\{9, 16, 3, 2, 4, 8, 5, 14, 12\}$ 的 $4\times 4$ 的 Young 氏矩阵.

为

$$
Y = \begin{bmatrix}
2 & 3 & 4 & 5 \\
8 & 9 & 12 & 14 \\
16 & \infty & \infty & \infty \\
\infty & \infty & \infty & \infty
\end{bmatrix}
$$

## b

对于一个 $m\times n$ 的 Young tableau, 证明如果 $T_{1,1} = \infty$ 则其为空, 如果 $T_{m,n} \lt \infty$ , 则其为满

如果 $T_{1,1} = \infty$, 由Young tableau的定义, $T_{i+1,j} \geq T_{i,j}, T_{i,j+1} \geq T_{i,j}$, 我们立即有 $T_{i\geq 1,j\geq 1} = \infty$, 从而其为空. 

对于 $T_{m,n} \lt \infty$, 基于类似的逻辑, 我们立即有 $T_{i\leq m, j\leq n} \lt \infty$, 从而为满

## c

给出一个在 $m\times n$ 的 Young tableau 上的时间复杂度为 $O(m+n)$ 的 `extractMin` 方法的实现. 

Young Tableau 的结构类似与最小堆, 但树中存在共用元素. 如上面的实现 `Y`, 而 `Y[i,j]` 的子结点就是 `Y[i+1, j]` 和 `Y[i, j+1]`. 可以看到, 每间隔一层, 就会有一个共用元素, 即 `Y[i+1, j+1]` 就是 `Y[i+1, j]` 的 "右节点" 同时也是 `Y[i, j+1]` 的 "左节点". 而 `Y[0, 0]` 则是其中的最小元素. 因此我们可以仿照 `maxHeapify` 来实现. 

注意到 Young Tableau 的矩阵实现 `T` 具有性质: `T[0,0]` 一定是矩阵中最小的元素. 因此我们要做的就是将 `T[0,0]` 置 `mn+1` (即数值实现上的无穷大量)并重构 Young tableau.　其实现在 `../Code/Chap_06/youngTab.py`. 在每次下沉元素都会降一层, 因此其时间复杂度为 $O(m+n)$, 为矩阵 `[0,0]` 到 `[-1,-1]` 的距离.

## d

设计一个 $O(m+n)$ 时间复杂度的 `insert` 方法

由于对称性, 一个 Young Tableau 事实上也是一个逆向排序后的矩阵. 因此类似 `extractMin` 中将 `[0,0]` 元素下沉, 我们插入时只需要将 `[-1, -1]` 元素赋值后上浮. 

## e

说明如何在 $O(n^3)$ 的时间内完成对 $n\times n$ 的 Young tableau 中元素的排序

重复调用 `extractMin`, 我们得到了一个排序算法. 该算法的时间复杂度正是

$$
O(n+n) \times n^2　＝　O(n^3)
$$

## f

设计一个 $O(m+n)$ 时间复杂度的算法, 判断一个元素是否是 Young tableau 中的元素.

其思想在于, 如果 `x != T[0,0]`, 那么判断其是否在其中只需要计算其是否在 `T[:,0]` 中, 花费 $O(m)$ 时间. 若不在, 则计算其是否在 `T[1:]` 中, 花费 $T_{m-1, n}$. 从而:

$$
T_{m,n} = O(m) + T_{m-1,n}
$$