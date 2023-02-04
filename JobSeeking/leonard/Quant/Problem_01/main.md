# 问题 1

考虑一个赌局, 基于200张4种颜色的牌, 每种的数字为1 - 50. 甲乙两个对手, 每人随机分发两张牌并且设置一个底牌(场上涉及到共5张牌), 胜负规则为:

如果两人手牌均能加上底牌配成对子(数字相同, 颜色不同), 那么谁的对子数字大谁赢.
如果一人能配成对子一人不能, 那么配成对子的人赢
如果两人都没有对子, 那么谁的最大数字大谁赢.

否则平局.

举例:

甲手牌 [1, 2], 乙手牌 [49, 50]:
如果底牌为5, 那么两人: 甲([1, 2, 5]), 乙([5, 49, 50]), 均无对子, 但乙牌面更大, 从而乙胜.
如果底牌为1, 那么甲可以配对成对子 [1, 1], 而乙无对子, 从而甲胜.

另一个例子

甲手牌 [1, 1], 乙手牌 [49, 50]:
如果底牌不为49, 50, 那么甲胜, 因为甲有对子.
如果底牌恰为49, 50 中的一个, 那么乙胜, 因为乙得到更大的对子.

该问题要求计算, 给定甲手牌为输入(仅数字, 不包含颜色信息), 计算甲的胜率(平局算输), 假设乙的手牌, 底牌均未知.

# 分析

如果通过穷举所有可能配置会导致运行时间过长. 其优化思路在于注意到最终判断胜负只看数字, 因此颜色上的简并可以手动计算. 

首先我们需要编写一个判断胜负的函数:

```python
from typing import Tuple


def getPair(a1: int, a2: int, c: int) -> Tuple[bool, int]:
    """
    返回 a1, a2, c 三个数组成的对子, 如果无法组成对子则返回 False, max_number
    """
    if a1 == a2:
        return True, a1
    if a1 == c or a2 == c:
        return True, c
    return False, max(a1, a2, c)


def isWin(a1: int, a2: int, b1: int, b2: int, c: int) -> bool:
    """
    返回配置为 a1, a2 和 b1, b2, 且底牌为 c 时 A 是否胜利, 平局算负
    """
    A_pair, A_val = getPair(a1, a2, c)
    B_pair, B_val = getPair(b1, b2, c)
    if A_pair and (not B_pair):
        return True
    if (not A_pair) and B_pair:
        return False
    return A_val > B_val
```

接下来我们需要计算每种 a1, a2, b1, b2, c 的数字配置对应的颜色配置. 注意到只能有4种颜色, 因此如果 a1, a2, b1, b2, c 对应的颜色取决于其按照相同数字分组的情况. 假设分为 $k$ 组, 每组中有数字 $n_k$, 那么颜色应当有 $C_4^{n_k} n_k!$ 种. 因此

```python
import math

def countColorNumber(a1: int, a2: int, b1: int, b2: int, c: int) -> int:
    counter = {}
    for x in [a1, a2, b1, b2, c]:
        if x not in counter:
            counter[x] = 1
        else:
            counter[x] += 1
    num = counter.values()
    result = 1
    for x in num:
        result *= math.factorial(4) / math.factorial(4 - x)
    return result
```

而最终计算成功概率的代码只需要遍历所有可能数字配置:

```python
def solution(a1: int, a2: int) -> float:
    total = 0
    success = 0
    for b1 in range(1, 50):
        for b2 in range(1, 50):
            for c in range(1, 50):
                count = countColorNumber(a1, a2, b1, b2, c)
                if isWin(a1, a2, b1, b2, c):
                    success += count
                total += count
    return success / total
```