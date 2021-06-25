# 二叉搜索树

## 插入和删除

对二叉搜索树的插入和删除操作需要同时保持二叉搜索树的性质. 

### 插入元素

要将一个新值 $v$ 插入到一个二叉搜索树 $T$ 中的过程称为 `insert`. 其实现为

```python{.line-numbers}
class binSearchTree:
    # Other methods
    def setValue(self, ptr, *args):
        k, v, l, r, p = args
        if ptr in range(self.size):
            self.rightInd[ptr] = r
            self.leftInd[ptr] = l
            self.pInd[ptr] = p
            self.key[ptr] = k
            self.val[ptr] = v
            return ptr
        else:
            self.rightInd.append(r)
            self.leftInd.append(l)
            self.pInd.append(p)
            self.key.append(k)
            self.val.append(v)
            self.size += 1
            return self.size - 1


    def insert(self, z):
        key, val = z
        y = x = self.getRoot()
        while not self.isEmpty(x):
            y = x
            if key < self.key[x]:
                x = self.left(x)
            else:
                x = self.right(x)
        if y is None:
            self.root = 0

        ptr = self.setValue(-1, key, val, None, None, y)
        if key < self.key[y]:
            self.leftInd[y] = ptr
        else:
            self.rightInd[y] = ptr
```

我们使用方法 `setValue` 来方便地为动态集合中修改值或添加值, 但它并不能保证插入不会改变二叉搜索树的特性.

为了理解 `insert` 方法, 我们需要证明一个定理:

_[Theorem]_: 对于不存在 `key` 冲突的情况, 即 `key` 两两不同, 插入操作只需要将新的元素添加为原树的叶子即可确保二叉搜索树的性质得到满足. 

该定理的证明不难通过中序遍历二叉搜索树 $T$ 会将 `key` 按照从小到大顺序排列的特性得到. 我们考虑插入元素携带 `key` 为 $k$, 而原树的 `key` 列表为 $T.key$. 我们假设 $T.key$ 中值在 $k$ 两边的为 $k_1\lt k \lt k_2$. 因为 `T.key` 中的元素两两不同, 因此这里为严格不等号, 而且 $k_1, k_2$ 在 $T.key$ 是相邻的.

由于 $k_1\lt k_2$, 根据二叉搜索树的性质, $k_1$ 应当在 $k_2$ 节点的左子树中. 我们能够确定 $k_1$ 不存在右子树, 因为如果它存在, 那么其中必然存在节点 $k_2\gt k' \gt k_1$, 这同 $k_1, k_2$ 是 $T.key$ 中对 $k$ 的紧的界矛盾. 

因此插入操作只需将 $k$ 放置在 $k_1$ 的右子节点作为二叉搜索树的叶子, 即可保证二叉搜索树的性质. 

有了这个定理, 我们就能理解 `insert` 的工作原理. 

25-30行中, 我们使用类似 `treeDive` 的方式查询符合定理要求的 $k_1, k_2$. 变量 `y` 总是 `x` 的父节点. 如果31行的判断成立, 这就意味着原本的树是空的. 因此触发了对 `self.root` 的重新赋值.

34行调用 `self.setValue`, 为树加入一个节点, 以第一个参数 `-1` 保证会增长树的尺寸, 子结点用 `None` 来确定它是一个叶子节点, 其父节点为 `y`. 35-38行, 通过判断 `key` 和 `y.key`, 来确定插入节点该在 `y` 左还是右. 