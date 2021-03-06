# 红黑树

二叉搜索树中的求最大/最小, 查找, 插入和删除操作均能够在 $O(h)$ 的时间内完成, 其中 $h$ 为树的高度. 但对于极端情况, $h$ 可能和 $n$ 拥有相当的数量级. 

我们现在讨论的红黑树是许多 "平衡" 搜索树中的一种, 能够保证在最坏情况下基本动态集合操作的时间复杂度在 $O(\log n)$.

## 红黑树的性质

红黑树是一个二叉搜索树, 其在每个节点上额外增加了一个存储位来表示节点的颜色, 可以是 `red` 或 `black`. 通过对任何一条从根到叶子的简单路径上各个节点的颜色进行约束, 红黑树确保没有一条路径会比其他路径长出二倍. 因此近似是**平衡**的. 

我们本次在 `python` 中如此实现红黑树, 它直接继承自我们在 Chapter 12 中实现的二叉搜索树. 我们额外添加一个标记颜色的布尔列表, 假对应红而真对应黑, 并重写涉及动态集合操作的方法, 来添加完成对 `color` 的操作. 

```python{.line-numbers}
class rbTree(binSearchTree):
    def __init__(self):
        super().__init__()
        self.colors = []

    def setValue(self, **kwargs):
        ptr = super().setValue(**kwargs)
        if "color" not in kwargs:
            col = True
        else:
            col = kwargs["color"]
        if ptr < self.size:
            self.colors[ptr] = col
        else:
            self.colors.append(col)

    def isBlack(self, x):
        return self.isEmpty(x) or x == self.root or self.colors[x]
```

一棵红黑树应当满足如下的性质:

1.  每个节点或者是红色的, 或者是黑色的. 
2.  根节点是黑色的.
3.  我们为每个原本的叶节点赋予两个空的子结点, 这样的每个叶节点是黑色的.
4.  如果一个节点是红色的, 那么它的两个子结点都是黑色的
5.  对每个节点, 从该节点到其所有后代叶节点的简单路径上, 均包含相同数目的黑色节点. 

为了实现性质2和3, 我们使用方法 `self.isBlack` 来判断其颜色. 其返回值的布尔操作能够满足我们的要求. 
为拥有性质5的红黑树, 我们可以定义 **黑高(black-height)** 的概念, 定义为从节点 $x$ 出发到叶节点的简单路径上的黑色节点个数 (不包含 $x$), 记作 $\textrm{bh}(x)$, 注意对于非叶节点的 $x$, 由于我们人为添加了黑色的空叶子, 因此 $\textrm{bh}(x) \geq 1$. 当满足性质5时, $\textrm{bh}(x)$ 应当和 **路径** 无关.

如下引理说明了为什么红黑树是一种好的搜索树

_[Lemma]_: 一个有 $n$ 个内部节点的红黑树高度至多为 $2\log_2(n+1)$. 

_[Proof]_: 我们证明任意节点 $x$ 为根的子树中都至少包含 $2^{\textrm{bh}(x)}-1$ 个内部节点. 为此使用归纳法. 如果 $x$ 是叶节点, 那么由于其确定的子树为空, 因此 $\textrm{bh}(x)= 0$, 同其包含 $0$ 个内部节点吻合. 

如果 $x$ 不是叶节点, 那么其确定子树的内部节点个数 $f(x)$ 应当满足:

$$
f(x) = 2 + f(x.left) + f(x.right) \geq 2 + 2^{\textrm{bh}(x.left)} - 1 + 2^{\textrm{bh}(x.right)} - 1.
$$

如果 $x$ 为红, 那么它的两个孩子颜色均为黑, 因此它孩子的黑高应当有:
$\textrm{bh}(x.left)=\textrm{bh}(x.right)=\textrm{bh}(x) - 1$, 因为性质5, 黑高和路径无关. 从这里推出

$$
f(x) \geq 2\times 2^{\textrm{bh}(x)-1} = 2^{\textrm{bh}(x)} \geq 2^{\textrm{bh}(x)}-1.
$$

而如果 $x$ 为黑, 那么其子结点黑高或者是 $\textrm{bh}(x)$ 或者比它少1. 而少1的情况我们已经看到满足命题, 因此不少1的情况自然也会满足. 从而我们考虑根节点, 根节点的内部节点个数正是 $n$, 它应当有:

$$
n \geq 2^{\textrm{bh}(\textrm{root})} - 1.
$$

由于根节点的黑高至少为树高度的一半(因为根据性质4, 不存在连续出现红色节点的情况, 从而黑高固定时, 最长的简单路径只能是它的两倍(根和叶都是黑色的)), 从而我们有:

$$
n \geq 2^{h/2} - 1 \Rightarrow h \leq 2\log_2(n+1).
$$

得证. 