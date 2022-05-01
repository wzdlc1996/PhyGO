n, m = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
b = sorted([int(x) for x in input().split()])
q = int(input())
intervals = []
for _ in range(q):
    intervals.append([int(x) for x in input().split()])
    
def clas(l, r):
    reds = 0
    blues = 0
    for redx in a:
        if l <= redx <= r:
            reds += 1
        elif redx > r:
            break
    for bluex in b:
        if l <= bluex <= r:
            blues += 1
        elif bluex > r:
            break
    
    if reds > blues:
        return 1
    elif reds == blues:
        return 2
    else:
        return 3

c1 = c2 = c3 = 0
for interval in intervals:
    c = clas(*interval)
    if c == 1:
        c1 += 1
    elif c == 2:
        c2 += 1
    else:
        c3 += 1
print(c1, c2, c3)