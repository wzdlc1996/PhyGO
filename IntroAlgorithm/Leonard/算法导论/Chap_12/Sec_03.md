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

        ptr = self.setValue(-1, key, val, None, None, y)
        if y is None:
            self.root = 0
        else:
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

25-30行中, 我们使用类似 `treeDive` 的方式查询符合定理要求的 $k_1, k_2$. 变量 `y` 总是 `x` 的父节点. 

32行调用 `self.setValue`, 为树加入一个节点, 以第一个参数 `-1` 保证会增长树的尺寸, 子结点用 `None` 来确定它是一个叶子节点, 其父节点为 `y`. 如果31行的判断成立, 这就意味着原本的树是空的. 因此触发了对 `self.root` 的重新赋值. 35-38行, 通过判断 `key` 和 `y.key`, 来确定插入节点该在 `y` 左还是右. 

同之前一样, 调用 `insert` 的时间复杂度为 $O(h)$, 是树深度的量级. 

### 删除元素

从二叉搜索树中删除一个元素并确保其特性保持稍微比较复杂. 一般的, 我们面对三种情况:

1.  待删除节点是一个叶子节点:
    此时我们只需要简单地删除它, 并将其父节点的孩子进行修改
2.  待删除节点有一个孩子:
    此时我们只需要将它的孩子及其子树提升到删除节点的位置, 并修改其父节点. 
3.  待删除节点 `z` 有两个孩子:
    这种情况是比较棘手的. 但根据二叉搜索树的性质, 我们的操作只会局限在删除节点开启的这个子树上. 我们只需要找到该节点的后继节点 `y`, 它在 `z` 的右子树中. 将它放置在删除位置, `z` 的左子树仍为 `y` 的左子树, 而 `z` 的右子树中的剩余部分则是 `y` 的右子树. 


```python{.line-numbers}
class binSearchTree:
    # other methods
    def transplant(self, des, src):
        """
        transplant subtree of src to des
        """
        if des == self.root:
            self.root = src
        else:
            par = self.par(des)
            if des == self.left(par):
                self.leftInd[par] = src
            else:
                self.rightInd[par] = src
            if not self.isEmpty(src):
                self.pInd[src] = par

    def delete(self, key):
        ptr = self.treeSearchPtr(self.root, key)
        if self.isEmpty(self.left(ptr)):
            self.transplant(ptr, self.right(ptr))
        elif self.isEmpty(self.right(ptr)):
            self.transplant(ptr, self.left(ptr))
        else:
            y = self.successor(ptr)
            if self.par(y) != ptr:
                self.transplant(y, self.right(y))
                self.rightInd[y] = self.rightInd[ptr]
                self.pInd[self.rightInd[y]] = y
            self.transplant(ptr, y)
            self.leftInd[y] = self.leftInd[ptr]
            self.pInd[self.leftInd[y]] = y

        self.key[ptr] = None
        self.val[ptr] = None
        self.size -= 1
```

我们实现了 `transplant` 方法来实现将 `src` 为根的子树转移到以 `des` 为根的节点. 其中 `treeSearchPtr` 方法实现了 `treeSearch`, 但返回的是指针值, 即 `list` 的索引.

我们着重分析第三种情况下的 `delete` 方法, 它正是25-32行. 其中25行找到 `ptr` 的后继位置. 之后:

26-29行工作于如果 `y` 不是 `ptr` 的右子结点的情况, 考虑一种情况(注意 `y` 作为后继节点, 它不存在左孩子.):

```
Node:   Left    Right   Parent
-------------------------------
p   :   ptr     -       -
ptr :   l       r       p
l   :   -       -       ptr
r   :   y       -       ptr
y   :   None    yr      r
```

27行将 `y` 的右子树转移到 `y` 的位置, 从而成为:

```
Node:   Left    Right   Parent
-------------------------------
p   :   ptr     -       -
ptr :   l       r       p
l   :   -       -       ptr
r   :   yr      -       ptr
y   :   None    yr      r
yr  :   -       -       r
```


28行将 `y` 的右孩子赋为 `ptr` 的右孩子. 

```
Node:   Left    Right   Parent
-------------------------------
p   :   ptr     -       -
ptr :   l       r       p
l   :   -       -       ptr
r   :   yr      -       ptr
y   :   None    r       r
yr  :   -       -       r
```

29行将 `y` 的右孩子的父节点赋为 `y`

```
Node:   Left    Right   Parent
-------------------------------
p   :   ptr     -       -
ptr :   l       r       p
l   :   -       -       ptr
r   :   yr      -       y
y   :   None    r       r
yr  :   -       -       r
```

30-32行处理 `ptr` 和 `y`. 
1.  如果 26 行的判断触发为真

    30行将 `y` 的子树转移到 `ptr`, 而 `ptr` 节点的信息是不变的.

    ```
    Node:   Left    Right   Parent
    -------------------------------
    p   :   y       -       -
    ptr :   l       r       p
    l   :   -       -       ptr
    r   :   yr      -       y
    y   :   None    r       p
    yr  :   -       -       r
    ```

    31行将 `y` 的左子节点赋为原 `ptr` 的左节点, 即

    ```
    Node:   Left    Right   Parent
    -------------------------------
    p   :   y       -       -
    ptr :   l       r       p
    l   :   -       -       ptr
    r   :   yr      -       y
    y   :   l       r       p
    yr  :   -       -       r
    ```

    32行将 `y.left` 的父节点赋值为 `y`
    
    ```
    Node:   Left    Right   Parent
    -------------------------------
    p   :   y       -       -
    ptr :   l       r       p
    l   :   -       -       y
    r   :   yr      -       y
    y   :   l       r       p
    yr  :   -       -       r
    ```

    约化(去除`ptr`节点)给出

    ```
    Node:   Left    Right   Parent
    -------------------------------
    p   :   y       -       -
    l   :   -       -       y
    r   :   yr      -       y
    y   :   l       r       p
    yr  :   -       -       r
    ```

    正是我们需要的. `p` 的左孩子为 `y`, `y` 的孩子关系同之前 `ptr` 一样, `y` 的右子树中不存在 `y` 自己. 

2.  如果 26 行的判断没有触发, 考虑一种情况:

    ```
    Node:   Left    Right   Parent
    -------------------------------
    p   :   ptr     -       -
    ptr :   l       y       p
    l   :   -       -       ptr
    y   :   None      yr      ptr
    ```

    30行执行:

    ```
    Node:   Left    Right   Parent
    -------------------------------
    p   :   y       -       -
    ptr :   l       y       p
    l   :   -       -       ptr
    y   :   None      yr      p
    ```

    31行:

    ```
    Node:   Left    Right   Parent
    -------------------------------
    p   :   y       -       -
    ptr :   l       y       p
    l   :   -       -       ptr
    y   :   l       yr      p
    ```

    32行:

    ```
    Node:   Left    Right   Parent
    -------------------------------
    p   :   y       -       -
    ptr :   l       y       p
    l   :   -       -       y
    y   :   l       yr      p
    ```

    约化后正是

    ```
    Node:   Left    Right   Parent
    -------------------------------
    p   :   y       -       -
    l   :   -       -       y
    y   :   l       yr      p
    ```

    亦为所求.

从而我们证明了算法的正确性

34-36行删除了对应位置的 `key` 和 `val`, 同时使树的尺寸减少 1. 值得注意的是, 在这种实现中, 为了保证`delete`操作时间是 $O(h)$, 我们没有动态地修改 `self.rightInd` 等列表, 它们记录了树的结构. 这使得树中总存在一些冗余, 但由于指针的存储需要的空间更少, 因此在拥有指针的语言实现中这种冗余带来的损耗是少的. 使用哈希的实现也会有少的损耗. 对存取来说最大的困难在于值 `val`, 因此35行释放这部分空间使得该实现的效率还是可以接受的. 




