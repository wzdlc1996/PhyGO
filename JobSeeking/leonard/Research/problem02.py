c = int(input())
f = [float(x) for x in input().split()]
Amat = [[float(x) for x in input().split()] for _ in range(c)]

attention = [sum([a * b for a, b in zip(Arow, f)]) for Arow in Amat]

maxInd = 0
maxItem = attention[0]
for i, x in enumerate(attention):
    if x > maxItem:
        maxInd = i
        maxItem = x
    

print(maxInd)