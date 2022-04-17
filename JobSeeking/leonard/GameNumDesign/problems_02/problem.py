def genBooleanVec(n: int) -> list:
    if n == 1:
        return [[0], [1]]
    sub = genBooleanVec(n-1)
    return [[0] + x for x in sub] + [[1] + x for x in sub]

def genSol(pb: list) -> list:
    r = []
    n = len(pb)
    for i in range(n):
        if i == 0 or i == n-1:
            r.append(1)
        elif -pb[i-1] + 2 * pb[i+1] > 0:
            r.append(1)
        else:
            r.append(0)
    return r

r = genBooleanVec(6)
for pb in r:
    pa = genSol(pb)
    if pa == pb:
        print("Equalibrium:", pa, pb)