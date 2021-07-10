# 红黑树

## 旋转

二叉搜索树中只有插入和删除节点可能导致红黑树的特性被破坏, 这一部分我们讨论如何重写它们. 其核心在于一种叫做 **旋转** 的操作. 

**旋转(rotation)** 是搜索树上的一种局部操作. 

1.  右旋 (right-rotate)

    对于一个拥有非空左子结点的节点可以定义右旋操作, 我们使用 (node -> (node.left, node.right)) 的形式来表示节点关系, 右旋操作如下改变这个部分:

    ```
    r -> y                                r -> x
    y -> (x, f3)        ---------->       x -> (f1, y)
    x -> (f1, f2)                         y -> (f2, f3)
    ```

2.  左旋 (left-rotate)

    左旋定义在拥有非空右子结点的节点上, 它事实上就是右旋的逆操作.

图示更加清晰:

![](./figs/right.png)
![](./figs/left.png)

(图片引用自博客 [@jianshujoker](https://www.jianshu.com/p/ab90c2ec07e4))

从而我们不难给出实现这些操作的代码, 注意这种局部操作只修改了存储节点关系的列表而不调整节点的值. 

```python{.line-numbers}
class bhTree(binSearchTree):
    # Other methods
    def rightRotate(self, x):
        if self.isEmpty(self.left(x)):
            print("Empty left child, leave tree unchanged")
            return
        
        y = self.left(x)
        p = self.par(x)

        # Modify the child of p into y
        if x == self.root:
            # discuss root separately, since p(root) = None
            self.root = y
        elif x == self.left(p):
            self.leftInd[p] = y
        else:
            self.rightInd[p] = y
        self.pInd[y] = p
        self.pInd[x] = y

        # Modify subtree belonging
        self.rightInd[y], self.leftInd[x] = x, self.rightInd[y]
```

## 插入节点

我们可以在 $O(\log n)$ 的时间内完成向一个含有 $n$ 个节点的红黑树中插入一个新的节点.

回忆在二叉搜索树中的插入操作, 我们通过按照搜索树进行搜索找到一个合适的叶节点位置, 然后将输入元素插入树中. 红黑树的插入操作将额外将该节点置红色, 然后调用一个修复红黑树性质的子程序来确保红黑树性质是保持的. 

_为什么不把新节点置黑色?_ : 如果将其置为黑色, 那么从其父节点开始向叶节点的不同简单路径上会拥有不同数量的黑色节点. 这将会破坏红黑树的性质5: "对每个节点, 从该节点到其所有后代叶节点的简单路径上, 均包含相同数目的黑色节点. ", 使得性质修复更加困难. 而如果置红色, 则性质5不会破坏而仅破坏性质4, 可以相对容易地进行修复(因为不需要增加或减少黑节点数量.)