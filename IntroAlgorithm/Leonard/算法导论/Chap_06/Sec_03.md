# 堆排序

## 优先队列

**优先队列(priority queue)** 是一种用来维护由一组元素构成集合 $S$ 的数据结构, 其中每个元素都有一个相关联的数值值成为 **key**, 一个 **最大优先队列** 支持如下操作

1.  `insert(S, x)`: 把元素 `x` 插入集合 $S$ 中, 等价于 $S\leftarrow S \cup \{x\}$
2.  `maximum(S)`: 返回 $S$ 中有最大 **key** 的元素
3.  `extractMax(S)`: 去掉并返回 $S$ 中有最大 **key** 的元素
4.  `increaseKey(S, x, k)`: 将元素 `x` 的 **key** 值增加到 `k`, 其中 我们假设 $k\geq x$.

优先队列的实现可以参考 `../Code/Chap_06/maxPriorityQueue.py`. 值得注意的是, 优先队列中的操作都有着 $O(\log N)$ 的时间复杂度. 