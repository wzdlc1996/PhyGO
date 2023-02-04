from typing import Tuple
import math


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


def countColorNumber(a1: int, a2: int, b1: int, b2: int, c: int) -> int:
    counter = {}
    for x in [a1, a2, b1, b2, c]:
        if x not in counter:
            counter[x] = 1
        else:
            counter[x] += 1
    num = counter.values()
    if len(num) == 1:
        return 0
    result = 1
    for x in num:
        result *= math.factorial(4) / math.factorial(4 - x)
    return result


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


print(solution(49, 50))
# print(solution(1, 2))