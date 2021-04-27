# 概率分析和随机算法

## 雇佣问题

雇佣问题被抽象为给定一个数组, 其元素之间存在序关系. 问题为找出其中的最大元素. 即:

-  **Input:** $S= \{x_i\}_{i=0}^{N-1}$
-  **Output:** $x = \max S$

该问题最一般的求解在于遍历数组, 使用一个寄存器变量储存已遍历过得元素中的最大值. 而每看到新的元素就更新一下这个变量. 当遍历完成时它返回寄存器中的变量. 因此它具有 $\Theta(1)$ 的空间复杂度, 而其时间复杂度为 $O(N)$.

我们这里主要讨论它的输入是一些随机实例的情形. 


### 最坏情形

我们忽略掉遍历整个数组的时间, 而考虑造成时间差异的核心在进行寄存器的更新. 因此算法的时间复杂度被最大值前递增子列的长度有关.

雇佣问题的最坏情形自然是所有元素从小到大排列, 从而寄存器必须更新 $N$ 次才能给出正确的结果, 即 $O(N)$ 的最大复杂度. 我们的问题在于如果输入是随机生成的, 它的平均复杂度是多少. 

## 关于随机算法的问题

### 练习 5.1-2

描述 `rand(a,b)` 的过程的一种实现, 它只调用 `rand(0,1)`.

我们可以这样实现该函数:

```python
def rand() -> float:
    """
    Return a random float number (uniform) in range [0,1)
    """
    pass

def rand(a, b) -> int:
    """
    Return a random float number (uniform) in range [a, b)
    """
    return a + (b - a) * rand()
```

### 练习 5.1-3

考虑给定的以概率 `p` 返回 1, `1-p` 返回 0的子程序, 实现一个均等概率返回0, 1的算法.

```python
def rand() -> int:
    """
    Return 0 with probability 1-p, 1 with p
    """
    pass

def rand_half() -> int:
    """
    Return 0, 1 with equal probability
    """
    while True:
        x, y = rand(), rand()
        if x==0 and y==1:
            return 1
        elif x==1 and y==0:
            return 0
        else:
            continue
```

该算法逃出循环给出返回值的概率为 $2p(1-p)$, 从而, 期望运行时间为 $1/(2p(1-p))$