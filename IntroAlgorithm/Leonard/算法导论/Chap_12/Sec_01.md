# 二叉搜索树

## 基本概念

一个**二叉搜索树**由一个二叉树组织. 一种实现是通过链表, 每个节点除了值属性 `key` 外还有左右子结点 `left`, `right` 以及父节点 `p` 的位置. 而根节点则是树中唯一一个 `p` 为 `None` 的节点.

一个二叉搜索树中的键需要满足性质: 

如果 `x` 是二叉搜索树中的一个节点, 如果 `y` 是 `x` 左子树的节点, 那么 `y.key <= x.key`, 而如果 `y` 是右子树的节点, 那么 `y.key >= x.key`. 

这个性质不同于我们过去讨论的堆结构, 可以从中缀和前/后缀的角度来进行区分. 

二叉搜索树这样的特征, 使得它很容易进行 **中序遍历(inorder-tree-walk)** 来 **从小到大操作树中的元素**, 该遍历的递归方法可以这样进行:

```python{.line-numbers}
def inorderTreeWalk(x):
    if not isEmpty(x):
        inorderTreeWalk(left(x))
        # Some operation on x
        inorderTreeWalk(right(x))
```

我们使用了某种函数式的抽象, `left`, `right` 函数实现了上面的节点的寻找子结点的操作, 而 `isEmpty` 确定其是否为空(根节点的父节点). 类似的事实上可以通过调换3-5行的次序来实现 **前序遍历(preorder-tree-walk)** 和 **后序遍历(postorder-tree-walk)**, 但不具备从小到大的特性. 

_[Theorem]_: 如果 `x` 是一个有 `n` 个节点的二叉搜索树的根, 那么执行一次 `inorderTreeWalk(x)` 需要 $\Theta(n)$ 的时间

_[Proof]_: 执行一次由于需要遍历所有节点, 因此有 $T(n) = \Omega(n)$ ($T(n)$ 为执行所用时间). 考虑根的左子树有 $k$ 个节点, 那么右子树有 $n-k-1$ 个节点. 因此应当有

$$
T(n) = T(k) + T(n-k-1) + O(1)
$$

从空树 $T(0) = O(1)$, 我们可以进行归纳法证明, 不难看到

$$
T(n) \leq ck + c(n-k-1) + 2d + t = c n + (2d+t - c)
$$

因此只需递归假设 $2d+ t- c \leq d \Rightarrow d + t \leq c$, 那么证明即可得到. 

## 二叉搜索树的实现

在python中, 我们使用字典(散列表实现)来实现一个二叉搜索树. 我们用一个列表存储数据本身, 但封装去除它的顺序索引, 而用另外三个列表来存储各个节点的左子节点和右子节点以及父节点. 根节点的父节点设置为 `None`

```python{.line-numbers}
class binSearchTree:
    def __init__(self):
        self.body = []
        self.leftInd = []
        self.rightInd = []
        self.pInd = []
    
    def left(self, x):
        return self.leftInd[x]
    
    def right(self, x):
        return self.rightInd[x]

    def par(self, x):
        return self.pInd[x]

    def isEmpty(self, x):
        return x is None
```