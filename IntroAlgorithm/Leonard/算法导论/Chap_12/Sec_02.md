# 二叉搜索树

## 查询二叉搜索树

除了通常的按照 `key` 属性查找节点, 二叉搜索树还支持如 找到最小和最大, 后继和前驱这些操作. 

### 查找

在二叉搜索树中查找一个关键字可以使用二分查找配合递归的办法. 其实现十分简单:

```python{.line-numbers}
class binSearchTree:
    # Other methods
    def treeSearch(self, x, key):
        if x is not None:
            print(self.key[x], key)
        if self.isEmpty(x):
            return None, None
        elif self.key[x] == key:
            return self.key[x], self.val[x]
        else:
            if self.key[x] > key:
                return self.treeSearch(self.left(x), key)
            else:
                return self.treeSearch(self.right(x), key)
```

不难看到, 由于每次递归都将会使节点的深度加一, 因此该方法的时间复杂度为 $O(h)$, 其中 $h$ 为树的深度. 

### 查找最小最大元素

从根节点出发, 没一步都沿着左(右)子树下降, 那么就可以找到树中拥有最小(大)关键字的元素. 其实现如下

```python{.line-numbers}
class binSearchTree:
    # other methods
    def treeDive(self, x, method):
        ch = method(x)
        while not self.isEmpty(ch):
            x = ch
            ch = method(x)
        return self.key[x], self.val[x]

    
    def findMin(self):
        return self.treeDive(self.getRoot(), self.left)

    def findMax(self):
        return self.treeDive(self.getRoot(), self.right)
```

这样实现的时间复杂度同样只有树的深度, 为 $O(h)$

### 后继和前驱

给定二叉搜索树中的一个节点, 我们可能需要找到按照中序遍历下的它的前一个元素和后一个元素, 这种操作被称为找到它的前驱和后继. 在二叉搜索树中, 我们可以不调用比较方法来实现这一点, 只需要注意到, 任意节点的前驱正是其左子树的最大元素(关键字), 而后继则是其右子树的最小元素. 其实现使用了上面定义的 `treeDive`:

```python{.line-numbers}
class binSearchTree:
    # other methods
    def predecessor(self, x):
        return self.treeDive(self.left(x), self.right)

    def successor(self, x):
        return self.treeDive(self.right(x), self.left)
```

同样的, 该操作的时间复杂度也是 `O(h)`.