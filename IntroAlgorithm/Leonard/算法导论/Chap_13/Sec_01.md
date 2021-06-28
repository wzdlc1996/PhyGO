# 红黑树

二叉搜索树中的求最大/最小, 查找, 插入和删除操作均能够在 $O(h)$ 的时间内完成, 其中 $h$ 为树的高度. 但对于极端情况, $h$ 可能和 $n$ 拥有相当的数量级. 

我们现在讨论的红黑树是许多 "平衡" 搜索树中的一种, 能够保证在最坏情况下基本动态集合操作的时间复杂度在 $O(\log n)$.

## 红黑树的性质

红黑树是一个二叉搜索树, 其在每个节点上额外增加了一个存储位来表示节点的颜色, 可以是 `red` 或 `black`. 通过对任何一条从根到叶子的简单路径上各个节点的颜色进行约束, 红黑树确保没有一条路径会比其他路径长出二倍. 因此近似是**平衡**的. 

我们本次在 `python` 中如此实现红黑树, 它直接继承自我们在 Chapter 12 中实现的二叉搜索树. 我们额外添加一个标记颜色的布尔列表, 假对应红而真对应黑, 并重写涉及动态集合操作的方法, 来添加完成对 `color` 的操作. 

```python{.line-numbers}
class bhTree(binSearchTree):
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

    def insert(self, z):
        return super().insert(z)

    def delete(self, key):
        return super().delete(key)

    def isBlack(self, x):
        return isEmpty(x) or x == self.root or self.colors[x]
```

一棵红黑树应当满足如下的性质:

1.  每个节点或者是红色的, 或者是黑色的. 
2.  根节点是黑色的.
3.  我们为每个原本的叶节点赋予两个空的子结点, 这样的每个叶节点是黑色的.
4.  如果一个节点是红色的, 那么它的两个子结点都是黑色的
5.  对每个节点, 从该节点到其所有后代叶节点的简单路径上, 均包含相同数目的黑色节点. 

为了实现性质2和3, 我们使用方法 `self.isBlack` 来判断其颜色. 其返回值的布尔操作能够满足我们的要求. 