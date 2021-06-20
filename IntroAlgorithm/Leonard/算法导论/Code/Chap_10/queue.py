#!/usr/bin/env python

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
        x = self.body[self.head]
        self.head += 1
        return x

    def __str__(self):
        return "queue_body:{}\nhead:{}, tail:{}".format(
            self.body,
            self.head,
            self.tail
        )

if __name__ == "__main__":
    qu = queue(1)
    qu.enqueue(1)
    print(qu)
    print(qu.dequeue())
    print(qu)
    qu.enqueue(1)
    print(qu)
    qu.enqueue(1)
