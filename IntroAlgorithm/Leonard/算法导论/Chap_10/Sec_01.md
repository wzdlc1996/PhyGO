# 基本数据结构

## 栈和队列

栈和队列是动态集合的不同实例. 

**栈(stack)** 是后进先出的, 拥有如下的几种操作:

1.  push: 将一个元素插入栈中
2.  pop: 将最近插入的元素返回并删除出栈

python 中的 `list` 类型事实上拥有栈的操作, 但这里我们纯粹作为演示地实现一个.

```python{.line-numbers}
class stack:
    def __init__(self):
        self.body = []
        self.top = -1
    
    def push(self, x):
        self.body += [x]
        self.top += 1

    def pop(self):
        x = self.body[self.top]
        self.body = self.body[:self.top]
        self.top -= 1
    
    def empty(self):
        return self.top == -1
```

可以看到 `self.top` 存放了最近插入元素的索引. 在C中我们事实上可以使用指针来实现这一点.

**队列(queue)** 是先进先出的, 拥有如下几种操作:

1.  enqueue: 将一个元素进入队列
2.  dequeue: 将最早进入的元素返回并移出队列

```python{.line-numbers}
class queue:
    def __init__(self):
        self.body = []
    
    def enqueue(self, x):
        self.body += [x]

    def dequeue(self, x):
        x = self.body[0]
        self.body = self.body[1:]
```

这里我们不再使用某个变量标记开头因为它总在第一个. 事实上栈我们同样不需要top. 但在某些静态数组实现中, 我们可能需要用这样的变量来标记数组的 "可见部分". 比如如下的一种实现:

```python{.line-numbers}
class queue:
    # fixed body
    def __init__(self, size):
        self.body = [0] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def cap(self):
        return self.tail - self.head
    
    def enqueue(self, x):
        if self.tail < self.size:
            self.body[self.tail] = x
            self.tail += 1
        elif self.cap() < self.size:
            self.body[:self.cap()] = self.body[self.head:self.tail]
            self.tail = self.tail - self.head
            self.head = 0
            self.enqueue(x)
        else:
            raise ValueError("Queue overflow")

    def dequeue(self):
        x = self.body[head]
        self.head += 1
        return x
```